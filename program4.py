# -------------------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 4: Advising System
# Tyler Bourgeois
# Last Modified: 10/21/17
# -------------------------------------------------
# A brief overview of the program.
# -------------------------------------------------

#Defines Class Generic Major
class Generic_Major:

    #Initialize method
    def __init__(self, init_first_name, init_last_name):
        self.first_name = init_first_name.title()
        self.last_name = init_last_name.title()
        self.major = "Generic"
        self.math_troubles = False
        self.major_troubles = False

    #Methods to get or set part of an object
    def set_first_name(self, new_first_name):
        self.first_name = new_first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def get_last_name(self):
        return self.last_name

    def set_math_troubles(self, new_math_troubles):
        self.math_troubles = new_math_troubles

    def get_math_troubles(self):
        return self.math_troubles

    def set_major_troubles(self, new_major_troubles):
        self.major_troubles = new_major_troubles

    def get_major_troubles(self):
        return self.major_troubles

    def get_major(self):
        return self.major

    #major advising and math advising functions to decide if the student needs
    #either and returns their options if they need help
    def major_advising(self):
        if(self.major_troubles):
            print("because you are having troubles with your major:\n--> visit your professor during office hours\n--> visit your acadmeic advisor")

    def math_advising(self):
        if(self.math_troubles):
            print("because you are having troubles with math:\n--> visit the Math Learning Center in Wilson 1-112")

#Defines CLS_Major as  subclass of Gneric_Major
class CLS_Major(Generic_Major):

    def __init__(self, init_first_name, init_last_name):
        Generic_Major.__init__(self, init_first_name, init_last_name)
        self.major = "College of Letters and Sciences"

#Defines COE_Major as  subclass of Gneric_Major
class COE_Major(Generic_Major):

    def __init__(self, init_first_name, init_last_name):
        Generic_Major.__init__(self, init_first_name, init_last_name)
        self.major = "College of Engineering"
    #Major advising specific to a COE major
    def major_advising(self):
        if(self.major_troubles):
            print("because you are having troubles with your major:\n--> visit the EMPower Student Center in Roberts 313\n--> visit your professor during office hours\n--> visit your academic advisor")

#Defines Computer_Engineering_Major as a subclass of COE_Major
class Computer_Engineering_Major(COE_Major):

    def __init__(self, init_first_name, init_last_name):
        COE_Major.__init__(self, init_first_name, init_last_name)
        self.major = "Computer Engineering"

#Defines Physics_Major as a subclass as CLS_Major
class Physics_Major(CLS_Major):

    def __init__(self, init_first_name, init_last_name):
        CLS_Major.__init__(self, init_first_name, init_last_name)
        self.major = "Physics"

    def major_advising(self):
        if(self.major_troubles):
            print("because you are having troubles with your major:\n--> visit the Physics Learning Center in Barnard Hall 230\n--> visit your professor during office hours\n--> visit your academic advisor")

#Defines Computer_Science_Major as a subclass of a COE_Major
class Computer_Science_Major(COE_Major):

    def __init__(self, init_first_name, init_last_name):
        COE_Major.__init__(self, init_first_name, init_last_name)
        self.major = "Computer Science"

    def major_advising(self):
        if(self.major_troubles):
            print("because you are having troubles with your major:\n--> visit the CS Student Success Center in Barnard Hall 259\n--> visit a CS professional advisor in Barnard Hall 357\n--> visit the EMPower Student Center in Roberts 313\n--> visit your professor during office hours\n--> visit your academic advisor")

# -------------------------------------------------
# Do not change anything below this line
# -------------------------------------------------

def advise(student):
    print("Student:", student.get_first_name(), student.get_last_name())
    print("Major: " + student.get_major() + ", Major Troubles: " +
          str(student.get_major_troubles()) + ", Math Troubles: " +
          str(student.get_math_troubles()))
    print()
    if not student.get_math_troubles() and not student.get_major_troubles():
        print("No advising is necessary.  Keep up the good work!")
    else:
        student.major_advising()
        student.math_advising()
    print("------------------------------")

# -------------------------------------------------

def process(student):
    advise(student)
    student.set_major_troubles(True)
    student.set_math_troubles(True)
    advise(student)

# -------------------------------------------------

def main():

    # Every student has a major, even if it is "undeclared"
    msu_student = Generic_Major("jalen", "nelson")
    process(msu_student)

    msu_student.set_math_troubles(False)
    advise(msu_student)

    msu_student.set_math_troubles(True)
    msu_student.set_major_troubles(False)
    advise(msu_student)

    # A CLS (College of Letters and Science) major is a subclass of a Generic major
    msu_student = CLS_Major("emma", "phillips")
    process(msu_student)

    # A COE (College of Engineering) major is a subclass of a Generic major
    msu_student = COE_Major("camden", "miller")
    process(msu_student)

    # A Computer Engineering major is a subclass of a COE major
    msu_student = Computer_Engineering_Major("gabriel", "smith")
    process(msu_student)

    # A Physics major is a subclass of a CLS major
    msu_student = Physics_Major("lena", "hamilton")
    process(msu_student)

    # A Computer Science major is a subclass of a COE major
    msu_student = Computer_Science_Major("halley", "jones")
    process(msu_student)

    msu_student.set_math_troubles(False)
    advise(msu_student)

    msu_student.set_math_troubles(True)
    msu_student.set_major_troubles(False)
    advise(msu_student)

# -------------------------------------------------

main()


