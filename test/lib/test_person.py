from lib.person import Person


def test_new_person():
    person = Person()
    person.name = "Rudy"
    person.last_name = "Montoya"
    person.id = 1
    assert str(person) == "name= Rudy, last name= Montoya, id= 1"
