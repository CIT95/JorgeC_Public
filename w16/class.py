
"""
Utilizing  OOP with inheritance.
May/5/21. Viva Cinco de Mayo!!!
"""



class Student: #Parent class (super) or BASE class
    def __init__(self, fullname, id, address, phone):
        self.fullname = fullname
        self.id = id
        self.address = address
        self.phone = phone

    def studentName(self):
        print(f'I am {self.fullname} and my student ID is {self.id} ')

    def studentAddress(self):
        print(f'His address is: {self.address}. Phone: {self.phone} ')


class Classes(Student): #inherite from the class STUDENT or DERIVED class
    def __init__(self, fullname, id, address, phone, classe, classnumber): 
        super().__init__(fullname, id, address, phone) #this will call the main class we inherite it from in this case PET. Parent class
        self.classe = classe
        self.classnumber = classnumber

    def showmyclass(self):
        print(f'I am {self.fullname} and my student ID is {self.id} taking {self.classe}')


class Club(Student): #inherite from the class STUDENT or DERIVED class
    def __init__(self, fullname, id, address, phone, hobbyname): 
        super().__init__(fullname, id, address, phone) #this will call the main class we inherite it from in this case PET. Parent class
        self.hobbyname = hobbyname        

    def passtime(self):
        print('My hobbies')

    def showHobby(self):
        print(f'I am {self.fullname} and my student ID is {self.id} and my Hobby is: {self.hobbyname}')



st1 = Student('Jorge Cortes', 101, '123 E Olive Ave Fresno, CA 93711','559-123-4567')
st1.studentName()
st1.studentAddress()

print('\n') #The classes object has access to al lthe functions including the PARENT class
st2 = Classes('Mike Cortes', 102, '123 E Olive Ave Fresno, CA 93711','559-123-4567', 'History 101','356-125') #no need to create the student info again, just call STUDENT class
st2.studentName() #also access to the PARENT class functions
st2.studentAddress() #also access to the PARENT class functions
st2.showmyclass()

print('\n')
st3 = Club('Jorge Cortes', 101, '123 E Olive Ave Fresno, CA 93711','559-123-4567','Bonsai') #no need to create the student info again, just call STUDENT class
st3.passtime()
st3.showHobby()
st3.studentName()   #also access to the PARENT class functions
st3.studentAddress() #also access to the PARENT class functions

