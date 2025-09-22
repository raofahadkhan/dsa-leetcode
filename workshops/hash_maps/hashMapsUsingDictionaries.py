# IMPLEMENTATION OF HASH_MAPS USING DICTIONARY

class PhoneBook:
    def __init__(self):
        self.phone_book = {}
        
    def add_contact(self, contact_name, contact_number):
        self.phone_book[contact_name] = contact_number
        
    def get_contact(self, contact_name):
        
        # 1st Approach
        # return self.phone_book[contact_name] if contact_name in self.phone_book else "Contact Number Not Found"
    
        # 2nd Approach
        return self.phone_book.get(contact_name, "Contact Number Not Found")
    
    def __repr__(self):
    # Provide a readable representation of the object
        return f"PhoneBook({self.phone_book})"
    
contact_list = PhoneBook()
contact_list.add_contact("fahad", "+92312-0000000")
print(contact_list)

contact_list.add_contact("ali", "+92312-0000000")
print(contact_list)

ali_contact_number = contact_list.get_contact("ali")
print("Ali's Contact Number: " + ali_contact_number)

fahad_contact_number = contact_list.get_contact('fahad')
print("Fahad's Contact Number: " + fahad_contact_number)

#  GETTING THE CONTACT NUMBER WHICH DOESN'T EXISTS IN CONTACT_LIST

hamza_contact_number = contact_list.get_contact('hamza')
print("Hamza's Contact Number: " + hamza_contact_number)
