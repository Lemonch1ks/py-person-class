from unittest import result


class Person:
    people = {}
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self




def create_person_list(people: list) -> list:
    new_peoples = []

    for pers in people:
        new_peoples.append(Person(name = pers.get("name"), age = pers.get("age")))

    for person in people:
        current_person = Person.people[person["name"]]

        if person.get("wife") is not None:
            current_person.wife = Person.people[person["wife"]]

        if person.get("husband") is not None:
            current_person.husband = Person.people[person["husband"]]



    return  new_peoples