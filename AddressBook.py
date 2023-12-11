import re
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        self.name = value

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not re.fullmatch(r'\d{10}', value):
            raise ValueError("Invalid phone number. Must be 10 digits.")

class Record:
    def __init__(self,name):
        self.name = Name(name)
        self.phones = []  
    
    def add_phone(self,phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        phone_to_edit = self.find_phone(old_phone)
        if phone_to_edit:
            phone_to_edit.value = new_phone

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
   
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        """Creates empty address book"""
        self.data = {}
    
    def add_record(self,some_record):
        self.data [some_record.name.value] = some_record.phones
    
    def delete(self, key):
        del self.data[key]
    
    def find(self, name_key):
        return self.data.get(name_key)


book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for record_name, record in book.data.items():
    print(record)

john = book.find("John")
if john_record:
    john_record.edit_phone("1234567890", "1112223333")
    print(john_record)

found_phone = john_record.find_phone("5555555555") if john_record else None
if found_phone:
    print(f"{john_record.name}: {found_phone}")
else:
    print(found_phone)

book.delete("Jane")


