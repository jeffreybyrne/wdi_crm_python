from contact import Contact


class CRM:

    def main_menu(self):
        """This method initializes our program, making sure that the user can
        choose an action and then do another one after that action is complete.
        """
        while True:
            self.print_main_menu()
            selection = int(input())
            self.call_option(selection)

    def print_main_menu(self):
        """This method prints out the main menu for the user
        """
        print('[1] Add a new contact')
        print('[2] Modify an existing contact')
        print('[3] Delete a contact')
        print('[4] Display all the contacts')
        print('[5] Search by attribute')
        print('[6] Exit')
        print('Enter a number: ')

    def call_option(self, input_number):
        """This method takes in a numeric input from the user and calls the
        corresponding method as per the listed options from the menu.
        """
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
        """This method prompts the user for input and creates a new contact
        based off of their input.
        """
        print("What is the first name of the new contact?")
        new_first_name = input()
        print("What is the last name of the new contact?")
        new_last_name = input()
        print("What is the email address of the new contact?")
        new_email = input()
        print("Enter a note for this contact:")
        new_note = input()
        Contact.create(first_name=new_first_name, last_name=new_last_name, email=new_email, note=new_note)
        # new_contact = Contact.create(new_first_name, new_last_name, new_email, new_note)

    def modify_existing_contact(self):
        """This method prompts the user to enter a contact number to update
        then asks which field they want to modify, what they want to change it
        to, and then makes that change.
        """
        print("Which contact do you want to modify?")
        search_id = int(input())
        print("What field do you wish to change?")
        print("[1] First Name")
        print("[2] Last Name")
        print("[3] Email Address")
        print("[4] Notes")
        field_change = int(input())
        print("What value do you want to change it to?")
        updated_value = input()
        contact_to_update = Contact.get(id=search_id)
        if field_change == 1:
            contact_to_update.first_name = updated_value
            contact_to_update.save()
        elif field_change == 2:
            contact_to_update.last_name = updated_value
            contact_to_update.save()
        elif field_change == 3:
            contact_to_update.email = updated_value
            contact_to_update.save()
        elif field_change == 4:
            contact_to_update.note = updated_value
            contact_to_update.save()
        print("This contact has been updated:")

    def delete_contact(self):
        """This method asks the user which contact they want to delete, and
        then deletes it.
        """
        print("Which contact do you want to delete?")
        delete_contact = int(input())
        curr_contact = Contact.get(id=delete_contact)
        curr_contact.delete()
        print("This contact has been deleted.")

    def display_all_contacts(self):
        """This method lists all contacts.
        """
        Contact.all()

    def search_by_attribute(self):
        """This method asks the user which field they wish to search by, then
        asks which value they want to search by, and then does a search for the
        first contact that matches their query.
        """
        print("What attribute would you like to search by?")
        print("[1] First Name")
        print("[2] Last Name")
        print("[3] Email Address")
        print("[4] Notes")
        search_field = int(input())
        print("What value would you like to search by?")
        search_value = input()
        if search_field == 1:
            result = Contact.get(first_name=search_value)
        elif search_field == 2:
            result = Contact.get(last_name=search_value)
        elif search_field == 3:
            result = Contact.find_by(email=search_value)
        elif search_field == 4:
            result = Contact.find_by(note=search_value)
        if result is not False:
            print("The following contact matches your search criteria:")
            print(result)
        else:
            print("There are no contacts that match your query.")


a_crm_app = CRM()
a_crm_app.main_menu()
