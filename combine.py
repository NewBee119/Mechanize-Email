# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import mechanize
import socket
import time
import eventlet
import smtplib
from email.mime.text import MIMEText
from email.header import Header



#Browser
br = mechanize.Browser()

#options
br.set_handle_equiv(True)
#br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

#Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.set_debug_http(True)
br.set_debug_redirects(True)
br.set_debug_responses(True)

#欺骗行为
# br.addheaders = [('User-agent', 'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11'
# )]
br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
)]



def sendreport(content,count):
	msg_from = '????????@qq.com'#发件人邮箱
	passwd = '????????????????'#授权码
	# msg_to = '1265616844@qq.com'
	msg_to = ['user-1@example.com','user-2@example.com']
	c = ",".join(msg_to)#收件人邮箱
	 

	subject = "timeout information"
	content = "connection number:" +" " + str(count)+ " , " + content
	msg = MIMEText(content)
	msg['Subject'] = subject
	msg['From'] = msg_from
	msg['To'] = c
	s = smtplib.SMTP_SSL("smtp.qq.com",465)#邮件服务器及端口号
	s.login(msg_from,passwd)
	s.sendmail(msg_from, msg_to, msg.as_string())
	print "success"
	s.quit()



def sendmail(flag_0,flag_1,count):
	if flag_0 and flag_1:
		sendreport("baidu and google all down",count)
		return True 
	if flag_0 == True and flag_1 == False:
		sendreport("baidu is down while google is ok",count)
		return True 
	if flag_0 == False and flag_1 == True:
		sendreport("google is down while baidu is ok",count)
		return True 
	return False


# content1 = "google connect timeout"
# msggoogle = MIMEText(content


dict_data = []
dict_h = []
f = open('english.txt')
for i in f:
	dict_data.append(i.strip('\n'))
	dict_h.extend(dict_data)
	# dict_h.extend(dict_data)  

print dict_h
count = 0
count1 = 0
t3_list=[]
t33_list=[]
total_time=120
FLAG = 0
while True:
	for i in dict_h:
		flag_0 = False
		flag_1 = False
		t1=time.time()
		print i
		brr = None			
		with eventlet.Timeout(60, False):
			r = br.open('https://www.baidu.com/')	
			br.select_form(nr = 0)
			# print br.form
			br.form['wd'] = i
			br.submit()		
			eventlet.monkey_patch() 
			brr=br.response().read()
		if brr is None:
			flag_0 = True
		else:
			pass
		t2=time.time()
		print 'CONNECTION CLOSED'
		t3 = t2-t1
		print t3
		time.sleep(total_time-t3)
		count = count+1
		print 'baiduCountnumber: ',count
		t11=time.time()
		print i
		brr = None
		with eventlet.Timeout(60, False):
			r = br.open('https://www.google.com/')
			br.select_form(nr = 0)
			# print br.form
			br.form['q'] = i
			br.submit()		
			eventlet.monkey_patch() 
			brr=br.response().read()
		if brr is None:
			flag_1 = True
		else:
			pass
		t22=time.time()
		print 'CONNECTION CLOSED'
		t33 = t22-t11
		print t33
		time.sleep(total_time-t33)
		count1 = count1+1
		print 'googleCountnumber: ',count1
		if flag_0|flag_1 :
			FLAG = FLAG + 1
		else:
			FLAG = 0
		if FLAG ==3 :
			if sendmail(flag_0,flag_1,count):
				exit()
