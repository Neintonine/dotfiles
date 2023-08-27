from generated.array import Array
from generated.formats.nif.imports import name_type_map
from generated.formats.nif.niparticle.niobjects.NiPSysModifier import NiPSysModifier


class BSPSysScaleModifier(NiPSysModifier):

	__name__ = 'BSPSysScaleModifier'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.num_scales = name_type_map['Uint'](self.context, 0, None)
		self.scales = Array(self.context, 0, None, (0,), name_type_map['Float'])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'num_scales', name_type_map['Uint'], (0, None), (False, None), (None, None)
		yield 'scales', Array, (0, None, (None,), name_type_map['Float']), (False, None), (None, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'num_scales', name_type_map['Uint'], (0, None), (False, None)
		yield 'scales', Array, (0, None, (instance.num_scales,), name_type_map['Float']), (False, None)