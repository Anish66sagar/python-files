#program to send mail
import smtplib
import getpass
myemail=input("your mail id:")
password=getpass.getpass()
recemail=input("Receiver mail Id:")
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(myemail,password)
message="Mess"
s.sendmail(myemail,recemail,message)
s.quit()
