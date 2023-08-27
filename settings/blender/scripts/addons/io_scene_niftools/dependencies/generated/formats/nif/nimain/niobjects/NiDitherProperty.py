from generated.formats.nif.imports import name_type_map
from generated.formats.nif.nimain.niobjects.NiProperty import NiProperty


class NiDitherProperty(NiProperty):

	"""
	NiDitherProperty allows the application to turn the dithering of interpolated colors and fog values on and off.
	"""

	__name__ = 'NiDitherProperty'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.flags = name_type_map['DitherFlags'](self.context, 0, None)
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'flags', name_type_map['DitherFlags'], (0, None), (False, None), (None, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'flags', name_type_map['DitherFlags'], (0, None), (False, None)
