from asyncio.format_helpers import _format_callback_source
from dataclasses import dataclass
from pprint import pprint
from faker import Faker
from faker.providers import internet

faker = Faker()
faker.add_provider(internet)

# Define Person and Machine classes
@dataclass(eq=True)
class Person:
    name: str

@dataclass
class Machine:
    ip: str

# Create list of Person instances
list_of_names = [
    Person(name=faker.name()) 
    for _ in range(20)
    ]
pprint(list_of_names)

# Create list of Machine instances
machines = [Machine(ip=faker.ipv4_private()) for _ in range(5)]
pprint(machines)

# Function to add a new person to the list
def add_person(name: str, person_list: list):
    new_person = Person(name=name)
    person_list.append(new_person)
    print(f"Added person: {new_person}")

# Function to remove a person from the list
def remove_person(name: str, person_list: list):
    person_list[:] = [p for p in person_list if p.name != name]
    print(f"Removed person with name: {name}")

# Function to filter people by name (returns a list of matching people)
def filter_persons(name: str, person_list: list):
    return [p for p in person_list if name.lower() in p.name.lower()]

# Function to add a new machine
def add_machine(ip: str, machine_list: list):
    new_machine = Machine(ip=ip)
    machine_list.append(new_machine)
    print(f"Added machine: {new_machine}")

# Function to remove a machine
def remove_machine(ip: str, machine_list: list):
    machine_list[:] = [m for m in machine_list if m.ip != ip]
    print(f"Removed machine with IP: {ip}")

# Function to filter machines by IP (returns a list of matching machines)
def filter_machines(ip: str, machine_list: list):
    return [m for m in machine_list if ip in m.ip]

# Example usage:
# Adding a person and machine
add_person(faker.name(), list_of_names)
add_machine(faker.ipv4_private(), machines)

# Removing a person and machine
remove_person(list_of_names[0].name, list_of_names)  # Remove first person
remove_machine(machines[0].ip, machines)  # Remove first machine

# Filtering by name and IP
filtered_persons = filter_persons("John", list_of_names)
filtered_machines = filter_machines("192.168", machines)

print("Filtered persons by 'John':")
pprint(filtered_persons)

print("Filtered machines by '192.168':")
pprint(filtered_machines)
