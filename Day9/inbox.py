import imaplib
import email

host = 'imap.gmail.com'

username = 'test1@gmail.com'
password = 'test1password'

def get_inbox():
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username,password)
    mail.select("inbox")

    _,search_data = mail.search(None,'UNSEEN')
    my_messages = []
    for num in search_data[0].split():
        email_data = {}
        _,data = mail.fetch(num,'(RFC822)')
        _,b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject','to','from','date']:
            print("{}: {}".format(header,email_message[header]))
            email_data[header] = email_message[header]
        for part in email_message.walk():
            try:
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True)
                    email_data['body'] =  body.decode() 
                elif part.get_content_type() == 'text/html':
                    html_body = part.get_payload(decode=True)
                    email_data['html_body'] =  html_body.decode() 
                    read = True
            except:
                read = False
                print(read)
        my_messages.append(email_data)
    return my_messages
if __name__ == "__main__":
    my_inbox = get_inbox()
    print(my_inbox)