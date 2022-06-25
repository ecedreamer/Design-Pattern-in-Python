"""
Simple Observer Pattern
"""


class NewsSubscriber:
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


class SongSubscriber:
    """ subscriber class """
    def __init__(self, name) -> None:
        self.name = name
        self.message = None

    def notify(self, message:str) -> None:
        """_summary_

        Args:
            message (str): _description_
        """        
        self.message = message
        print(f"@{self.name}: {self.message}")


class Publisher:
    def __init__(self) -> None:
        self.subscribers = {}

    def register(self, subscriber, callback=None):
        if callback is None:
            callback = getattr(subscriber, "receive")
        self.subscribers[subscriber] = callback
    
    def unregister(self, subscriber):
        del self.subscribers[subscriber]

    def notify(self, message):
        for _, callback in self.subscribers.items():
            callback(message)


def main():
    pub = Publisher()

    sub1 = NewsSubscriber("sub1")
    sub2 = SongSubscriber("sub2")
    sub3 = NewsSubscriber("sub3")

    pub.register(sub1, sub1.receive)
    pub.register(sub2, sub2.notify)
    pub.register(sub3, sub3.receive)

    pub.notify("Hello world!")

    pub.unregister(sub2)
    pub.notify("Sub2 has unsubscribed.")


if __name__ == "__main__":
    main()