import smtplib
import getpass

myemail="mpnaveenkumr@gmail.com"
password=getpass.getpass()
recemail="mahammdarafik2000@gmail.com"

s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("mpnaveenkumr@gmail.com",306046008)

message="hai bro"

s.sendmail(myemail,recemail,message)


s.quit()