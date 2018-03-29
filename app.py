#chcp 936 <--run this on the command prompt to view chinese characters
import colorama
import sqlite3
import re

from colorama import Fore, Back, Style
colorama.init(autoreset=True)
score = 0


def findWholeWord(w,a):
	countLimit = 3
	if len(w) < 3:
		return False
	elif w in a:
		return True
	else:
		return False

def createDatabase():
	conn = sqlite3.connect('test.db')
	print (" Created database successfully")
	conn.execute("DROP TABLE IF EXISTS LANGUAGE")
	conn.execute('''CREATE TABLE LANGUAGE
         (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         Question           TEXT    NOT NULL,
         Answer            TEXT     NOT NULL);''')
	print ("Table created successfully")
	conn.close()


def populateDb():
	conn = sqlite3.connect('test.db')
	total = 0
	with open('file.txt' , "r", encoding="utf-8") as fp:
		line = fp.readline()
		print(Fore.GREEN + "Inserting...")
		while line:
			total+=1
			text = line.split(":")
			question = text[0]
			answer = text[1].strip()
			conn.execute('''INSERT INTO LANGUAGE (Question,Answer)VALUES (?, ? )''', (question, answer))
			line = fp.readline()
		conn.commit()
		print("{} records inserted".format(total))


def startQuiz():
	conn = sqlite3.connect('test.db')
	cursor = conn.execute('SELECT * FROM LANGUAGE')
	score = 0
	for row in cursor:
		question = row[1]
		answer = row[2]
		print("What is ", end="")
		print(Fore.GREEN + question)
		response = input("Your Answer: ")
		if response.casefold() == "hint":
			wordHint = ""
			wordCount = 1
			for i in answer:
				if i ==";":
					i=" | "
				wordCount +=1
				if wordCount % 2 == 0:
					wordHint += i
				else:
					wordHint+="*"
			print()
			print("Hint: {}".format(wordHint))
			response = input("Your Answer: ")


		if response.casefold() == answer.casefold():
			print(Fore.CYAN + "Correct!")
			print()
			score+=1
		else:
			partialAnsa = findWholeWord(response,answer)
			print(partialAnsa)
			if partialAnsa:
				print(Fore.CYAN + "Correct!")
				print()
				score+=1
			else:
				print("Wrong! the correct answer is: ", end="")
				print(Fore.YELLOW + answer)	
				print()



def searchWord(word):
	conn = sqlite3.connect('test.db')
	cursor = conn.execute('SELECT * FROM LANGUAGE')

def getOption(x):
	if x == "2":
		startQuiz()
	elif x == "3":
		searchWord()




print(Fore.GREEN + "Welcome...")
print(Fore.GREEN + "Enter 1: To set up database \nEnter 2: To take quiz")
userInput = input()
if userInput == "1":
	createDatabase()
	populateDb()
	print("Alright sparky! all done..")
	print(Fore.GREEN + "Enter 2: To take quiz \n Enter 3: To search for a word")
	userOption = input()
	getOption(userOption)
elif userInput == "2":
	startQuiz()


	





# with open('file.txt' , "r", encoding="utf-8") as fp:  
#    line = fp.readline()
#    cnt = 1
#    while line:
#        text = line.split(":")
#        question = text[0]
#        answer = text[1].strip()
#        print("What is ", end="")
#        print(Fore.GREEN + question)	
#        response = input("Your Answer: ")
#        #Sresponse = response.replace(' ', '-').lower()
#        #print("Answer:{}|Response:{}".format(answer,response))
#        #print("Answer:{}|Response:{}".format(len(answer),len(response)))
#        if response.casefold() == answer.casefold():
#        	print(Fore.CYAN + "Correct!")
#        	score+=1
#        else: 
#        	print("Wrong! the correct answer is: ", end="")
#        	print(Fore.YELLOW + answer)	
#        print("Your current score is: {}".format(score))
#        print("")
#        line = fp.readline()







    

