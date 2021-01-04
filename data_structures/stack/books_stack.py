# Write code simulating Stack of books. The class should allow you to add and remove books from Stack,
# browsing titles in Stack and last position on Stack. Use magic methods to allow:
#
# adding Stacks together
# comparing Stack sizes
# Stack's string representation
# stating stack length
# STACK = LIFO = LastInFirstOut
from collections import deque


class BooksStack:
    def add_new_book(self, title):
        self.stack.append(title)

    def get_book(self):
        return self.stack.pop()

    def all_books(self) -> deque:
        return self.stack

    def __init__(self, stack_name: str, category: str):
        self.stack = deque()  # self.stack: List[str] = []
        self.stack_name = stack_name
        self.category = category

    def __add__(self, second_stack):
        new = BooksStack(stack_name=self.stack_name,
                         category=self.category)
        new.stack = self.stack + second_stack.stack
        return new

    # comparision
    def __gt__(self, second_stack):
        return len(self.stack) > len(second_stack)

    def __lt__(self, second_stack):
        return len(self.stack) < len(second_stack)

    def __ge__(self, second_stack):
        return len(self.stack) >= len(second_stack)

    def __le__(self, second_stack):
        return len(self.stack) <= len(second_stack)

    def __str__(self):
        return f'Stack {self.stack_name} with category of books {self.category}'

    def __repr__(self):
        books = ' '.join(self.stack)
        return f'stack_name: {self.stack_name} \n category: {self.category} \n books: {books}'

    def __len__(self):
        return len(self.stack)


my_books = BooksStack("My Stack of Books", "Natural")

my_books.add_new_book("Cheetahs")
my_books.add_new_book("Elephants")
my_books.add_new_book("Cats")

print(my_books.all_books())
# print(my_books.get_book())
# print(my_books.get_book())
# print(my_books.all_books())

# her_books = BooksStack("Her Stack of Books", "Natural")
# her_books.add_new_book("Horses")
# print(her_books.all_books())
# my_books = my_books + her_books
# print(my_books.all_books())
#
# print(my_books > her_books)
# print(my_books <= her_books)
#
# print(my_books)
# print(repr(my_books))
#
# print(len(my_books))


class Stack:
    def __init__(self):
        self.items = deque()

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)