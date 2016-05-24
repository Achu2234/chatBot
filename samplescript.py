#C:\Users\TWBRITT\AppData\Local\Programs\Python\Python35-32
import urllib
import json

import urllib.request
import request1
import webbrowser
from duckduckgo import duckduckgo
from PyDictionary import PyDictionary
#duck=duckduckgo();
parser='htmlparser'
definedstringjoin=""
name=""
askingforname=True
definitionvalues=["what is a ", "define ", "what is an "]
browsersearchvalues=["search for"]
ivory_filesearch_key=["What is your","what is your favorite", "what is your all-time", "what is your favorite", ""]
ivory_file={'name': 'Ivory', 'age': '15', 'color': 'orange', 'eye color': 'blue', 'movie': 'The Internship', 'book': 'Harry Potter Book Six', 'band': 'Casting Crowns', 'Song': 'Die a Happy Man', 'food': 'fried rice'}
ivory_for_for=['name', 'age', 'color', 'eye color', 'movie', 'book', 'band', 'song', 'food']
dictionary=PyDictionary()

#soup=dictionary.PyDictionary(html, 'htmlparser')
#print (dictionary.meaning("indentation"))

print ("Hello, I am Ivory. What is your name?")
inputer=input("A: ")
print(ivory_file[ivory_for_for[1]])
def run():
	global ivory_file
	global askingforname
	global ivory_for_for
	global definedstringjoin
	global inputer
	global ivory_file
	global ivory_filesearch_key
	if askingforname==True:
		name=inputer
		askingforname=False
#for num in range(len(input)):
	for fileb in range (len(ivory_filesearch_key)):
		for c in range (len(ivory_for_for)):
			if inputer.find(ivory_filesearch_key[fileb]+ivory_for_for[c])>-1:
				print("My favorite " + ivory_for_for[c] + " is " + ivory_file[ivory_for_for[c]])
				break
	for num in range (len(definitionvalues)):
		if inputer.find(definitionvalues[num])>-1:
			abc=inputer.find(definitionvalues[num])+len(definitionvalues[num])
			for fnum in range(abc, len(inputer)):
				definedstringjoin=definedstringjoin+inputer[fnum]
			#print(definedstringjoin)
				if int(abc)+len(definedstringjoin)==len(inputer):
					print(dictionary.meaning(definedstringjoin))
					abc=0
					definedstringjoin=""
	inputer=input("A: ")
	run()
				
		#print (abc)
		#print (input.find(definitionvalues))
#print (dictionary.meaning())		
#if input.find("hello")>-1:
url="https://www.google.com/?gws_rd=ssl#q="+inputer
print ("Hello", name)
print (url)
inputer=input("A: ")
run()
#r=duckduckgo.query('mars')
#print(r.answer.primary)
#duckduckgo = urllib.request.urlopen("http://api.duckduckgo.com/?q=dogs+description&format=json&pretty=1");
#duckduckgo3 = json.load(urllib.request.urlopen("https://www.google.com/?gfe_rd=ssl&ei=JiIdV8u7LY_M8Ae77YSwDA#safe=strict&q=mars", 'utf-8'));
#duckduckgo3 = json.loads(str(urllib.request.urlopen("https://www.google.com/?gfe_rd=ssl&ei=JiIdV8u7LY_M8Ae77YSwDA#safe=strict&q=mars"), 'html'));
#stringshortener=string(duckduckgo)
#if stringshortener.length

#print(duckduckgo3.read());
#print (duckduckgo.get_zci('random'))
#webbrowser.get().open(url)