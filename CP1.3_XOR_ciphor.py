import hex_converter
import operator
import base64

#import langdetect

# **************************************************************************
#  INSTRUCTIONS:
#
# The hex encoded string:
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

# has been XOR'd against a single character. Find the key, decrypt the message.
# You can do this by hand. But don't: write code to do it for you.

# How? Devise some method for "scoring" a piece of English plaintext. 
# Character frequency is a good metric. 
# Evaluate each output and choose the one with the best score.
# ***************************************************************************

# create a list of characters
# base64 contains 64 characters
chr_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
            'U', 'V', 'W', 'X', 'Y', 'Z',  'a', 'b', 'c', 'd', 
            'e', 'g', 'f', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'x', 'y', 
            'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '+', '/']

# create a list of XOR'd values. should have same index as chr_list. print the n response with n chr. 
def plaintext_scorer(str):
    #if en > than other languages
    # print response
    # how to score english responses? which is more english


def main():
    str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    # convert to base64
    # convert to byte
    # XOR with chr_list
    # convert to base64? or none
    # score 

if __name__ == "__main__":
    main()
