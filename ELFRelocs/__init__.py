from enum import IntEnum

from .relocEnums import *
from .relocImpls import *


class SpecialSectionIndex(IntEnum):
	UNDEF = 0
	LORESERVE = 0xFF00
	LOPROC = 0xFF00
	BEFORE = 0xFF00
	AFTER = 0xFF01
	HIPROC = 0xFF1F
	ABS = 0xFFF1
	COMMON = 0xFFF2
	HIRESERVE = 0xFFFF


class RelocWrapper:
	def __init__(self, reloc, table):
		self._reloc = reloc
		self.type = table(reloc.entry["r_info_type"])

	@property
	def offset(reloc):
		raise NotImplementedError()

	@property
	def addend(reloc):
		raise NotImplementedError()

	@property
	def symbol_shndx(reloc):
		raise NotImplementedError()

	@property
	def symbol_value(reloc):  # reloc.symbol.st_value
		raise NotImplementedError()


class Relocator:
	def __init__(self, arch):
		self.table = archTableMapping[arch]

	def relocFromPointerRawAddr(self, raw) -> RelocWrapper:
		raise NotImplementedError()

	@property
	def B(self):
		return None

	@property
	def GOT(self):
		return None

	@property
	def L(self):
		return None

	def G(self, *args):
		return None

	def Z(self, *args):
		return None

	def computeRelocatedPtr(self, ptrVirtualAddr, ptrValue):
		reloc = self.relocFromPointerRawAddr(ptrVirtualAddr)
		if reloc:
			symVirtAddr = ptrValue + reloc.symbol_value
			P = ptrVirtualAddr + reloc.offset

			rImplName = reloc.type.name
			if hasattr(ELF_Relocs_Impls, rImplName):
				impl = getattr(ELF_Relocs_Impls, rImplName)

			#print(rImplName, impl)

			res = impl(symVirtAddr, reloc, P, GOT=self.GOT, G=self.G(), Z=self.Z(), L=self.L, B=self.B)

			if isinstance(res, tuple):
				format, relocatedRawPtr = res
			else:
				relocatedRawPtr = res
				format = None

			return format, relocatedRawPtr
		else:
			return None, ptrValue
