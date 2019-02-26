from peewee import SqliteDatabase, Model, CharField, TextField

db = SqliteDatabase('crm.db')


class Contact(Model):
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    note = TextField()

    class Meta:
        database = db

    def full_name(self):
        """Returns the full (first and last) name of the contact"""
        return self.first_name + ' ' + self.last_name


# contact1 = Contact.create('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')
# contact2 = Contact.create('Bit', 'Bot', 'bitbot@bitmakerlabs.com', 'beep boop')
#
# print(len(Contact.contacts))
# print(contact1.id)
# print(contact2.id)
# print(Contact.find(1))
# print(Contact.find(2))
# print(Contact.find(3))
# print(contact1.update('first_name', 'Jeff'))
# print(contact2.update('flirst_name', 'Jeff'))
# print(Contact.all())
# print(Contact.all())
# print(Contact.find_by('first_name', 'Betty'))
# print(Contact.find_by('first_name', 'Betty2'))
db.connect()
db.create_tables([Contact])
