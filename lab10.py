# -------------------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 4: Advising System
# Last Modified: October 31, 2017
# -------------------------------------------------
# This is to check on Student status and to update Studeny to resources
# that is for there Major.
# -------------------------------------------------

## This Class holds Generic info to be tested and printed
class Generic_Major:
    def __init__(self, firstName, lastName):
        self.firstName = firstName.title()
        self.lastName = lastName.title()        
        self.major = "Generic"
        self.major_troubles = False
        self.math_troubles = False

    def get_first_name(self):
        return self.firstName

    def get_last_name(self):
        return self.lastName

    def get_major(self):\
        return self.major

    def get_major_troubles(self):
        return self.major_troubles

    def get_math_troubles(self):
        return self.math_troubles

    def major_advising(self):
        if self.major_troubles:
            print("because you are having troubles with your major:")
            print("--> visit your professor during office hours")
            print("--> visit your academic advisor")
        
    def math_advising(self):
        if self.math_troubles:
            print("because you are having troubles with math:")
            print("--> visit the Math Learning Center in Wilson 1-112")

    def set_major_troubles(self, x):
        self.major_troubles = x

    def set_math_troubles(self, x):
        self.math_troubles  = x
        
        
## This is all the Sub-Class to test and print for selected Majors    
class CLS_Major(Generic_Major):
    def __init__(self, firstName, lastName):
        Generic_Major.__init__(self, firstName, lastName)
        self.major = "College of Letters and Sciences"       

class COE_Major(Generic_Major):
    def __init__(self, firstName, lastName):
        Generic_Major.__init__(self, firstName, lastName)
        self.major = "College of Engineering"
    def major_advising(self):
        if self.major_troubles:
            print("--> visit the EMPower Student Center in Roberts 313")
        Generic_Major.major_advising(self)
               
class Computer_Engineering_Major(Generic_Major):
    def __init__(self, firstName, lastName):
        Generic_Major.__init__(self, firstName, lastName)
        self.major = "Computer Engineering"
    def major_advising(self):
        if self.major_troubles:
            print("--> visit the EMPower Student Center in Roberts 313")
        Generic_Major.major_advising(self)

class Physics_Major(Generic_Major):
    def __init__(self, firstName, lastName):
        Generic_Major.__init__(self, firstName, lastName)
        self.major = "Physics"
    def major_advising(self):
        if self.major_troubles:
            print("--> visit the Physics Learning Center in Barnard Hall 230")
        Generic_Major.major_advising(self)

class Computer_Science_Major(Generic_Major):
    def __init__(self, firstName, lastName):
        Generic_Major.__init__(self, firstName, lastName)
        self.major = "Computer Science"
    def major_advising(self):

        if self.major_troubles:
            print("--> visit the CS Student Success Center in Barnard Hall 259")
            print("--> visit a CS professional advisor in Barnard Hall 357")
            print("--> visit the EMPower Student Center in Roberts 313")
        Generic_Major.major_advising(self)

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

