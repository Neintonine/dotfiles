from generated.bitfield import BasicBitfield
from generated.bitfield import BitfieldMember
from generated.formats.nif.basic import Bool
from generated.formats.nif.basic import Ushort


class BhkWeldInfo(BasicBitfield):

	__name__ = 'bhkWeldInfo'
	_storage = Ushort
	angle_edge_1 = BitfieldMember(pos=0, mask=0x001F, return_type=Ushort.from_value)
	angle_edge_2 = BitfieldMember(pos=5, mask=0x03E0, return_type=Ushort.from_value)
	angle_edge_3 = BitfieldMember(pos=10, mask=0x7C00, return_type=Ushort.from_value)
	unused_bit = BitfieldMember(pos=15, mask=0x8000, return_type=Bool.from_value)

	def set_defaults(self):
		self.angle_edge_1 = 15
		self.angle_edge_2 = 15
		self.angle_edge_3 = 15
		self.unused_bit = false
