#coding:utf8
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

#bngxqetniesgbaic
#kxqercjocxnybbbh
def send_Message(News = '卧槽',sub = '不明来历'):
	mail_info = {
		"from": "837538041@qq.com",
		"to": "837538041@qq.com",
		"hostname": "smtp.qq.com",
		"username": "837538041@qq.com",
		"password": "bngxqetniesgbaic",
		"mail_subject": sub,
		"mail_text": News,
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

# #encoding=utf-8
# import os


# cmd = """osascript<<END

# tell application "Messages"

# send "%s" to buddy "hbgxsm95@qq.com" of (service 1 whose service type is iMessage)

# end tell

# END"""

# def send_Message(News = '卧槽'):
     # print News
     # os.system(cmd % News)