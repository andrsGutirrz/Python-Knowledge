# Email Module

## What does it do?
1. Send text/html as a string and it can render it
2. Send attached file with text/html

## Installation
```shell
pip install git+https://github.com/andrsGutirrz/Email_Module.git  
```

## Usage
```python
serverLink = 'smtp.gmail.com:587'  
password = 'xxxxx'  
sender = 'sxxxx@gmail.com '  
subject = 'Your subject'  
receivers = ['list_of_Address' ]  
body = 'your body msg'  
      
route =r'rout_to_file'  
filename = 'name_of_file_with_extension'  
```

#### With attached file
```python
# Mandatory "rb" mode
with open(route,"rb") as f:  
    send_email_attached(serverLink, password, subject, body, sender, receivers, f,filename)
```

#### or simple text/html body
```python
send_email(serverLink,password,subject,body,sender,receivers)
```

## Example
```python
from email_module import emailSender as em

serverLink = 'smtp.gmail.com:587'
senderPassword = 'xxxxx'
sender = 'sxxxx@gmail.com '
subject = 'Your subject'

receivers = [
    'a@gmail.com',
    'b@gmail.com',
    'c@hotmail.com',
    'd@yahoo.com',
]

body = '<p>ulla pariatur. <b>Excepteur</b> sint occaecat cupidatat</p>'
      
route ='C:\\myfile.pdf'
filename = 'myfile.pdf'

with open(route,"rb") as f:
    em.send_email_attached(serverLink, senderPassword, subject, body, sender, receivers, f,filename)
```