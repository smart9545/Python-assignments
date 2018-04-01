#############################################
#	COMPSCI 105 SS C, 2018              #
#	Assignment 1                        #
#                                           #
#	@author  	FanYu and fyu914    #
#	@version	19/1/2018           #
#############################################
"""
Description：
I'm going to implement a simple assessment marking management program.
Firstly,read a solution file, read a class list, read a series of student responses,
Secondly,compare the student responses with the solution for each assessment,
draw a histogram for each assessment and finally display the marking result for all students.
"""

from Student import Student
from Assessment import Assessment
from Histogram import Histogram
	
def read_classlist(inputFileName):
	#This function ...
    try:
        with open(inputFileName,'r') as f:
            content= f.read()
            content_list = content.split("\n")
            student_list = []
            for item in content_list:
                ilist = item.split(',')
                student = Student(ilist[0],ilist[1],ilist[2])
                student_list.append(student)
            return student_list
        
    except FileNotFoundError:
         print("File out.txt could not be opened")
		
	
def read_solution(inputFileName):
	#This function ...
    try:
        with open(inputFileName,'r') as f:
            content= f.read()
            content_list = content.split("\n")
            lab_list=[]
            for item in content_list:
                result_list = item.split(':')
                solution = Assessment(result_list[0],result_list[1])
                lab_list.append(solution)
            return lab_list
        
    except FileNotFoundError:
         print("File out.txt could not be opened")

def read_data(lab,class_list):
    h = Histogram(len(lab.get_anwerlist())+1,len(lab.get_anwerlist()))
    with open(str(lab.get_name())+".txt",'r') as f:
        content = f.read()
        content_list = content.split("\n")
        for line in content_list:
            id,data = line.split(":")
            mark = lab.calculate_marks(data)
            h.append_marks(mark)
            for s in class_list:
                if id == s.get_id():
                   s.append_marks(mark)
    return h
            

def display_separator():
    #This function prints out the separator
    lines = "-" * 40
    print(lines)


	
def main():  
 	#complete this
    class_list = read_classlist("classlist.txt")
    asst_list = read_solution("solution.txt")
    for asst in asst_list:
       display_separator()
       print(asst.get_name())
       my_histogram = read_data(asst, class_list)
       my_histogram.draw()
    for s in class_list:
       print(s)
    display_separator()
    
main()
