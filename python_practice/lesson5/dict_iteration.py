people = {
    "Alex": 29,
    "Den": 35,
    "Ivan": 18
}
print(list(people.keys()))
for name in people.keys():
    print(name)

for age in people.values():
    print(age)

for person in people.items():
    print(person)

for name, age in people.items():
    print(f"My name is {name}, I am {age} years old")
