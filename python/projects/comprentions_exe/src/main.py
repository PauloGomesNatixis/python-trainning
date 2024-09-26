from asyncio.format_helpers import _format_callback_source
from dataclasses import dataclass
from pprint import pprint
from faker import Faker
from faker.providers import internet

faker = Faker()
faker.add_provider(internet)

@dataclass(eq=True)
class Person:
    name: str

@dataclass
class Machine:
    ip: str

list_of_names = [
    Person(name=faker.name())
    for _ in range(20)
]

list_of_names = [ Person(name=faker.name())
    for _ in range(20)
]
pprint(list_of_names)

machines = [
    Machine(ip=faker.ipv4_private())
    for _ in range(5)
]
pprint(machines)




