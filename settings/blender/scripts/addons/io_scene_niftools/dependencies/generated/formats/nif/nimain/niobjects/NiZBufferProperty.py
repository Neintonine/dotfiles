from generated.formats.nif.imports import name_type_map
from generated.formats.nif.nimain.niobjects.NiProperty import NiProperty


class NiZBufferProperty(NiProperty):

	"""
	Allows applications to set the test and write modes of the renderer's Z-buffer and to set the comparison function used for the Z-buffer test.
	"""

	__name__ = 'NiZBufferProperty'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.flags = name_type_map['ZBufferFlags'].from_value(3)

		# Z-Test function. In Flags from 20.1.0.3 on.
		self.function = name_type_map['TestFunction'].TEST_LESS_EQUAL
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'flags', name_type_map['ZBufferFlags'], (0, None), (False, 3), (None, None)
		yield 'function', name_type_map['TestFunction'], (0, None), (False, name_type_map['TestFunction'].TEST_LESS_EQUAL), (lambda context: 67174412 <= context.version <= 335544325, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'flags', name_type_map['ZBufferFlags'], (0, None), (False, 3)
		if 67174412 <= instance.context.version <= 335544325:
			yield 'function', name_type_map['TestFunction'], (0, None), (False, name_type_map['TestFunction'].TEST_LESS_EQUAL)
