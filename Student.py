#############################################
#	COMPSCI 105 SS C, 2018              #
#	Assignment 1                        #
#                                           #
#	@author  	FanYu and fyu914    #
#	@version	19/1/2018           #
#############################################
"""
Description：
Design a class named Student to represent a student record. The Student class contains the following:
·Four private data fields named name，id，email，marks
·Create accessor and mutator methods for all data fields
·Create __str__ method return nicely formatted string representation of students
"""

class Student:
    def __init__(self,name,id,email):
        self.__name = name
        self.__id = id
        self.__email = email
        self.__marks = []
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_email(self):
        return self.__email
    def get_marks(self):
        return self.__marks
    def __str__(self):
        return str(self.__id)+":"+' {name}, {email}, marks: {marks}'.format(name = self.__name,email = self.__email,marks = self.__marks)
    def append_marks(self,value):
        self.__marks.append(value)
        return self.__marks
