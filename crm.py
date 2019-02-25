from contact import Contact


class CRM:

    running = True

    def main_menu(self):
        while CRM.running:
            self.print_main_menu()
            selection = int(input())
            self.call_option(selection)

    def print_main_menu(self):
        print('Option 1')

# def call_option(self):
#
#
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
