from MODEL.model import Contact
import CONTAC
from VIEW.view import View


class Controller:

    def __init__(self):
        self.option_select = 0
        self.name_contact = ""
        self.view = View()
        self.contacts = []

    def options_select_s(self):
        while self.option_select != 8:
            self.option_select = self.view.print_options()

            if self.option_select == 1:
                self.create_contacts()

            if self.option_select == 2:
                self.export_contacts()

            if self.option_select == 3:
                self.list_contacts()

            if self.option_select == 4:
                self.charge_contacts()

            if self.option_select == 5:
                self.search_contacts()

            if self.option_select == 6:
                self.add_phone()

            if self.option_select == 7:
                self.output_program()

    def create_contacts(self):
        new_contacts = self.view.contact_data()
        self.contacts.append(new_contacts)
        self.view.create_contac()

    def export_contacts(self):
        name_directory = self.view.new_directory_n()
        list_export = []
        for new_contacts in self.contacts:
            list_export.append(new_contacts.export())

        with open(f"datos/{name_directory}.json", "w") as fp:
            json.dump(list_export, fp)

        self.view.correct_action()

    def list_contacts(self):
        for new_contacts in self.contacts:
            print(new_contacts.export())

    def charge_contacts(self):
        try:
            with open("datos/CONTACTS.json", "r") as fp:
                datas = contac.load(fp)

            for new_contacts in datas:
                self.contacts.append(
                    Contact(
                        name=new_contacts["name"],
                        lastname=new_contacts["lastname"],
                        nickname=new_contacts["nickname"],
                        number=new_contacts["number"],
                        email=new_contacts["email"],
                        birthday=new_contacts["birthay"]
                    )
                )

        except Exception as e:
            self.view.correct_action(e)

    def search_contacts(self):
        results = []
        contact_name = self.view.search_contacto()
        for contact in self.contacts:
            if contact_name == contact_name:
                results.append(contact)
                break
        self.view.print_result(results)

    def add_phone(self):
        pass


    def output_program(self):
        self.view.output_program()
