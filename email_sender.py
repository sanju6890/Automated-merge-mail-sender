# sender is the another python file which acts as dependency contains subject, body, and sender email_id and passsword
import sender
import smtplib
# a list of names and e-mail ids
name_list=[ ["Sanjay","sanjay@gmail.com"],
            ["Tech-deets","itworld@gmail.com"],
            ["Gopi","gopi@gmail.com"]
          ]

print('\n\n************************ WELCOME TO PYTHON E-mail SENDER *************************\n')
print('processing all e-mails to send.........\n')

# send_email() is the function which creates the SMTP request and send the e-mail.
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
