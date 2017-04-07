import http.cookiejar
import urllib.request
import re
import datetime
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

def crawl_for_news():
	req = urllib.request.Request(url = web,
							 headers = headers)
	html = urllib.request.urlopen(req).read()

	re_html = re.compile(html.decode())

	result_list = re.findall('<a href=\"\/node\/.*',html.decode())

	for item in result_list:
		sub_result = re.sub('<a href=\"\/node\/','',item)
		node_num = re.sub('\".*','',sub_result)
		sub_result = re.sub('.*\">','',item)
		msg = re.sub('<.*','',sub_result)
		#print(msg)
		#news_dict[str(node_num)] = msg
		if(str(node_num) not in news_dict.keys()):
			news_dict[str(node_num)] = msg
			mail_text = msg + ',http://seit.sysu.edu.cn/node/' + str(node_num)
			send_msg(msg,mail_text)
			continue
		else:			
			continue
			
def send_msg(msg,mail_text):
	mail_info = {
		"from": "837538041@qq.com",
		"to": "837538041@qq.com",
		"hostname": "smtp.qq.com",
		"username": "837538041@qq.com",
		"password": "jrcqfdwxqdfkbeac",
		"mail_subject": '学院新闻：'+msg,
		"mail_text": mail_text,
		"mail_encoding": "utf-8"
	}

	#if __name__ == '__main__':
		#这里使用SMTP_SSL就是默认使用465端口
	try:
		smtp = SMTP_SSL(mail_info["hostname"])
		smtp.set_debuglevel(1)
		
		smtp.ehlo(mail_info["hostname"])
		smtp.login(mail_info["username"], mail_info["password"])

		msg = MIMEText(mail_info["mail_text"], "plain", mail_info["mail_encoding"])
		msg["Subject"] = Header(mail_info["mail_subject"], mail_info["mail_encoding"])
		msg["from"] = mail_info["from"]
		msg["to"] = mail_info["to"]
		
		smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())

		smtp.quit()
		print ("suceess")
	except Exception:
		print ("failed")


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'}

web = 'http://seit.sysu.edu.cn/all/'

req = urllib.request.Request(url = web,
							 headers = headers)
html = urllib.request.urlopen(req).read()

filepath = "E:/PyCharm/testFile.txt"

filehandle = open(filepath,'w+',encoding='UTF-8')

filehandle.write(html.decode())

re_html = re.compile(html.decode())

result_list = re.findall('<a href=\"\/node\/.*',html.decode())

news_dict = {}

for item in result_list:
	sub_result = re.sub('<a href=\"\/node\/','',item)
	node_num = re.sub('\".*','',sub_result)
	sub_result = re.sub('.*\">','',item)
	msg = re.sub('<.*','',sub_result)
	#print(msg)
	news_dict[str(node_num)] = msg
	
	#下面两行测试完记得删掉
	mail_text = msg + ',http://seit.sysu.edu.cn/node/' + str(node_num)
	send_msg(msg,mail_text)


begin_time = datetime.datetime.now()
while(1):
	end_time = datetime.datetime.now()
	gap = (end_time - begin_time).seconds
	if(gap >= 10):
		begin_time = datetime.datetime.now()
		print (begin_time)
		crawl_for_news()
		
		continue
	else:
		continue
	
	