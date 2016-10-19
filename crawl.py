#encoding=utf-8
import sys, re
import random, traceback
import urllib

import urllib.request
#from urllib import urlopen
from bs4 import *
import os
import iMessage
import datetime

#电信院
web1 = "http://seit.sysu.edu.cn"
#数据院
web2 = "http://sdcs.sysu.edu.cn"
#教务处
web3 = "http://jwc.sysu.edu.cn"
#学生处
web4 = "http://xsc.sysu.edu.cn"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'}
seit_1 = "quicktabs-tabpage-_tab2-"
seit_2 = "quicktabs-tabpage-tztab1-"
sdcs = "cat-"
jwc = "block-views-jwnews-block-"
xsc = "quicktabs-tabpage-fronttabright-"
def Showtext(word):
	print (word.encode('gbk', 'ignore'))

def Initialize_seit(url, page, start = 0, end = 3):
	global seit_dict
	#url = "quicktabs-tabpage-tztab1-%s"
	url += "%s"
	for i in range(start, end):
		try:
			tagpage = url % i
			req = urllib.request.Request(url = page,
					headers = headers)
			c = urllib.request.urlopen(req)
			read_soup = BeautifulSoup(c.read(), "html.parser",from_encoding="utf-8" )
			#print (read_soup)
			search_list = read_soup.find_all(id=tagpage)[0]
			#print search_list
			dl = search_list("ul")[0]
			for li in dl("li"):
				date = li.find_all("span")
				#print date[0].get_text()
				try:
					#print li.find_all("a")[0]["title"]
					seit_dict[li.find_all("a")[0]["title"]]=date[0].get_text()
				except Exception:
					msg = traceback.format_exc()
					#print li.find_all("a")[0].get_text()
					seit_dict[li.find_all("a")[0].get_text()]=date[0].get_text()
					continue
		except Exception:
			msg = traceback.format_exc()
			print (msg)

def Initialize_sdcs(url, page, start = 0, end = 3):
	global sdcs_dict
	#url = "quicktabs-tabpage-tztab1-%s"
	url += "%s"
	for i in range(start, end):
		if i % 2 == 0:
			try:
				tagpage = url % i
				req = urllib.request.Request(url = page,
						headers = headers)
				c = urllib.request.urlopen(req)
				read_soup = BeautifulSoup(c.read(), "html.parser", from_encoding="utf-8")
				#print read_soup
				search_list = read_soup.find_all(id=tagpage)[0]
				#print search_list
				dl = search_list("ul")[0]
				for li in dl("li"):
					date = li.find_all("span")
					#print date[0].get_text()
					try:
						#print li.find_all("a")[0]["title"]
						sdcs_dict[li.find_all("a")[0]["title"]]=date[0].get_text()
					except Exception:
						msg = traceback.format_exc()
						#print li.find_all("a")[0].get_text()
						sdcs_dict[li.find_all("a")[0].get_text()]=date[0].get_text()
						continue
			except Exception:
				msg = traceback.format_exc()
				print (msg)

def Initialize_JWC(url, page, start = 1, end = 3):
	global JWC_dict
	#url = "quicktabs-tabpage-tztab1-%s"
	url += "%s"
	for i in range(start, end):
		try:
			tagpage = url % i
			req = urllib.request.Request(url = page,
					headers = headers)
			c = urllib.request.urlopen(req)
			read_soup = BeautifulSoup(c.read(), "html.parser", from_encoding="utf-8")
			#print read_soup
			search_list = read_soup.find_all(id=tagpage)[0]
			#print search_list
			dl = search_list("ul")[0]
			for li in dl("li"):
				date = li.find_all("span")
				#print date[0].get_text()
				try:
					#print li.find_all("a")[0]["title"]
					JWC_dict[li.find_all("a")[0]["title"]]=date[0].get_text()
				except Exception:
					msg = traceback.format_exc()
					#print li.find_all("a")[0].get_text()
					JWC_dict[li.find_all("a")[0].get_text()]=date[0].get_text()
					continue
		except Exception:
			msg = traceback.format_exc()
			print (msg)

