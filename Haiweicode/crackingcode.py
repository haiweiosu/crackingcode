#This is a code cracking algorithm that select true
#password from given sweetwords.
#This algorithm considers the case where T is top 100 
#passwords in rockyou.com as true passwords.
#The honeywords already generatrd in last homework. 

#Author: Haiwei Su
#Date: 11/1/2015

import random
import sys
import string
from random import randint
from itertools import izip
import pprint
from collections import Counter


#This function read input file of rickyou password file
def parse_dataset(input_file):
    """
    Parse passwords from dataset and remove frequency count
    If file of form "$FREQUENCY $PASSWORD\n", keep only password
    """
    with open(input_file) as myfile:
        passwords = [line.rstrip('\n') for line in open(input_file)]
        passwords = [line.split()[1] if len(line.split()) > 1 else line.split()[0] for line in passwords]
    return passwords

#Given a row of sweetwords, this function identifies which 
#following 3 cases it applied to.The function categorizes a 
#row of sweetwords by checking the pattern of the first 
#passwords in the list. 
def check_pattern (row_list):
	word = row_list[0]
	numbercount = 0
	charcount = 0
	if word.isdigit():
		return 0
	for i in word:
		if i.isalpha():
			charcount += 1
		else:
			numbercount += 1

	if charcount == len(word):
		return 3
	else:
		return 2

#Given three cases, this function will crack the passwords 
#based on the case number returned by ch eck_pattern function
# 0: password containing only numbers
# 1: password mixing with numbers and letters
# 2: password containing only letters
def cracking_password (case_number, row_list):
	
		





























