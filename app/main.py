class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_peoples = []

    for p in people:
        new_peoples = [Person(name=p.get("name"), age=p.get("age")) for p in people]

    for person_data in people:
        current_person = Person.people[person_data.get("name")]

        if person_data.get("wife") is not None:
            current_person.wife = Person.people[person_data.get("wife")]

        if person_data.get("husband") is not None:
            current_person.husband = Person.people[person_data.get("husband")]

    return new_peoples
