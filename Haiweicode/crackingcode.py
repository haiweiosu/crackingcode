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
		return 2
	else:
		return 1

#Given three cases, this function will crack the passwords 
#based on the case number returned by ch eck_pattern function
# 0: password containing only numbers
# 1: password mixing with numbers and letters
# 2: password containing only letters
def cracking_password (case_number, row_list):
	#Dealing with the case where password containing only numbers
	guess = None
	if case_number == 0:
		serail_list2 = []
		for number in row_list:
			if len(number) <= 1:
				return random.choice(row_list)
			prev_digit = number[0]
			gap = int(number[1] or 0) - int(number[0] or 0)
			# print gap
			isSequence = True
			count = 0
			for idx in range(1, len(number)):
				if gap != (int(number[idx]) - int(prev_digit)):
					isSequence = False
					break
				else:
					prev_digit = number[idx]
					count += 1
			if isSequence:
				serail_list2.append(number)
			elif not isSequence and count == len(number) - 2:
				serail_list2.append(number)
			else:
				guess = row_list.index(random.choice(row_list))
		# print guess

		#Second step, calculate number of increasing sequence number vs. decreasing sequence number
		if len(serail_list2) != 0:
			increase_list = []
			decrease_list = []
			# print serail_list2
			for i in range(0, len(serail_list2)):
				element = serail_list2[i]
				if int(element[1]) - int(element[0]) >= 0 :
					increase_list.append(element)
				elif int(element[1]) - int(element[0]) < 0:
					decrease_list.append(element)
			#if increasecount larger than decreasecount, choose the smallest increasing sequence number
			if len(increase_list) >= len(decrease_list):
				guess = increase_list.index(min(increase_list))
			#else, choose the largest decreasing sequence number
			else:
				guess = decrease_list.index(max(decrease_list))
		# print increase_list

	#Dealing with the case where password mixing with nubers and letters
	elif case_number == 1:
		serail_list = []
		#First, get the numerical part
		for b in range(len(row_list)):
			string = str(row_list[b-1])
			number = filter(str.isdigit, string)
			letter = filter(str.isalpha, string)
			serail_list.append(number)
		# print serail_list
		#repeat case1 algorithm
		serail_list2 = []
		for number in serail_list:
			if len(number) <= 1:
				return row_list.index(random.choice(row_list))
			prev_digit = number[0]
			gap = int(number[1]) - int(number[0])
			isSequence = True
			for idx in range(1, len(number)):
				if gap != (int(number[idx]) - int(prev_digit)):
					isSequence = False
					break
				else:
					prev_digit = number[idx]
			if isSequence:
				serail_list2.append(number)

		#Second step, calculate number of increasing sequence number vs. decreasing sequence number
		increase_list = []
		decrease_list = []
		# print serail_list2
		for i in range(0, len(serail_list2)):
			element = serail_list2[i]
			if int(element[1]) - int(element[0]) == 1:
				increase_list.append(element)
			elif int(element[1]) - int(element[0]) == -1:
				decrease_list.append(element)
		#if increasecount larger than decreasecount, choose the smallest increasing sequence number
		if len(increase_list) >= len(decrease_list):
			temp = letter + min(increase_list)
			guess = row_list.index(temp)
		#else, choose the largest decreasing sequence number
		else:
			temp = letter + max(decrease_list)
			guess = row_list.index(temp)

	#Dealing with the case where passwords containing only letters
	else:
		noCapitallist = []
		noSpeciallist = []
		for c in row_list:
			if not any(ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for ch in c):
				 noCapitallist.append(c)
			else:
				continue
		for d in noCapitallist:
			if any(h in "12$@0" for h in d):
				break
			else:
				noSpeciallist.append(d)

		e = enchant.Dict("en_US")

		for i, element in enumerate(noSpeciallist):
			isword = e.check(element) or e.check(element.title())
			if isword:
				guess = i
			else:
				guess = noSpeciallist.index(random.choice(noSpeciallist))
	return guess

def main():

	# Return early if not enough args
	if len(sys.argv) < 4:
		print "Wrong number of arguments."
		return

	# Parse command-line arguments
	outputf = sys.argv[1]
	n = int(sys.argv[1])
	m = int(sys.argv[2])
	inputf = sys.argv[3]


	sweetwords = parse_sweetword_sets(inputf) # Parse input file

	finalguess = []
	for i in sweetwords:
		a = check_pattern(i)
		b = cracking_password(a, i)
		finalguess.append(b)
	print finalguess


main()