numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
}
print(numbers)
print(numbers['one'])

information = {
    "name": "Edson",
    "Lastname": "Galan",
    "Age": 22,
}
print(information)
del information['Lastname']
print(information)

keys = information.keys()
print(keys)
print(type(keys))

values = information.values()
print(values)
print(type(values))

pairs = information.items()
print(pairs)
print(type(pairs))


# Contacts
contacts = {
    "Edson": {
        "Lastname": "Galan",
        "Age": 28,
    },
    "Juan": {
        "Lastname": "Perez",
        "Age": 23,
    },
    "Sara": {
        "Lastname": "Gonzalez",
        "Age": 25,
    }
}
print(contacts)
print(contacts["Sara"])