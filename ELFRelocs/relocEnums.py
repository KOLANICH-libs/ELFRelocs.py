from enum import IntEnum

from ELFMachine import ELFMachine


class ELF_I686_RELOCS(IntEnum):
	# common
	NONE = 0

	PC32 = 2
	GOT32 = 3
	PLT32 = 4
	COPY = 5
	GLOB_DAT = 6
	JMP_SLOT = 7
	RELATIVE = 8

	GOTOFF = 9
	GOTPC = 10
	THIRTYTWO_PLT = 11

	# i686

	SIXTEEN = 20
	PC16 = 21
	EIGHT = 22
	PC8 = 23
	SIZE32 = 38


class ELF_AMD64_RELOCS(IntEnum):
	# common
	NONE = 0

	PC32 = 2
	GOT32 = 3
	PLT32 = 4
	COPY = 5
	GLOB_DaT = 6
	JMP_SLOT = 7
	RELATIVE = 8

	GOTOFF = 9
	GOTPC = 10
	THIRTYTWO_PLT = 11
	SIZE32 = 32

	# x86_64
	SIXTIFOUR = 1
	GOTPCREL = 9
	THIRTYTWO = 10
	THIRTYTWOS = 11

	SIXTEEN = 12
	PC16 = 13
	EIGHT = 14
	PC8 = 15
	PC64 = 24

	GOTOFF64 = 25
	GOTPC32 = 26
	SIZE64 = 33


archTableMapping = {
	ELFMachine.X86_64: ELF_AMD64_RELOCS,
	ELFMachine.EM_386: ELF_AMD64_RELOCS,
}
