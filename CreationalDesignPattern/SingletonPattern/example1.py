""" 
Singleton Design Pattern:
A Singleton is a class which has only one instance and a well-defined point of access to it.

Scenario: 
Suppose that we are making a system for an organization. To show organization information, we need to store it in a class. Since it is specific to that organization, so only one instance of that organization class can be created.
"""


class Organization(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance


    def __init__(self, name, address, contact) -> None:
        self.name = name
        self.address = address
        self.contact = contact



if __name__ == "__main__":
    org1 = Organization("ABC Company", "Kathmandu, Nepal", "01-5555555 / https://abccompany.com.np")
    org2 = Organization("DEF Company", "Kathmandu, Nepal", "01-5555555 / https://abccompany.com.np")
    assert org1 == org2
