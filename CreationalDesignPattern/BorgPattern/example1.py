"""
The Borg pattern (also known as the Monostate pattern) is a way to
implement singleton behavior, but instead of having only one instance
of a class, there are multiple instances that share the same state. In
other words, the focus is on sharing state instead of sharing instance
identity.
"""


class ClassA(object):
    _state = {}

    def __init__(self) -> None:
        self.__dict__ = self._state


class ClassB(ClassA):
    def __init__(self) -> None:
        super().__init__()


if __name__ == "__main__":
    a1 = ClassA()
    a2 = ClassA()
    a1.value = "Dipak"
    print(a2.value)
    b1 = ClassB()
    print(b1.value)
    print(a1 == a2)