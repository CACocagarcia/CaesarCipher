#!/usr/bin/env python3

# input statements for the values
text = str(input('Input text: '))
key = int(input('Enter a number between 1-26: ')) #decided to go with 26 because 26 is the standar amount units that each character in a group can be displaced

def encrypt(text,key): 
    result = "" 

    # LOOP TO TRANSFORM THE TEXT
    # This loop first grabs the string that is inputed by the user
    # then it grabs each indidual symbol that composes the string

    for i in range(len(text)): 
        char = text[i] 
    
    # As the value "char" is storing each individual symbol, the symbol will be transformed with the applied formula
    # this loop is checking for symbols that are: capital letters, spaces, lower case letters, exclamation mark, question mark,
    # periods, @ symbol, dollar sign, and pound # symbol
    
    # EXPLANATION OF MATHEMATICAL FUNCTION
    # ORIGINS En(x) = (x+n)mod R
    # the E as a function of n of X, is equal to the sum of x + n, times the modulus of R
    # the mod function returns the remainder of the division
    
    # it's essential to understand that for make this project work the table of ASCII values was used as a reference table for
    # encryption and later on for decryption in the second program
    # Computers can only understand numbers, so an ASCII code is the numerical representation of a character 
    
        # """ Encrypt uppercase letters """
        # .isupper is a built-in-method in python 
        if (char.isupper()): # this line is checking if the symbol stored in the char value is a capital letter
            result += chr((ord(char) + key - 65) % 26 + 65) #""" data set of 26 symbols with an initial position of 65 in ASCII """
            
            #"""
            #------> the chr() method returns a character (a string) from an integer (represents unicode code point of the character).
            #------> the ord() method returns an integer representing Unicode code point for the given Unicode character.
            
            #------> key = the number input by the user
            
            #------> the number that follows the "%" represents the number that belong to the set of symbols from the ASCII table
            #---------- the number that is repetitive in the formula represents the initial position of the set of sybols
            
            #------> the section where it's "key-65" and "26+65" = these are proportion addition and subtraction to allow the translation of the symbols
            #--------- to stay within the set group
            #"""
            
        #""" Encrypt Numbers """ 
        elif (char.isdigit()): #.isdigit() is a built-in-method in python
            result += chr((ord(char) + key - 48) % 10 + 48) #""" data set of 10 symbols with an initial position of 48 in ASCII """
                
        #""" Encrypt Spaces """   
        elif (char.isspace()): #.isspace() is a built-in-method in python
            result += chr((ord(char) + key - 32) % 15 + 32) #""" data set of 15 symbols with an initial position of 32 in ASCII """
        
        #""" Encrypt Periods """ 
        elif (char == chr(46)): # 46 is the ASCII value of a period .
            result += chr((ord(char) + key - 33) % 14 + 33) #""" data set of 14 symbols with an initial position of 33 in ASCII """
        
        #""" Encrypt Commas """
        elif (char == chr(44)): # 44 is the ANCII value of a comma
            result += chr((ord(char) + key - 33) % 14 + 33) #""" data set of 14 symbols with an initial position of 33 in ASCII """
        
        #""" Encrypt Question Mark """
        elif (char == chr(63)): # 63 is the ASCII value of a ?
            result += chr((ord(char) + key - 58) % 7 + 58) #""" data set of 17 symbols with an initial position of 58 in ASCII """
        
        #""" Encrypt exclamation mark """
        elif (char == chr(33)): # 33 is the ASCII value of an !
            result += chr((ord(char) + key - 33) % 14 + 33) #""" data set of 14 symbols with an initial position of 33 in ASCII """
        
        #""" Encrypt @ symbol """
        elif (char == chr(64)): # 64 is the ASCII value of an @
            result += chr((ord(char) + key - 58) % 7 + 58) #""" data set of 7 symbols with an initial position of 58 in ASCII """
        
        #""" Encrypt Dollar Sign """ 
        elif (char == chr(36)): # 36 is the ASCII value of a $
            result += chr((ord(char) + key - 32) % 16 + 32) #""" data set of 16 symbols with an initial position of 32 in ASCII """
        
        #""" Encrypt Pound Symbol """ 
        elif (char == chr(35)): # 35 is the ASCII value of a #
            result += chr((ord(char) + key - 32) % 16 + 32) #""" data set of 16 symbols with an initial position of 32 in ASCII """
            
        
        #""" Default Statement: Encrypt lower case letters """
        else: 
            result += chr((ord(char) + key - 97) % 26 + 97) #""" data set of 26 symbols with an initial position of 97 in ASCII """
  
    return result 

#""" Output results """ 
print ("PlainText: " + text)
print ("Key: " + str(key))
print ("CipherText: " + encrypt(text,key))



