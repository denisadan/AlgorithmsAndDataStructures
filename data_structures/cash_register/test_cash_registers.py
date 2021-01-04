import time

from data_structures.cash_register.cash_register import CashRegister, FasterCashRegister
from data_structures.cash_register.client import Woman

start = time.time()

client1 = Woman("Anna", "Johnson")

cr = CashRegister()
for i in range(10001):
    cr.add_client(client1)
for i in range(10000):
    cr.process()
print(time.time() - start)

start = time.time()

fastercr = FasterCashRegister()
for i in range(10001):
    fastercr.add_client(client1)

for i in range(10000):
    fastercr.process()

print(time.time() - start)
