from generated.base_enum import BaseEnum
from generated.formats.nif.basic import Byte


class AGDConsistencyType(BaseEnum):

	__name__ = 'AGDConsistencyType'
	_storage = Byte

	AGD_MUTABLE = 0
	AGD_STATIC = 1
	AGD_VOLATILE = 2
