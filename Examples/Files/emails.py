from email.message import EmailMessage #doesn't allow to send email
import smtplib #sending emails
from string import Template
from pathlib import Path

html_template = Template(Path('./Examples/Files/templates/template.html').read_text())

# print(html_template)

# print(html_template.is_valid())

html_content = html_template.substitute({'name': 'Ripley', 'date': '04/27'}) # this is how you set the values in your template.

my_email = EmailMessage()
print(type(my_email))

my_email['from'] = 'Natalie'
my_email['to'] = 'example@example.com'
my_email['subject'] = "Hello from Python"
# my_email.set_content("Hello! \n I just wanted to say hello!")
my_email.set_content(html_content, 'html')

# needs to be opened and closed like a file
with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
  # port is the docker container connections
  smtp_server.ehlo()
  # smtp_server.starttls()
  # smtp_server.login('username', 'password')
  smtp_server.send_message(my_email)
  print("Email was sent!")