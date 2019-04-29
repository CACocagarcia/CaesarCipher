#!/usr/bin/env python3

text = str(input('Enter message to decrypt: '))

"""
-> This program focuses on Decryption
-> the program will ask the user to input a ciphertext, and then through brute force the program will decrypt the ciphertext
-> Brute Force = trial-and-error method used to obtain information
------ The key to decrypt is unknown. What is known is that the encryption key is inbetween the numbers 1-26
------ BruteForce is applied by using a while loop, and with it use all 26 possible values for the key
"""

"""
it's essential to understand that for make this project work the table of ASCII values was used as a reference table for
encryption and later on for decryption in the second program
Computers can only understand numbers, so an ASCII code is the numerical representation of a character 
"""

"""
This text should be in line 55, but i set it here because it's a lot of info
EXPLANATION FOR SPECIAL CHARACTER DECRYPTION

-> These special characters could encrypted in the cyphertext: ! @ # $ ? .

-> What is known: Since i developed the encryption program, I have knowledge that those characters will be encrypted within the respected group
------- that they belong to in the ASCII table.

-> What is NOT known: To what character was the symbol encrypted to ?

-> Approach taken for the conditional statement:
------ We know each symbol that composes the ciphertext. We don't know what to match it to in the conditional statement though.
------ We know the formulas used in the Encryption program for each symbol. So my approach was this:
------ 1) Grab the initial symbol from the cyphertext and apply conditional argument: ==
------ 2) Grab the original formula used to encrypt a specific symbol: For Example: chr((ord(char) + key - 33) % 14 + 33) ; which belongs to periods
------ 3) set up the following statement: char == chr((46 + j - 33) % 14 + 33) ; for this case
------------ From the original encrypting formula, we dont know what would go for ord(char), because we don't know what exactly it encrypted
------------ if we leave ord(char), then the program will grab the already encrypted symbol, encrypt it again, and then make the comparison. That doesn't work
------------ So then what I decided to do was that in the formula, replace the ord(char) to the actual ASCII value of the symbol and then let it run the math
------------------ the program would encrypt that symbol each iteration, but at a certain iteration (appropriate key) the char value will equal to the value
------------------ provided by the formula. Meaning that the program has discovered with the appropriate key what was the original symbol encrypted into, and
------------------ then it will allow the program to decrypt the encrypted symbol back to its original symbol. 
"""

j = 1 # the variable J will be the variable that will be changing per iteration
while j <= 26:
    j += 1
# function to decrypt the message
    def decrypt(text,j):
        result = ""    # stores value for function
      
        # grabs the plaintext and stores each symbol
        for i in range(len(text)):
            char = text[i] 
      
            # initial condition is to check whether if the value for char is Upper Case
            if (char.isupper()):
                #------> the chr() method returns a character (a string) from an integer (represents unicode code point of the character).
                #------> the ord() method returns an integer representing Unicode code point for the given Unicode character.
                
                # EXPLANATION OF FIRST MATHEMATICAL FUNCTION
                # ORIGINS En(x) = (x-n)mod R
                # the E as a function of n of X, is equal to the difference of x - n, times the modulus of R
                # the mod function returns the remainder of the division
                
                #------> j = the number input by the user that will be changing over each iteration
                
                #------> the number that follows the "%" represents the number that belong to the set of symbols from the ASCII table
                #---------- the number that is repetitive in the formula represents the initial position of the set of sybols
                
                #------> the section where it's "j-65" and "26+65" = these are proportion addition and subtraction to allow the translation of the symbols
                #--------- to stay within the set group
                result += chr((ord(char) - j - 65) % 26 + 65) # data set of 26 symbols with an initial position of 65 in ASCII
            
            elif (char.isdigit()): #.isdigit() is a built-in-method in python
                result += chr((ord(char) - j - 48) % 10 + 48) # data set of 10 symbols with an initial position of 48 in ASCII
            
            #space    
            elif (char == chr((32 + j - 32) % 15 + 32)): # 32 in ASCII
                result += chr((ord(char) - j - 32) % 15 + 32) # data set of 15 symbols with an initial position of 32 in ASCII
            
            #period
            elif (char == chr((46 + j - 33) % 14 + 33)): # 46 in ASCII
                result += chr((ord(char) - j - 33) % 14 + 33) # data set of 14 symbols with an initial position of 33 in ASCII
            
            #comma
            elif (char == chr((44 + j - 33) % 14 + 33)): # 44 in ANSCII
                result += chr((ord(char) - j - 33) % 14 + 33) # data set of 14 symbols with an initial position of 33 in ASCII
            
            #question mark
            elif (char == chr((63 + j - 58) % 7 + 58)): # 63 in ASCII
                result += chr((ord(char) - j - 58) % 7 + 58) # data set of 7 symbols with an initial position of 58 in ASCII
                   
            #exclamation
            elif (char == chr((33 + j - 33) % 14 + 33)): # 33 in ASCII
                result += chr((ord(char) - j - 33) % 14 + 33) # data set of 14 symbols with an initial position of 33 in ASCII
            
            # @ symbol
            elif (char == chr((64 + j - 58) % 7 + 58)): # 64 in ASCII
                result += chr((ord(char) - j - 58) % 7 + 58) # data set of 7 symbols with an initial position of 58 in ASCII
            
            # $ symbol
            elif (char == chr((36 + j - 32) % 16 + 32)): # 36 in ASCII
                result += chr((ord(char) - j - 32) % 16 + 32) # data set of 16 symbols with an initial position of 32 in ASCII
            
            # pound # symbol
            elif (char == chr((35 + j - 32) % 16 + 32)): # 35 in ASCII
                result += chr((ord(char) - j - 32) % 16 + 32) # data set of 16 symbols with an initial position of 32 in ASCII

            # decrypt lowercase symbols
            else: 
                result += chr((ord(char) - j - 97) % 26 + 97) # data set of 26 symbols with an initial position of 97 in ASCII
            
        return result
    
    #output results 
    print ("PlainText: " + decrypt(text,j) )    