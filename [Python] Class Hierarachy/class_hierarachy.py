from ast import Str
import numpy


class InnerObject(object):
    __slots__ = "A", "B"
    def __init__(self, A:int = 0, B:int = 0) -> None:
        print("InnerObject created.\n")
        self.A = A
        self.B = B
    def clone(self):
        return InnerObject(self.A, self.B)

class OuterObject(object):
    __slots__ = "IO", "C"
    def __init__(self, IO:InnerObject = None, C:Str = "Default C") -> None:
        print("OuterObject created.\n")
        if IO != None:
            self.IO = IO
        else:
            self.IO = InnerObject()
        self.C = C
    def clone(self):
        return OuterObject(self.IO.clone(), self.C)

class BaseClass(object):
    __slots__ = "A", "B", "OO"
    def __init__(self, A:int = 0, B:int = 0, OO:OuterObject = None) -> None:
        print("BaseClass created.\n")
        self.A = A
        self.B = B
        if OO != None:
            self.OO = OO
        else:
            self.OO = OuterObject()
    def clone(self):
        return BaseClass(self.A, self.B, self.OO.clone())

class DerivedClass(BaseClass):
    __slots__ = "D", "E", "OO2"
    def __init__(self, A: int = 0, B: int = 0, OO: OuterObject = None, D:int = 0, E:Str = "Default E", OO2:OuterObject = None) -> None:
        super().__init__(A, B, OO)
        print("DerivedClass created.\n")
        self.D = D
        self.E = E
        if OO2 != None:
            self.OO2 = OO2
        else:
            self.OO2 = OuterObject()
    def clone(self):
        return DerivedClass(self.A, self.B, self.OO.clone(), self.D, self.E, self.OO2.clone())


