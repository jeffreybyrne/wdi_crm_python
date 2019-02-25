class Contact:

    contacts = []
    next_id = 1

    def __init__(self, new_f_name, new_l_name, new_email, new_note):
        """This method should initialize the contact's attributes"""
        self.first_name = new_f_name
        self.last_name = new_l_name
        self.email = new_email
        self.note = new_note
        self.id = Contact.next_id
        Contact.next_id += 1

    @classmethod
    def create(cls, new_f_name, new_l_name, new_email, new_note):
        """This method should call the initializer,
        store the newly created contact, and then return it
        """
        new_contact = Contact(new_f_name, new_l_name, new_email, new_note)
        Contact.contacts.append(new_contact)
        return new_contact

    @classmethod
    def all(cls):
        """This method should return all of the existing contacts"""

    @classmethod
    def find(cls, input_id):
        """ This method should accept an id as an argument
        and return the contact who has that id
        """
        for num in range(0, len(Contact.contacts)):
            if Contact.contacts[num].id == input_id:
                return Contact.contacts[num]
        return False

    def update(self, update_field, update_value):
        """ This method should allow you to specify
        1. which of the contact's attributes you want to update
        2. the new value for that attribute
        and then make the appropriate change to the contact
        """
        if update_field not in ['first_name', 'last_name', 'email', 'note']:
            return False
        else:
            self.update_field = update_value
            return True

    @classmethod
    def find_by(cls):
        """This method should work similarly to the find method above but it
        should allow you to search for a contact using attributes other than id
        by specifying both the name of the attribute and the value. eg.
        searching for 'first_name', 'Betty' should return the first contact
        named Betty
        """

    @classmethod
    def delete_all(cls):
        """This method should delete all of the contacts"""

    def full_name(self):
        """Returns the full (first and last) name of the contact"""

    def delete(self):
        """This method should delete the contact
        HINT: Check the Array class docs for built-in methods that might be
        useful here
        """

    # Feel free to add other methods here, if you need them.
contact1 = Contact.create('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')
contact2 = Contact.create('Bit', 'Bot', 'bitbot@bitmakerlabs.com', 'beep boop')

print(len(Contact.contacts))
print(contact1.id)
print(contact2.id)
print(Contact.find(1))
print(Contact.find(2))
print(Contact.find(3))
print(contact1.update('first_name', 'Jeff'))
print(contact2.update('flirst_name', 'Jeff'))
