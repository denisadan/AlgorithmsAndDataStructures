import abc


class Client(abc.ABC):
    def __init__(self, first_name: str, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @abc.abstractmethod
    def __str__(self) -> str:
        pass


class Woman(Client):
    def __str__(self) -> str:
        return f"Mrs {self.first_name} {self.last_name}"


class Man(Client):
    def __str__(self) -> str:
        return f"Mr {self.first_name} {self.last_name}"


class Child(Client):
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} jr"
