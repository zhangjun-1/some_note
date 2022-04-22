#邮件发送
import smtplib,string


with open('feng.txt','r',encoding= 'utf-8') as f:
    a = f.read()
HOST = "10.3.19.129"                          #定义smtp主机      
SUBJECT = "Test email from Python"              #邮件主题
TO = "zhangjun295@h-partners.com"               #邮件收件人
FROM = "zhangjun295@h-partners.com"             #发件人
text = a                                        #邮件内容
BODY = "\r\n".join((                            #组装sendmail方法的邮件主题内容，各段以"\r\n"分隔
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
    ))
server = smtplib.SMTP()                         #创建一个SMTP()对象
server.connect(HOST,"25")                       #通过connect连接smtp主机
server.login("xxxx@xxxx.com","password")          #邮箱账号登录校验
server.sendmail(FROM,[TO],BODY.encode('utf-8')) #发送邮件
server.quit()                                   #断开smtp

