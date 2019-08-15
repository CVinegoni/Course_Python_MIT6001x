
# File: usresidents.py
# Project: ps6
# File Created: Tuesday, 6th August 2019 11:36:26 am
# Author: C.V (vinegoni@yahoo.com)
# -----
# Last Modified: Tuesday, 6th August 2019 11:36:26 am
# Modified By: C.V (vinegoni@yahoo.com)
# -----
# Copyright 2019 - C.V
###
## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##


class Person(object):
    def __init__(self, name):
        # create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None

    def getLastName(self):
        # return self's last name
        return self.lastName

    def setAge(self, age):
        # assumes age is an int greater than 0
        # sets self's age to age (in years)
        self.age = age

    def getAge(self):
        # assumes that self's age has been set
        # returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age

    def __lt__(self, other):
        # return True if self's name is lexicographically less
        # than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        # return self's name
        return self.name


class USResident(Person):
    """ 
    A Person who resides in the US.
    """

    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        # Write your code here
        Person.__init__(self, name)
        list_status = ['citizen', 'legal_resident', 'illegal_resident']
        try:
            if status in list_status:
                self.status = status
            else:
                self.status = None
                raise ValueError('Value error raised')
        except ValueError as ve:
            print(ve)

    def getStatus(self):
        """
        Returns the status
        """
        return self.status


a = USResident('Tim Beaver', 'citizen')
print(a.getStatus())
b = USResident('Tim Horton', 'legal_resident')
print(b.getStatus())
