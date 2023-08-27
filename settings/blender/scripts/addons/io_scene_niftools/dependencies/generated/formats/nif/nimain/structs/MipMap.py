from generated.base_struct import BaseStruct
from generated.formats.nif.imports import name_type_map


class MipMap(BaseStruct):

	"""
	Description of a mipmap within an NiPixelData object.
	"""

	__name__ = 'MipMap'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# Width of the mipmap image.
		self.width = name_type_map['Uint'](self.context, 0, None)

		# Height of the mipmap image.
		self.height = name_type_map['Uint'](self.context, 0, None)

		# Offset into the pixel data array where this mipmap starts.
		self.offset = name_type_map['Uint'](self.context, 0, None)
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'width', name_type_map['Uint'], (0, None), (False, None), (None, None)
		yield 'height', name_type_map['Uint'], (0, None), (False, None), (None, None)
		yield 'offset', name_type_map['Uint'], (0, None), (False, None), (None, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'width', name_type_map['Uint'], (0, None), (False, None)
		yield 'height', name_type_map['Uint'], (0, None), (False, None)
		yield 'offset', name_type_map['Uint'], (0, None), (False, None)
