from functools import wraps


def _addend(fun):
	@wraps(fun)
	def WithAddend(symVirtAddr, reloc, P, GOT, G, Z, L, B):
		return fun(symVirtAddr, reloc, P, GOT, G, Z, L, B) + reloc.addend

	return WithAddend


def _GOTOFF(fun):
	@wraps(fun)
	def withMinusGOT(symVirtAddr, reloc, P, GOT, G, Z, L, B):
		#print("GOT=", GOT)
		return fun(symVirtAddr, reloc, P, GOT, G, Z, L, B) - GOT

	return withMinusGOT


def _GPLUS(fun):
	@wraps(fun)
	def withPlusG(symVirtAddr, reloc, P, GOT, G, Z, L, B):
		#print("G=", G)
		return G + fun(symVirtAddr, reloc, P, GOT, G, Z, L, B)

	return withPlusG


def _PC(fun):
	@wraps(fun)
	def withMinusP(symVirtAddr, reloc, P, GOT, G, Z, L, B):
		#print("P=", P)
		return fun(symVirtAddr, reloc, P, GOT, G, Z, L, B) - P

	return withMinusP


@_addend
def _simple(symVirtAddr, reloc, P, GOT, G, Z, L, B):
	#print("symVirtAddr=", symVirtAddr)
	return symVirtAddr


@_addend
def _Z(symVirtAddr, reloc, P, GOT, G, Z, L, B):
	#print("Z=", Z)
	return Z


@_addend
def _GOT(symVirtAddr, reloc, P, GOT, G, Z, L, B):
	#print("GOT=", GOT)
	return GOT


def _set_size(size):
	def set_size_decorator(fun):
		@wraps(fun)
		def sizeSet(symVirtAddr, reloc, P, GOT, G, Z, L, B):
			return size, fun(symVirtAddr, reloc, P, GOT, G, Z, L, B)

		return sizeSet

	return set_size_decorator


class ELF_Relocs_Impls:
	SIXTIFOUR = _set_size(8)(_simple)
	THIRTYTWO = _set_size(4)(_simple)
	SIXTEEN = _set_size(2)(_simple)
	EIGHT = _set_size(1)(_simple)
	PC8 = _set_size(1)(_PC(_simple))
	PC16 = _set_size(2)(_PC(_simple))
	PC32 = _set_size(4)(_PC(_simple))
	PC64 = _set_size(8)(_PC(_simple))
	GOTOFF = _set_size(4)(_GOTOFF(_simple))
	GOTOFF64 = _set_size(8)(_GOTOFF(_simple))
	GOTPC = _PC(_GOT)
	GOTPCREL = _set_size(4)(_GPLUS(GOTPC))
	SIZE32 = _set_size(4)(_Z)
	SIZE64 = _set_size(8)(_Z)

	@_addend
	def THIRTYTWO_PLT(symVirtAddr, reloc, P, GOT, G, Z, L, B):
		return L

	PLT32 = _set_size(4)(_PC(THIRTYTWO_PLT))

	@_addend
	def RELATIVE(symVirtAddr, reloc, P, GOT, G, Z, L, B):
		#print("B=", B)
		return B

	@_GPLUS
	def GOT32(symVirtAddr, reloc, P, GOT, G, Z, L, B):
		return reloc.addend

	def GLOB_DAT(symVirtAddr, reloc, P, GOT, G, Z, L, B):
		return symVirtAddr

	@_set_size(4)
	def JMP_SLOT(symVirtAddr, reloc, P, GOT, G, Z, L, B):
		return symVirtAddr

	@_set_size(4)
	def GOTPC32(symVirtAddr, reloc, P, GOT, G, Z, L, B):
		return P + _GOT(symVirtAddr, reloc, P, GOT, G, Z, L, B)
