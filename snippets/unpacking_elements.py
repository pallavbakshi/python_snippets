# Setting up pycharm
# Set up project interpreter, Preferences
# Set up python console interpreter, Preferences

record = ('Pallav', 1, 2, 'Bakshi')
first_name, *numbers, last_name = record

first_name
numbers
last_name

# Always
print(bool(isinstance(numbers, list)))


records = [
    ('foo', 1, 2),
    ('hello', 1),
    ('trial', 1, 2),
]

for tag, *args in records:
    if tag == 'foo':
        print(*args)
    elif tag == 'hello':
        print(*args)


def recursive_sum(items):
    head, *tail = items
    return head + recursive_sum(tail) if tail else head

# Be careful about recursion limit
recursive_sum([1, 2, 3, 4, 5])


head, *tail = [1]
head
tail