def Initialize_XSC(url, page, start = 1, end = 3):
	global XSC_dict
	#url = "quicktabs-tabpage-tztab1-%s"
	url += "%s"
	try:
		tagpage = url % 0
		req = urllib.request.Request(url = page,
				headers = headers)
		c = urllib.request.urlopen(req)
		read_soup = BeautifulSoup(c.read(), "html.parser", from_encoding="utf-8")
		#print read_soup
		search_list = read_soup.find_all(id=tagpage)[0]
		#print search_list
		dl = search_list("ul")[0]
		for li in dl("li"):
			date = li.find_all("span")
			#print date[0].get_text()
			try:
				#print li.find_all("a")[0]["title"]
				XSC_dict[li.find_all("a")[0]["title"]]=date[0].get_text()
			except Exception:
				msg = traceback.format_exc()
				#print li.find_all("a")[0].get_text()
				XSC_dict[li.find_all("a")[0].get_text()]=date[0].get_text()
				continue
	except Exception:
		msg = traceback.format_exc()
		print (msg)


def Notification_seit(url, page, start = 0, end = 3):
	global seit_dict
	signal = 1
	url += "%s"
	for i in range(start, end):
		try:
			tagpage = url % i
			req = urllib.request.Request(url = page,
					headers = headers)
			c = urllib.request.urlopen(req)
			read_soup = BeautifulSoup(c.read(), "html.parser", from_encoding="utf-8")
			#print read_soup
			search_list = read_soup.find_all(id=tagpage)[0]
			#print search_list
			dl = search_list("ul")[0]
			for li in dl("li"):
				date = li.find_all("span")
				try:
					#print li.find_all("a")[0]["title"]
					if li.find_all("a")[0]["title"] not in seit_dict.keys():
						print ("hehe")
						seit_dict[li.find_all("a")[0]["title"]]=date[0].get_text()
						iMessage.send_Message(News=li.find_all("a")[0]["title"],sub='News From SEIT')
						#iMessage.send_Message(News='News From SEIT')
						signal = 0
					else:
						continue
				except Exception:
					msg = traceback.format_exc()
					if li.find_all("a")[0].get_text() not in seit_dict.keys():
						seit_dict[li.find_all("a")[0].get_text()]=date[0].get_text()
						print ("xixi")
						iMessage.send_Message(News=li.find_all("a")[0].get_text(),sub='News From SEIT')
						#iMessage.send_Message(News='News From SEIT')
						signal = 0
					else:
						continue
		except Exception:
			msg = traceback.format_exc()
			print (msg)
	if signal == 1:
		print ("No News From SEIT!")

def Notification_sdcs(url, page, start = 1, end = 5):
	global sdcs_dict
	url += "%s"
	signal = 1
	for i in range(start, end):
		if i % 2 == 0:
			try:
				tagpage = url % i
				req = urllib.request.Request(url = page,
						headers = headers)
				c = urllib.request.urlopen(req)
				read_soup = BeautifulSoup(c.read(), "html.parser", from_encoding="utf-8")
				#print read_soup
				search_list = read_soup.find_all(id=tagpage)[0]
				#print search_list
				dl = search_list("ul")[0]
				for li in dl("li"):
					date = li.find_all("span")
					try:
						#print li.find_all("a")[0]["title"]
						if li.find_all("a")[0]["title"] not in sdcs_dict.keys():
							print ("hehe")
							sdcs_dict[li.find_all("a")[0]["title"]]=date[0].get_text()
							iMessage.send_Message(News=li.find_all("a")[0]["title"],sub='News From SDCS')
							#iMessage.send_Message(News='News From SDCS')
							signal = 0
						else:
							continue
					except Exception:
						msg = traceback.format_exc()
						if li.find_all("a")[0].get_text() not in sdcs_dict.keys():
							sdcs_dict[li.find_all("a")[0].get_text()]=date[0].get_text()
							print ("xixi")
							signal = 0
							iMessage.send_Message(News=li.find_all("a")[0].get_text(),sub='News From SDCS')
							#iMessage.send_Message(News='News From SDCS')
						else:
							continue
			except Exception:
				msg = traceback.format_exc()
				print (msg)
	if signal == 1:
		print ("No News From SDCS!")

