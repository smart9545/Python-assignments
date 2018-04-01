#############################################
#	COMPSCI 105 SS C, 2018              #
#	Assignment 2                        #
#                                           #
#	@author  	FanYu and fyu914    #
#	@version	10/2/2018           #
#############################################
"""
Description：
Implement the functionality for the read_sentence() recursive
function without using loops. This function  take a list of words as its input
to represent a sentence. It will also take an integer to determine how long a
word must be before its definition must be looked up. The function  print the
sentence, ensuring no words longer than the integer are printed. Instead their
definitions would be printed.
The function get_definition() will take a word as its input and return a list
of words representing the dictionary definition of the passed in word.
"""
def read_sentence(sentence, max_letters):
    ##You need to implement this recursive function
    if sentence==None:
        return None 
    if len(sentence)>=1:
        if len(sentence[0])> max_letters:
            read_sentence(get_definition(sentence[0]),max_letters)
        else:
            print(sentence[0],end=" ")
        read_sentence(sentence[1:],max_letters)

##This function will return a list of words to represent
##the definition of the word.
##This function will be implemented for you and you may
##assume that the definition of the word will be returned if necessary
##
##Feel free to follow the example below to add your own words and their
##definitions for testing purposes!
def get_definition(word):
    if word == 'sentence':
        return ['set', 'of', 'words']
    if word == 'difficult':
        return ['not', 'easy']
    if word == 'extraordinary':
        return ['better', 'than', 'ordinary']
    if word == 'ordinary':
        return ['normal']
    if word == 'discover':
        return ['come', 'by']
    if word == 'mitochondria':
        return ['cells', 'in', 'cytoplasm','that','convert','energy']
    if word == 'cytoplasm':
        return ['gel', 'outside', 'a','nucleus']
    if word == 'powerhouse':
        return ['main', 'source', 'of','power']

print()
##should print: better than normal people are not easy to come by
read_sentence(['extraordinary', 'people', 'are', 'difficult', 'to', 'discover'], 7)
print()
##should print: better than ordinary people are not easy to discover 
read_sentence(['extraordinary', 'people', 'are', 'difficult', 'to', 'discover'], 8)
print()
##should print: cells in gell outside a nucleus that convert energy are the main source of power of the cell
read_sentence(['mitochondria', 'are', 'the', 'powerhouse', 'of', 'the', 'cell'], 7)
print()
##should print: mitochondria are the powerhouse of the call
read_sentence(['mitochondria', 'are', 'the', 'powerhouse', 'of', 'the', 'cell'], 20)


            
