from contact import Contact


class CRM:

    def main_menu(self):
        while True:
            self.print_main_menu()
            selection = int(input())
            self.call_option(selection)

    def print_main_menu(self):
        print('[1] Add a new contact')
        print('[2] Modify an existing contact')
        print('[3] Delete a contact')
        print('[4] Display all the contacts')
        print('[5] Search by attribute')
        print('[6] Exit')
        print('Enter a number: ')

    def call_option(self, input_number):
        if input_number == 1:
            self.add_new_contact()
        elif input_number == 2:
            self.modify_existing_contact()
        elif input_number == 3:
            self.delete_contact()
        elif input_number == 4:
            self.display_all_contacts()
        elif input_number == 5:
            self.search_by_attribute()
        elif input_number == 6:
            quit()

    def add_new_contact(self):
        print("What is the first name of the new contact?")
        new_first_name = input()
        print("What is the last name of the new contact?")
        new_last_name = input()
        print("What is the email address of the new contact?")
        new_email = input()
        print("Enter a note for this contact:")
        new_note = input()
        Contact.create(new_first_name, new_last_name, new_email, new_note)

    def modify_existing_contact(self):
        print("Which contact do you want to modify?")
        search_id = int(input())
        print("What field do you wish to change?")
        field_change = input()
        while field_change not in ['first_name', 'last_name', 'email', 'note']:
            print("Please enter a valid field to change.")
            field_change = input()
        print("What value do you want to change it to?")
        updated_value = input()
        contact_to_update = Contact.find(search_id)
        contact_to_update.update(field_change, updated_value)
        print("This contact has been updated:")
        print(contact_to_update)

    def delete_contact(self):
        print("Which contact do you want to delete?")
        delete_contact = int(input())
        curr_contact = Contact.find(delete_contact)
        curr_contact.delete()
        print("This contact has been deleted.")

    def display_all_contacts(self):
        Contact.all()

    def search_by_attribute(self):
        print("What attribute would you like to search by?")
        search_field = input()
        while search_field not in ['first_name', 'last_name', 'email', 'note']:
            print("Please enter a valid field to change.")
            search_field = input()
        print("What value would you like to search by?")
        search_value = input()
        result = Contact.find_by(search_field, search_value)
        if result is not False:
            print("The following contact matches your search criteria:")
            print(result)


a_crm_app = CRM()
a_crm_app.main_menu()
