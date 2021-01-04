from data_structures.cash_register.client import Client
from data_structures.queue.queue import Queue, QueueDeque


class CashRegister:

    def __init__(self) -> None:
        self.clients = Queue()

    def __str__(self) -> str:
        return f"{self.clients}"

    def add_client(self, client: Client):
        self.clients.push(client)
        # print(f"Added client: {client}")

    def process(self) -> Client:
        # print(f"Removed client")
        return self.clients.pop()


# client1 = Woman("Anna", "Johnson")
# client2 = Man("John", "Smith")
# client3 = Child("Chris", "Novak")
#
# cr = CashRegister()
# cr.add_client(client1)
# cr.add_client(client2)
# cr.add_client(client3)
#
# print(f"{cr}")
#
# cr.process()
# cr.process()
#
# print(f"{cr}")


class FasterCashRegister(CashRegister):
    def __init__(self) -> None:
        super().__init__()
        self.clients = QueueDeque()

    def process(self):
        self.clients.pop()
