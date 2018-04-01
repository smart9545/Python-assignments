#############################################
#	COMPSCI 105 SS C, 2018              #
#	Assignment 1                        #
#                                           #
#	@author  	FanYu and fyu914    #
#	@version	19/1/2018           #
#############################################
"""
Description：
Design a class named Assessment to represent an assessment record. The Assessment class contains the following:
·Two private data fields named name，answer_list
·Create accessor and mutator methods for all data fields
·Create __str__ method return nicely formatted string representation of assessment
·Create calculate_marks method which takes a string data as a parameter,compares the answer keys and returns total marks gained
"""

class Assessment:
    def __init__(self,name,answerlist):
        self.__name = name
        self.__answerlist = answerlist.split(",")
    def get_name(self):
        return self.__name
    def get_anwerlist(self):
        return self.__answerlist
    def __str__(self):
        return self._name +":"+" answer: "+'{}'.format(self.__answerlist)

    def calculate_marks(self,testlist):
        sum = 0
        test_list = testlist.split(",")
        if len(test_list) < len(self.__answerlist):
            return "Not enough answers"
        else:
            for index in range(len(self.__answerlist)):
                if self.__answerlist[index] == test_list[index]:
                    sum = sum + 1
            return sum
