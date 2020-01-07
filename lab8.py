# -----------------------------------------------------
# CSCI 127, Lab 8
# October 19, 2017
# Tyler Bourgeois
# -----------------------------------------------------

class Contact:

    def __init__(self, init_first_name, init_last_name, init_cell_number):
        self.first_name = init_first_name
        self.last_name = init_last_name
        self.cell_number = init_cell_number
        self.title = ""

    def __str__(self):
        if len(self.title)>0 : self.title = self.title + " "
        space = len(self.title + self.first_name + " " + self.last_name)
        return self.title + self.first_name + " " + self.last_name + (self.cell_number).rjust((37-space))      

    def set_title(self, new_title):
        self.title = new_title

    def get_title(self):
        return self.title

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def get_last_name(self):
        return self.last_name

    def set_cell_number(self, new_cell_number):
        self.cell_number = new_cell_number

    def get_cell_number(self):
        return self.cell_number

    def get_area_code(self):
        numberlist = self.cell_number.split("-")
        return numberlist[0]

# -----------------------------------------------------
# Do not change anything below this line
# -----------------------------------------------------

def print_directory(contacts):
    print("My Contacts")
    print("-----------")
    for person in contacts:
        print(person)
    print("-----------\n")

# -----------------------------------------------------

def main():
    champ = Contact("???", "Bobcat", "406-994-0000")
    president = Contact("Waded", "Cruzado", "406-994-CATS")
    professor = Contact("John", "Paxton", "406-994-4780")

    contacts = [champ, president, professor]

    print_directory(contacts)

    champ.set_first_name("Champ")
    president.set_title("President")
    professor.set_title("Professor")

    print_directory(contacts)

    print("The area code for cell number", champ.get_cell_number(), "is", \
           champ.get_area_code())

# -----------------------------------------------------

main()
