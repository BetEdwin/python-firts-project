from MODEL.model import Contact


class View:

 def print_options(self):
            print('CONTACT BOOK')
            print('*' * 50)
            print('Select an Option:')
            print('1. create contact')
            print('2. list contacts')
            print('3. modify contact')
            print('4. delate contact')
            print('5. search contact')
            print('6. output')
            return int(input("Select an option you want    "))

    def contact_data(self):
        name = str(input("Enter the name"))
        lastname = str(input("Enter the lastname"))
        nickname = str(input("Entrer the lastname"))
        number = int(input("Enter the number"))
        email = str(input("Enter the number, include @"))
        birthday = str(input("Enter the date of birth"))
        return Contact(name, lastname, nickname, number, email, birthday)

    def create_contac(self):
        print("Contact created")

    def correct_action(self):
        print("Action performed successfully")

    def wrong_action(self):
        print("Action not performed")

    def search_contacto(self):
        return str(input("Enter the name of the contact you want to obtain...  "))

    def print_result(self, contacts):
        for contact in contacts:
            print(contact.exportar())
        self.wait()

    def wait(self):
        input("Enter to continue")


    def output_program(self):
        print("End, Thank you!")



