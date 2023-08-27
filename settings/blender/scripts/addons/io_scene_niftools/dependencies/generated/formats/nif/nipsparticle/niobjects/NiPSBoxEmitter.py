from generated.formats.nif.imports import name_type_map
from generated.formats.nif.nipsparticle.niobjects.NiPSVolumeEmitter import NiPSVolumeEmitter


class NiPSBoxEmitter(NiPSVolumeEmitter):

	"""
	A particle emitter that emits particles from a rectangular volume.
	"""

	__name__ = 'NiPSBoxEmitter'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.emitter_width = name_type_map['Float'](self.context, 0, None)
		self.emitter_height = name_type_map['Float'](self.context, 0, None)
		self.emitter_depth = name_type_map['Float'](self.context, 0, None)
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'emitter_width', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'emitter_height', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'emitter_depth', name_type_map['Float'], (0, None), (False, None), (None, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'emitter_width', name_type_map['Float'], (0, None), (False, None)
		yield 'emitter_height', name_type_map['Float'], (0, None), (False, None)
		yield 'emitter_depth', name_type_map['Float'], (0, None), (False, None)
