#%%  Leer oor lyste
# https://realpython.com/python-list/

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

print(colors[0])
print(colors[2])

# %%
# Lyste kan verskillende tipes bevat:

heterogeen = [42, "apple", True, {"name": "John Doe"}, (1, 2, 3), [3.14, 2.78]]
heterogeen[3]

# %%
# List literals

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
fruits = ["apple", "banana", "orange", "kiwi", "grape"]
cities = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Philadelphia"
]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

inventory = [
    {"product": "phone", "price": 1000, "quantity": 10},
    {"product": "laptop", "price": 1500, "quantity": 5},
    {"product": "tablet", "price": 500, "quantity": 20}
]

functions = [print, len, range, type, enumerate]

empty = []

#%%
# List constructor laat jou toe om lyste te maak in funksies:
def fibonacci_generator(stop):
    current_fib, next_fib = 0, 1
    for _ in range(0, stop):
        fib_number = current_fib
        current_fib, next_fib = next_fib, current_fib + next_fib
        yield fib_number


fibonacci_generator(10)


list(fibonacci_generator(10))

# %%


