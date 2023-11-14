class Contact:
    all_contacts = []
    def __init__(self, name, lastname, phone_number):
        self.name = name
        self.lastname = lastname
        self.phone_number = phone_number
        Contact.all_contacts.append(self)

    def print_contact(self):
        print("Contact Details:")
        print(f"Name: {self.name} {self.lastname}")
        print(f"Phone Number: {self.phone_number}")


class Friend(Contact):
    def play_football_with_me(self):
        print(f"{self.name} {self.lastname} invites you to play football!")


class ContactList(list):
    def search_by_name(self, name):
        matching_contacts = []
        for contact in self:
            if contact.name == name:
                matching_contacts.append(contact)
        return matching_contacts


all_contacts = ContactList()
c1 = Contact("Aichu", "Sultanalieva", "996709497796")
c2 = Contact("Begi", "Makusutova", "996709497796")
c3 = Contact("Kuka", "Askarbekova", "996709497796")

search_results = all_contacts.search_by_name("Aichu")
for contact in search_results:
    contact.print_contact()