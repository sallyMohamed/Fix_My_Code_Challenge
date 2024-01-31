#!/usr/bin/python3
"""
User class
"""

class User:
    """ User class represents a user """

    def __init__(self):
        """ Initializes a new User instance """
        self.__email = None

        @property
        def email(self):
            """ Getter method for the email attribute """
            return self.__email

        @email.setter
        def email(self, value):
            """ Setter method for the email attribute """
            if not isinstance(value, str):
                raise TypeError("email must be a string")
            self.__email = value
