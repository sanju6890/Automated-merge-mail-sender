import sender
import smtplib

name_list=[ ["Sanjay","sanjay6890@mail.com"],
            ["Tech-deets","itworld.6890@gmail.com"],
            ["Sanju","sanjusaikap2001@gmail.com"]
          ]

print('\n\n************************ WELCOME TO PYTHON E-mail SENDER *************************\n')
print('processing all e-mails to send.........\n')

def send_email(subject,body,reciver_id,reciver_name):
    try:
        server=smtplib.SMTP_SSL("smtp.gmail.com",465)         
        server.login(sender.email_id,sender.password)         
        email=f"Subject:{subject}\n\n{body}"
        server.sendmail(sender.email_id,reciver_id,email)
        server.quit()
        print(f"E-mail sent successfully to {reciver_name} !!")
    except:
        print("E-mail sending failed !!")

for name,mail_id in name_list:
    body = f"Hello {name}\n{sender.body}"
    send_email(sender.subject,body,mail_id,name)

print('\nAll E-mails Sucessfully sent........')        
print("Thank you !!") 
