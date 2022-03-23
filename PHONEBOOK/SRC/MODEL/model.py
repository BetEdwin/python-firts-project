print("PHONEBOOK")


class Contact:

    name = ""
    lastname = ""
    nickname = ""
    number = ""
    email = ""
    birthday = ""

    def __init__(self, name, lastname, nickname, number, email, birthday):
        self.name = name
        self.lastname = lastname
        self.nickname = nickname
        self.number = number
        self.email = email
        self.birthday = birthday

    def contact_name(self):
        return self.name

    def contact_lastname(self):
        return self.lastname

    def contact_nickname(self):
        return self.nickname

    def contact_number(self):
        return self.number

    def contact_email(self):
        return self.email

    def contacto_birthday(self):
        return self.birthday

    def export(self):
        return {"name": self.name, "lastname": self.lastname,
                "nickname": self.lastname, "number": self.number,
                "email": self.email, "birthday": self.birthday}