def Notification_JWC(url, page, start = 1, end = 3):
	global JWC_dict
	url += "%s"
	signal = 1
	for i in range(start, end):
		try:
			tagpage = url % i
			req = urllib.request.Request(url = page,
					headers = headers)
			c = urllib.request.urlopen(req)
			read_soup = BeautifulSoup(c.read(), "html.parser", from_encoding="utf-8")
			#print read_soup
			search_list = read_soup.find_all(id=tagpage)[0]
			#print search_list
			dl = search_list("ul")[0]
			for li in dl("li"):
				date = li.find_all("span")
				try:
					#print li.find_all("a")[0]["title"]
					if li.find_all("a")[0]["title"] not in JWC_dict.keys():
						print ("hehe")
						JWC_dict[li.find_all("a")[0]["title"]]=date[0].get_text()
						iMessage.send_Message(News=li.find_all("a")[0]["title"],sub='News From JWC')
						#iMessage.send_Message(News='News From JWC')
						signal = 0
					else:
						continue
				except Exception:
					msg = traceback.format_exc()
					if li.find_all("a")[0].get_text() not in JWC_dict.keys():
						JWC_dict[li.find_all("a")[0].get_text()]=date[0].get_text()
						print ("xixi")
						signal = 0
						iMessage.send_Message(News=li.find_all("a")[0].get_text(),sub='News From JWC')
						#iMessage.send_Message(News='News From JWC')
					else:
						continue
		except Exception:
			msg = traceback.format_exc()
			print (msg)
	if signal == 1:
		print ("No News From JWC!")

def Notification_XSC(url, page, start = 1, end = 3):
	global XSC_dict
	url += "%s"
	signal = 1
	try:
		tagpage = url % 0
		req = urllib.request.Request(url = page,
				headers = headers)
		c = urllib.request.urlopen(req)
		read_soup = BeautifulSoup(c.read(), "html.parser", from_encoding="utf-8")
		#print read_soup
		search_list = read_soup.find_all(id=tagpage)[0]
		#print search_list
		dl = search_list("ul")[0]
		for li in dl("li"):
			date = li.find_all("span")
			try:
				#print li.find_all("a")[0]["title"]
				if li.find_all("a")[0]["title"] not in XSC_dict.keys():
					print ("hehe")
					XSC_dict[li.find_all("a")[0]["title"]]=date[0].get_text()
					iMessage.send_Message(News=li.find_all("a")[0]["title"],sub='News From XSC')
					#iMessage.send_Message(News='News From XSC')
					signal = 0
				else:
					continue
			except Exception:
				msg = traceback.format_exc()
				if li.find_all("a")[0].get_text() not in XSC_dict.keys():
					XSC_dict[li.find_all("a")[0].get_text()]=date[0].get_text()
					print ("xixi")
					signal = 0
					iMessage.send_Message(News=li.find_all("a")[0].get_text(),sub='News From XSC')
					#iMessage.send_Message(News='News From XSC')
				else:
					continue
	except Exception:
		msg = traceback.format_exc()
		print (msg)
	if signal == 1:
		print ("No News From XSC!")


def Run(start, end):
	global seit_dict
	global sdcs_dict
	global JWC_dict
	global XSC_dict
	Initialize_seit(seit_1,web1, start, end)
	Initialize_seit(seit_2,web1,start,end)
	Initialize_sdcs(sdcs,web2,1,5)
	Initialize_JWC(jwc,web3,1,3)
	Initialize_XSC(xsc,web4,1,3)
	#for date in XSC_dict.keys():
	#	print date

if __name__ == "__main__":
	#reload(sys)
	#sys.setdefaultencoding('utf-8')
	seit_dict={}
	sdcs_dict={}
	JWC_dict={}
	XSC_dict={}
	begin_time = datetime.datetime.now()
	Run(0,3)
	while 1:
		end_time = datetime.datetime.now()
		interval = (end_time - begin_time).seconds
		if interval > 10:
			begin_time = datetime.datetime.now()
			print (begin_time)
			Notification_seit(seit_1,web1, 0,3)
			Notification_seit(seit_2,web1,0,3)
			Notification_sdcs(sdcs,web2,1,5)
			Notification_JWC(jwc,web3,1,3)
			Notification_XSC(xsc,web4,1,3)
			continue
		else:
			continue