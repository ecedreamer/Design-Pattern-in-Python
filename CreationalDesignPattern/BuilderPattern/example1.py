"""
Builder Design Pattern:
Builder Design Pattern is a Creational Design Pattern which helps in building the complex object using
simple objects  and uses algorithmic approach ie. Step by Step. 

It provides clear separation and a unique layer between construction and representation of a specified object created by class.

It provides better control over construction process of the pattern created.

It gives the perfect scenario to change the internal representation of objects.

---------------------------------------------------------------------------------
In the Example below, BankCustomer object is a complex object which consists of simple objects of Profile, Address and Contact
classes. BankCustomerBuilder is a concrete implementation of BuilderInterface. Director class is responsible for creating 
BankCustomer object step by step. 


"""

from __future__ import annotations
from abc import ABC, abstractmethod


class BankCustomer:
    def __init__(self) -> None:
        self.profile = None
        self.address = None
        self.contact = None

    def set_profile(self, profile: Profile):
        self.profile = profile

    def set_address(self, address: Address):
        self.address = address

    def set_contact(self, contact: Contact):
        self.contact = contact

    def get_details(self):
        print(f"Name: {self.profile.name} ({self.profile.dob})")
        print(
            f"City: {self.address.municipality} - {self.address.ward}, {self.address.district}")
        print(f"Mobile: {self.contact.mobile}")


class Profile:
    def __init__(self, name, gender, dob, blood_group) -> None:
        self.name = name
        self.gender = gender
        self.dob = dob
        self.blood_group = blood_group


class Address:
    def __init__(self, ward, municipality, district, province) -> None:
        self.ward = ward
        self.municipality = municipality
        self.district = district
        self.province = province


class Contact:
    def __init__(self, email, mobile) -> None:
        self.email = email
        self.mobile = mobile


class BuilderInterface(ABC):
    @abstractmethod
    def create_profile(self, name, gender, dob, blood_group):
        """ creates profile information"""

    @abstractmethod
    def create_address(self, ward, municipality, district, province):
        """ creates address"""

    @abstractmethod
    def create_contact(self, email, mobile):
        """ creates contact info """


class BankCustomerBuilder(BuilderInterface):
    def create_profile(self, name, gender, dob, blood_group):
        """ creates profile information"""
        return Profile(name, gender, dob, blood_group)

    def create_address(self, ward, municipality, district, province):
        """ creates address"""
        return Address(ward, municipality, district, province)

    def create_contact(self, email, mobile):
        """ creates contact info """
        return Contact(email, mobile)


class Director:
    def __init__(self, builder: BuilderInterface) -> None:
        self.builder = builder

    def get_profile_info(self):
        name, gender, dob, blood_group = input(
            "Enter name, gender, dob, blood_group separated by comma: ").split(",")
        print(name, gender, dob, blood_group)
        return name, gender, dob, blood_group

    def get_address_info(self):
        ward, municipality, district, province = input(
            "Enter ward, municipality, district, province separated by comma: ").split(",")
        return ward, municipality, district, province

    def get_contact_info(self):
        email, mobile = input(
            "Enter email and mobile separated by comma: ").split(",")
        return email, mobile

    def build_customer(self):
        customer = BankCustomer()
        profile = self.builder.create_profile(*self.get_profile_info())
        customer.set_profile(profile)

        address = self.builder.create_address(*self.get_address_info())
        customer.set_address(address)

        contact = self.builder.create_contact(*self.get_contact_info())
        customer.set_contact(contact)
        print("Customer object built Successfully")
        return customer


def main():
    bank_customer_builder = BankCustomerBuilder()
    director = Director(bank_customer_builder)
    print("Building customer")
    customer = director.build_customer()
    customer.get_details()


if __name__ == "__main__":
    main()
