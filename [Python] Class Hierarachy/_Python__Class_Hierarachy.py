
from class_hierarachy import DerivedClass

from class_hierarachy import OuterObject
from class_hierarachy import InnerObject


DC1 = DerivedClass()
DC2 = DerivedClass(1, 2, OuterObject(InnerObject(11, 12), "C"), 3, "E", OuterObject(InnerObject(21, 22), "C2"))
