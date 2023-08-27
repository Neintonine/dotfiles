from generated.formats.nif.imports import name_type_map
from generated.formats.nif.nipsparticle.niobjects.NiPSFieldForce import NiPSFieldForce


class NiPSTurbulenceFieldForce(NiPSFieldForce):

	"""
	Inside a field, updates particle velocity to simulate the effects of turbulence.
	"""

	__name__ = 'NiPSTurbulenceFieldForce'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.frequency = name_type_map['Float'](self.context, 0, None)
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'frequency', name_type_map['Float'], (0, None), (False, None), (None, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'frequency', name_type_map['Float'], (0, None), (False, None)
