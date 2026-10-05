class User:

    def __init__(self, id, name, username, email):
        self._id = id
        self._name = name
        self._username = username
        self._email = email

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @classmethod
    def from_json(cls, data):
        return cls(
            id=data["id"],
            name=data["name"],
            username=data["username"],
            email=data["email"]
        )