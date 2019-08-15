
# File: exam-05.py
# Project: ps6
# File Created: Tuesday, 6th August 2019 2:09:07 pm
# Author: C.V (vinegoni@yahoo.com)
# -----
# Last Modified: Tuesday, 6th August 2019 2:09:07 pm
# Modified By: C.V (vinegoni@yahoo.com)
# -----
# Copyright 2019 - C.V
###
### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'


class Campus(object):

    def __init__(self, center_loc):
        self.center_loc = center_loc

    def __str__(self):
        return str(self.center_loc)


class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    list_locations = []

    def __init__(self, center_loc, tent_loc=Location(0, 0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        # Your code here
        Campus.__init__(self, center_loc)
        self.list_locations.append(tent_loc)

    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        for location in self.list_locations:
            if location.dist_from(new_tent_loc) < 0.5:
                return False
        self.list_locations.append(new_tent_loc)
        return True

    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        # Your code here
        try:
            self.list_locations.remove(tent_loc)
        except:
            print('Exception')

    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        # Your code here
        list_x = []
        indices = []
        for location in self.list_locations:
            list_x.append(location.getX())
        indices = sorted(range(len(list_x)), key=lambda k: list_x[k])
        for k in indices:
            print(self.list_locations[k])


c = MITCampus(Location(1, 2))
c.add_tent(Location(2, 3))
c.add_tent(Location(1, 2))
c.add_tent(Location(0, 0))
c.add_tent(Location(2, 3))
c.get_tents()
