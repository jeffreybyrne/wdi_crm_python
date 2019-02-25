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
            print("What is the first name of the new contact?")
            new_first_name = input()
            print("What is the last name of the new contact?")
            new_last_name = input()
            print("What is the email address of the new contact?")
            new_email = input()
            print("Enter a note for this contact:")
            new_note = input()
            Contact.create(new_first_name, new_last_name, new_email, new_note)
        elif input_number == 2:
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
        elif input_number == 3:
            # delete a contact
            pass
        elif input_number == 4:
            # display_all_contacts
            Contact.all()
        elif input_number == 5:
            # search by attribute
            pass
        elif input_number == 6:
            quit()


# def add_new_contact(self):
#
#
# def modify_existing_contact(self):
#
#
# def delete_contact(self):
#
#
# def display_all_contacts(self):
#
# def search_by_attribute(self):


thing = CRM()
thing.main_menu()
