#############################################
#	COMPSCI 105 SS C, 2018              #
#	Assignment 2                        #
#                                           #
#	@author  	FanYu and fyu914    #
#	@version	10/2/2018           #
#############################################
"""
Description：
Define a function called hashing() which simulates a list of keys
being inserted, in the order given, into the hashtable. The function should
return a representation of the hashtable as a list - where the keys are shown in
their positions and the value None is used to represent unused positions.
"""

##This function should return a list representing a hashtable filled
##with the input keys using the input probing method
def hashing(list_of_keys, size, probing, q):
    new_list=[None]*size
    if probing == 'linear':
       for key in list_of_keys:
           index = key%len(new_list)
           find = False
           while not find:
               if new_list[index]==None:
                   new_list[index]= key
                   find = True
               else:
                   index = (index+1)%len(new_list)
       return new_list
                    
    elif probing == 'quadratic':
        for key in list_of_keys:
            found = False
            original_index = key% len(new_list)
            index=original_index
            j = 0
            while not found:
                if new_list[index]== None:
                    new_list[index]= key
                    found = True
                else:
                    j+=1
                    index =int((original_index +j*j )%len(new_list))
        return new_list
    elif probing == 'double':
        for key in list_of_keys:
              found = False
              index = key%len(new_list)
              while not found:
                    if new_list[index]==None:
                        new_list[index]=key
                        found =True
                    else:
                        step_value = q - key%q
                        if (index+ step_value)%len(new_list) !=0:
                            index =(index+ step_value)%len(new_list)
        return  new_list


            
            

