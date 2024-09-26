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

# PersonManager to manage list of Person objects
class PersonManager:
    def __init__(self):
        self.person_list = []

    # Method to add a person
    def add_person(self, name: str):
        new_person = Person(name=name)
        self.person_list.append(new_person)
        print(f"Added person: {new_person}")

    # Method to remove a person by name
    def remove_person(self, name: str):
        self.person_list = [p for p in self.person_list if p.name != name]
        print(f"Removed person with name: {name}")

    # Method to filter people by name
    def filter_persons(self, name: str):
        return [p for p in self.person_list if name.lower() in p.name.lower()]

    # Method to display all persons
    def display_persons(self):
        pprint(self.person_list)


# MachineManager to manage list of Machine objects
class MachineManager:
    def __init__(self):
        self.machine_list = []

    # Method to add a machine
    def add_machine(self, ip: str):
        new_machine = Machine(ip=ip)
        self.machine_list.append(new_machine)
        print(f"Added machine: {new_machine}")

    # Method to remove a machine by IP
    def remove_machine(self, ip: str):
        self.machine_list = [m for m in self.machine_list if m.ip != ip]
        print(f"Removed machine with IP: {ip}")

    # Method to filter machines by IP
    def filter_machines(self, ip: str):
        return [m for m in self.machine_list if ip in m.ip]

    # Method to display all machines
    def display_machines(self):
        pprint(self.machine_list)


# Example usage:

# Create instances of PersonManager and MachineManager
person_manager = PersonManager()
machine_manager = MachineManager()

# Add 20 people and 5 machines
for _ in range(20):
    person_manager.add_person(faker.name())

for _ in range(5):
    machine_manager.add_machine(faker.ipv4_private())

# Display the lists of people and machines
print("List of persons:")
person_manager.display_persons()

print("List of machines:")
machine_manager.display_machines()

# Remove the first person and machine
if person_manager.person_list:
    person_manager.remove_person(person_manager.person_list[0].name)

if machine_manager.machine_list:
    machine_manager.remove_machine(machine_manager.machine_list[0].ip)

# Display lists again after removal
print("After removal:")
person_manager.display_persons()
machine_manager.display_machines()

# Filter people by name and machines by IP
filtered_persons = person_manager.filter_persons("John")
filtered_machines = machine_manager.filter_machines("192.168")

print("Filtered persons by 'John':")
pprint(filtered_persons)

print("Filtered machines by '192.168':")
pprint(filtered_machines)
