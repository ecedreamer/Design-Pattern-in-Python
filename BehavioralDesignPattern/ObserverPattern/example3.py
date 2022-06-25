"""
Simple Observer Pattern
"""


class Subscriber:
    def __init__(self, name) -> None:
        self.name = name
        self.message = None

    def receive(self, message:str) -> None:
        """
        Its a receiver method which receives the notification from publisher. 
        Args:
            message (str): message from the publisher
        """        
        self.message = message
        print(f"@{self.name}: {self.message}")


class Publisher:
    def __init__(self, events) -> None:
        self.subscribers = {event: dict() for event in events}

    def get_subscribers(self, event) -> dict:
        return self.subscribers[event]

    def register(self, event, subscriber: Subscriber, callback=None):
        if callback is None:
            callback = getattr(subscriber, "receive")
        self.get_subscribers(event)[subscriber] = callback
    
    def unregister(self, event, subscriber) -> None:
        del self.get_subscribers(event)[subscriber]

    def notify(self, event:str, message:str) -> None:
        for _, callback in self.get_subscribers(event).items():
            callback(message)


def main():
    EVENTS = ["News", "Songs"]
    pub = Publisher(EVENTS)

    sub1 = Subscriber("sub1")
    sub2 = Subscriber("sub2")
    sub3 = Subscriber("sub3")

    pub.register(EVENTS[0], sub1, sub1.receive)
    pub.register(EVENTS[0], sub2, sub2.receive)
    pub.register(EVENTS[1], sub3, sub3.receive)

    pub.notify(EVENTS[0], "Breaking news: Python has become the number one programming language.!")

    pub.unregister(EVENTS[0], sub2)
    pub.notify(EVENTS[1], "A new sont has uploaded to Python Youtube Channel sung by Anaconda.")


if __name__ == "__main__":
    main()