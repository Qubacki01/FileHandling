###
#
#

import email_module

# Read the raw email from the file
with open('email.txt', 'r', encoding='utf-8') as file:
    email_content = file.read()

# Fetch and print the sender, recipient, subject, and body using the functions from emails module
sender = email_module.email_sender(email_content)
recipient = email_module.email_recipient(email_content)
subject = email_module.email_subject(email_content)
body = email_module.email_body(email_content)

# Output the results
print("Sender:", sender)
print("Recipient:", recipient)
print("Subject:", subject)
print("Body:", body)
