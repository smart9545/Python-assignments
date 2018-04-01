#############################################
#	COMPSCI 105 SS C, 2018              #
#	Assignment 1                        #
#                                           #
#	@author  	FanYu and fyu914    #
#	@version	19/1/2018           #
#############################################
"""
Description：
Design a class named Histogram to represent a histogram record. The Histogram class contains the following:
·Three private data fields named range, max_mark, occurrence_list
·Create accessor and mutator methods for all data fields
·Create __str__ method return nicely formatted string representation of Histogram object
·Create a public methor append_marks to update the occurence list of marks
"""




class Histogram:
    def __init__(self,number,max ):
        self.__range = number
        self.__max = max
        self.__occurrencelist = [0]*number
    def get_max_mark(self):
        return self.__max
    def get_range(self):
        return self.__range
    def get_occurrence_list(self):
        return self.__occurrencelist
    def append_marks (self,number):
        if number <= self.__max :
            self.__occurrencelist[number] += 1
        return self.__occurrencelist
    def draw(self):
        for key in range(self.__range):
            print (key,":","*"* self.__occurrencelist[key],sep="")
    def __str__(self):
        return "max_mark"+":"+' {maxmarks}, occurrence: {occurrencelist}'.format(maxmarks = self.__max,occurrencelist =self.__occurrencelist)

