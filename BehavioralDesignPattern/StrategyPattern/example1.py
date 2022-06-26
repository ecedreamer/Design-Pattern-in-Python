""" 
Strategy design pattern 

In computer programming, the strategy pattern (also known as the policy pattern) is a behavioral software design pattern that enables selecting an algorithm at runtime. Instead of implementing a single algorithm directly, code receives run-time instructions as to which in a family of algorithms to use.

Components: 
    1. Cotext:  It maintains a reference to one of the concrete strategies.
    2. Strategy Interface: Common to all Stretegy implementation class so that context can communicate
    3. Concrete Strategy classes: Implementation class of several types of Stretegy


Use Case: If a task is to be done according to certain strategies that can be changed in run time

-----------------------About the Example -------------------------------------------
This examples explains the process of setting of Web API server environment according to the backend framework used

"""
from __future__ import annotations
from abc import ABC, abstractmethod
import time


# Context Class

class WebApiServer:
    def __init__(self, name: str, root_url: str, backend: BackendFramework) -> None:
        self.name = name
        self.root_url = root_url
        self.backend = backend

    def install(self):
        self.backend.install_runtime_env()
        self.backend.install_dependencies()

    def __repr__(self) -> str:
        return f"{self.name}({self.root_url}) API server developed using {self.backend.name}/{self.backend.base_language}."


# Strategy Interface

class BackendFramework(ABC):
    def __init__(self, name: str, base_language: str) -> None:
        """ Backend Framework for Web Server

        Args:
            name (str): name of the framework
            base_language (str): base language which the framework is written in
        """        
        self.name = name
        self.base_language = base_language

    @abstractmethod
    def install_runtime_env(self) -> None:
        """ installing runtime environment for the programming language"""

    @abstractmethod
    def install_dependencies(self) -> None:
        """ installing dependencies for the framework"""


# Strategy Implementations

class DjangoFramework(BackendFramework):
    def install_runtime_env(self) -> None:
        """ installing runtime environment for the programming language"""
        print(f"Installing {self.base_language} in the server")
        time.sleep(1)
        print("Installing pip in the server")
        time.sleep(1)
        print(f"{self.base_language} and pip installed successfully")
        time.sleep(1)

    def install_dependencies(self) -> None:
        """ installing dependencies for the framework"""
        print("Running 'pip install django' ")
        time.sleep(1)
        print("Successfully installed django==4.1.0 on your python environment")
        time.sleep(1)


class SpringFramework(BackendFramework):
    def install_runtime_env(self) -> None:
        """ installing runtime environment for the programming language"""
        print(f"Installing {self.base_language} in the server")
        time.sleep(1)
        print("{self.base_language} installed successfully")
        time.sleep(1)

    def install_dependencies(self) -> None:
        """ installing dependencies for the framework"""
        print("Preparing to install spring framework")
        time.sleep(1)
        print("Successfully installed spring framework for java environment.")
        time.sleep(1)


# addning new framework here does not need to modify the existing codebase (Context and strategy classes)
# so it supports OPEN/CLOSED principle of SOLID Desing Principle.

def main():
    django_framework = DjangoFramework("Django", "Python")
    spring_framework = SpringFramework("Spring", "Java")

    print("\n--------Setting up environment for News API Server \n")
    news_api_server = WebApiServer(
        "Nepal News", "https://nepalnews.com.np/api/v1/", django_framework)
    news_api_server.install()

    print("\n--------Setting up environment for Bank API Server \n")

    bank_api_server = WebApiServer(
        "Nepal Development Bank", "https://nepaldevelopmentbank.com/api/v1/", spring_framework)
    bank_api_server.install()

    print("------------ SUCCESSFULLY SETUP API SERVER ENVIRONMENTS------------")
    print(news_api_server)
    print(bank_api_server)


if __name__ == "__main__":
    main()
