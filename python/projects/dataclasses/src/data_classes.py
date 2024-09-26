
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Job:
    title: str
    salary: float

@dataclass
class Person:
    name: str
    age: int
    email: str
    job: Job | None 
    job2: Optional[Job] 
    
@dataclass
class Manager(Person):
    business_unit:  Optional[str] = None
    cod: Optional[int] = None
    
@dataclass
class Engineer(Person):
    area: str
    technology: List[str]
    
emploee = Person(name="foo",age=11,email="aaaaa@aaaaa.pt",job="Eng", job2="mana")
emploee.name = "Antonio"
print(emploee)

manager = Manager("Nelson",45,"neaaaa@ssss.pt","man","sysAdm","Manager",123)
print(manager)


eng = Engineer("aaa",23,"aaaaa@sddsdd.pt","ENG","","area",["linux","windows"])
print(eng)

# # Create a Job instance
# manager_job = Job(title="Manager", salary=100)
# dev_job = Job(title="Software Developer", salary=50)

# # Create a Person instance with a Job
# manager = Person(name="joão", job=manager_job)
# person = Person(name="Maria",job=dev_job)

# # Display the person and their job details
# print(manager)
# print(person)

# # Function to create and add a new Job
# def add_job(title: str, salary: float) -> Job:
#     return Job(title=title, salary=salary)

# # Function to create and add a new Person with a Job
# def add_person(name: str, job: Job) -> Person:
#     return Person(name=name, job=job)

# # Example usage
# new_job = add_job(title="Manager", salary=90000)
# new_job = add_job(title="Dev", salary=5000)
# new_job = add_job(title="Support", salary=4000)


# new_person = add_person(name="John Doe", job=new_job)
# new_person = add_person(name="Doe", job=new_job)
# new_person = add_person(name="Mat", job=new_job)

# # Display the created person with their job
# print(new_person)