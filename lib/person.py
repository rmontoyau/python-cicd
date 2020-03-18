class Person:
    def __init__(self):
        self._name = None
        self._last_name = None
        self._id = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    def __str__(self):
        return f"name= {self._name},\
         last name= {self._last_name},\
         id= {self._id}"
