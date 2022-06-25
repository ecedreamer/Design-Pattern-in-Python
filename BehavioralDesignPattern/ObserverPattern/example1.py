"""
Simple Observer Pattern
"""


class Subscriber:
    """ subscriber class """
    def __init__(self, name) -> None:
        self.name = name
        self.message = None

    def receive(self, message:str) -> None:
        """_summary_

        Args:
            message (str): _description_
        """        
        self.message = message
        print(f"@{self.name}: {self.message}")


class Publisher:
    def __init__(self) -> None:
        self.subscribers = set()

    def register(self, subscriber: Subscriber):
        self.subscribers.add(subscriber)
    
    def unregister(self, subscriber):
        self.subscribers.discard(subscriber)

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.receive(message)


def main():
    pub = Publisher()

    sub1 = Subscriber("sub1")
    sub2 = Subscriber("sub2")
    sub3 = Subscriber("sub3")

    pub.register(sub1)
    pub.register(sub2)
    pub.register(sub3)

    pub.notify("Hello world!")

    pub.unregister(sub2)
    pub.notify("Sub2 has unsubscribed.")


if __name__ == "__main__":
    main()