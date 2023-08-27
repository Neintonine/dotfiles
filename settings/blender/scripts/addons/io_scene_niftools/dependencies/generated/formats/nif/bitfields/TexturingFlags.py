from generated.bitfield import BasicBitfield
from generated.bitfield import BitfieldMember
from generated.formats.nif.basic import Bool
from generated.formats.nif.basic import Ushort
from generated.formats.nif.enums.ApplyMode import ApplyMode


class TexturingFlags(BasicBitfield):

	"""
	Flags for NiTexturingProperty
	"""

	__name__ = 'TexturingFlags'
	_storage = Ushort
	multitexture = BitfieldMember(pos=0, mask=0x0001, return_type=Bool.from_value)
	apply_mode = BitfieldMember(pos=1, mask=0x000E, return_type=ApplyMode.from_value)
	decal_count = BitfieldMember(pos=4, mask=0x0FF0, return_type=Ushort.from_value)

	def set_defaults(self):
		pass
