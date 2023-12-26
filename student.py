import re

class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} is from {self.house}"

    #The house in this Class has comflicts
    #So after the "def house",we use self._house to replace self.house
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self,house):
        if house not in ["Room 1","Room 2","Room 3"]:
            raise ValueError("Invalid House")
        self._house = house
    
    #Just like the house,we code the defencive code of name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
    

def main():
    student = get_student()
    #student.house = "Room 4"#This sentence will cause ValueError
    #student.name = ""
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name,house)

if __name__ == "__main__":
    main()