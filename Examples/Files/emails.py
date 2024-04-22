from email.message import EmailMessage #doesn't allow to send email
import smtplib #sending emails

my_email = EmailMessage()
print(type(my_email))

my_email['from'] = 'Natalie'
my_email['to'] = 'example@example.com'
my_email['subject'] = "Hello from Python"
my_email.set_content("Hello! \n I just wanted to say hello!")

# needs to be opened and closed like a file
with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
  # port is the docker container connections
  smtp_server.ehlo()
  # smtp_server.starttls()
  # smtp_server.login('username', 'password')
  smtp_server.send_message(my_email)
  print("Email was sent!")