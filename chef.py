"""
ChefBot - Shows the solution to Codechef problems using selenium web-driver API.
Takes username, password and problemcode and displays the first accepted solution from all submissions. 

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pprint import pprint
from getpass import getpass
import time


class ChefBot:
	def __init__(self, username, pswd):
		self.username = username
		self.pswd = pswd
		self.bot = webdriver.Firefox()
	
	def login(self):
		bot = self.bot
		bot.get("https://www.codechef.com/")
		username = bot.find_element_by_id('edit-name')
		pswd = bot.find_element_by_name('pass')
		username.clear()
		pswd.clear()
		time.sleep(3)
		username.send_keys(self.username)
		pswd.send_keys(self.pswd)
		pswd.submit()
# Not too classy ->	pswd.send_keys(Keys.RETURN)
		time.sleep(3)
	
	def destroy(self):
		" Close the window after the job is done. "
		self.bot.close()

	def logout(self):
		bot = self.bot 
		"Logs out of the current session. "
		bot.get('https://www.codechef.com/node')
		bot.find_element_by_class_name('logout-link').click()

	def cookies(self):
		i = 0
		" Stores all cookies used by the link, because why not? "
		bot = self.bot
		cookie = {'name':'foo' , 'value' : 'bar'}
		bot.add_cookie(cookie)
		try:
			file = open('file.txt', 'w+')
			pprint(bot.get_cookies(), file)
			print("Cookie objects stored in file. ")
		except FileNotFoundError as ex1:
			print("File not found or couldn't be opened. ")
		finally:
			print("Cookie processing done.")

	def problem_solver(self, problem_code,lang):
		" Stores the solution of the problem in a file. "
		bot = self.bot
		bot.get('https://www.codechef.com/status/' + problem_code)
# Click all submissions button.
		sel = Select(bot.find_element_by_id("status"))
		try:
			for index in range(len(sel.options)):
				sel = Select(bot.find_element_by_name("status"))
				sel.select_by_index(index)
				sel.select_by_visible_text("AC")
			for index in range(len(sel.options)):
				sel = Select(bot.find_element_by_name("language"))
				sel.select_by_index(index)
				sel.select_by_visible_text(lang)
			clicker = bot.find_element_by_name("Submit")
			clicker.click()
			tab = bot.find_element_by_link_text('View')
			tab.click()
			bot.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
		except Exception as ex:
			print(ex)
'''
Opens file and stores code in it. Dosen't work because all code is stored in weird HTML tags and not plaintext.  
			try:
				sol = open(problem_code+'.cpp', 'w+')
				data = bot.find_element_by_class_name('ace_content').gettext()
				pprint(data, sol)
				print("Data succesfully written to file. ")
			except Exception as ex2:
				print(ex2)
			finally:
				print("File processing done. ")
'''
		
		
user = str(input("Username: "))
passkey = getpass(prompt="Password: ")
probcode = str(input("Problem Code: "))
lang = str(input("Language (C++14,PYTH,JAVA etc.): "))
Bot = ChefBot(user, passkey)
Bot.login()
Bot.cookies()
time.sleep(2)
Bot.problem_solver(probcode, lang)
time.sleep(2)
Bot.logout()
time.sleep(2)
Bot.destroy()