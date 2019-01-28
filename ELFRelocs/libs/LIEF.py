__all__ = ("LIEFRelocator",)
from ELFMachine import ELFMachine

from .. import Relocator, RelocWrapper


class LIEFRelocWrapper(RelocWrapper):
	def __init__(self, reloc, table, symbol):
		self._reloc = reloc
		self.type = table(int(reloc.type))

	@property
	def offset(self):
		return self._reloc.address

	@property
	def addend(self):
		return self._reloc.addend

	@property
	def symbol_value(self):
		return self._reloc.symbol.value


class LIEFRelocator(Relocator):
	def __init__(self, liefBinary):
		arch = ELFMachine(int(liefBinary.concrete.header.machine_type))
		super().__init__(arch)
		self.liefBinary = liefBinary

	@property
	def B(self):
		return self.liefBinary.concrete.imagebase

	def relocFromPointerRawAddr(self, raw) -> RelocWrapper:
		backendReloc = self.liefBinary.concrete.get_relocation(raw)
		if backendReloc is not None:
			return LIEFRelocWrapper(backendReloc, self.table)
