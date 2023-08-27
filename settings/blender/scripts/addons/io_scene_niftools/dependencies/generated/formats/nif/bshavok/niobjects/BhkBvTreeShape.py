from generated.formats.nif.bshavok.niobjects.BhkShape import BhkShape
from generated.formats.nif.imports import name_type_map


class BhkBvTreeShape(BhkShape):

	"""
	Bethesda extension of hkpBvTreeShape. hkpBvTreeShape adds a bounding volume tree to an hkpShapeCollection.
	A bounding volume tree is useful for testing collision between a moving object and large static geometry.
	"""

	__name__ = 'bhkBvTreeShape'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# The shape.
		self.shape = name_type_map['Ref'](self.context, 0, name_type_map['BhkShape'])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'shape', name_type_map['Ref'], (0, name_type_map['BhkShape']), (False, None), (None, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'shape', name_type_map['Ref'], (0, name_type_map['BhkShape']), (False, None)
