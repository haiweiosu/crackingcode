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
import enchant
from random import randint
from itertools import izip
import pprint
from collections import Counter


import csv

def parse_sweetword_sets(sweetwords_file):
    """
    Parse csv sweetwords into 2d matrix array.
    """
    sweetwords = []
    with open(sweetwords_file, 'rb') as f:
        reader = csv.reader(f)
        sweetwords = list(reader)
    return sweetwords

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
	#Dealing with the case where password containing only numbers
	if case_number == 1:
		serail_list = []
		for i in len(row_list):
			string = str(row_list[i-1])
			isSequence = False
			#First step, select numbers are in sequence. If it is in sequence, add it into seail_list
			for j in len(string):
				if int(string[j+1]) - int(string[j]) == int(string[j+2]) - int(string[j+1]):
					isSequence = True
					continue
				else:
					break
			if isSequence == True:
				serail_list.append(string)

		#Second step, calculate number of increasing sequence number vs. decreasing sequence number
		increasecount = 0
		decreasecount = 0
		increase_list = []
		decrease_list = []
		for i in len(serail_list):
			element = str(serail_list[i-1])
			if int(element[1]) - int(element[0]) == 1:
				increasecount += 1
				increase_list.add(element)
			elif int(element[1]) - int(element[0]) == -1:
				decreasecount += 1
				decrease_list.add(element)
		#if increasecount larger than decreasecount, choose the smallest increasing sequence number
		if increasecount >= decreasecount:
			guess = min(int(s) for s in increase_list)
		#else, choose the largest decreasing sequence number
		else:
			guess = max(int(s) for s in decrease_list)

	#Dealing with the case where password mixing with nubers and letters
	elif case_number == 2:
		serail_list = []
		#First, get the numerical part
		for b in len(row_list):
			string = str(row_list[i-1])
			number = filter(str.isdigit, string)
			serail_list.add(number)

		#repeat case1 algorithm
		serail_list2 = []
		for i in len(serail_list):
			string = str(serail_list[i-1])
			isSequence = False
			#First step, select numbers are in sequence. If it is in sequence, add it into seail_list
			for j in len(string):
				if int(string[j+1]) - int(string[j]) == int(string[j+2]) - int(string[j+1]):
					isSequence = True
					continue
				else:
					break
			if isSequence == True:
				serail_list2.append(string)

		#Second step, calculate number of increasing sequence number vs. decreasing sequence number
		increasecount = 0
		decreasecount = 0
		increase_list = []
		decrease_list = []
		for i in len(serail_list2):
			element = str(serail_list2[i-1])
			if int(element[1]) - int(element[0]) == 1:
				increasecount += 1
				increase_list.add(element)
			elif int(element[1]) - int(element[0]) == -1:
				decreasecount += 1
				decrease_list.add(element)
		#if increasecount larger than decreasecount, choose the smallest increasing sequence number
		if increasecount >= decreasecount:
			guess = min(int(s) for s in increase_list)
		#else, choose the largest decreasing sequence number
		else:
			guess = max(int(s) for s in decrease_list)

	#Dealing with the case where passwords containing only letters
	else:
		noCapitallist = []
		noSpeciallist = []
		for c in row_list:
			if not any(ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for ch in c):
			     noCapitallist.add(c)
			else:
				continue

		for d in noCapitallist:
			if any(h in "12$@0" for h in d):
				break
	    	else:
	    		noSpeciallist.add(d)

		e = enchant.Dict("en_US")

		for element in noSpeciallist:
			isword = e.check(element)
	    	if isword == True:
	    		guess = element
	return guess

sweetwords = parse_sweetword_sets(finaloutput.csv)
print sweetwords

a = truepassword_list(sweetwords, len(sweetwords))


def truepassword_list (data_row_file, m):
	finalguess = []
	for i in m:
		finalguess.add(cracking_password(check_pattern(data_row_file[i]), data_row_file[i]))

	return finalguess
