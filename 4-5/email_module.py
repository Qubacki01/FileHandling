###
#
#

import re

def email_sender(email_content):    # Function to get sender email
    match = re.search(r"From:\s+<(.+)>", email_content)     
    if match:
        return match.group(2)
    return None


def email_recipient(email_content):  # Function to get receiver email
    match = re.search(r"To:\s+<(.+)>", email_content)   # <(.+)> - gets all between <>
    if match:
        return match.group(2)
    return None


def email_subject(email_content):   # Function to get email subject
    match = re.search(r"Subject:\s+(.+)", email_content)
    if match:
        return match.group(1)
    return None


def email_body(email_content):  # Function to get email body
    match = re.search(r"\n\n(.*)", email_content, re.DOTALL)    # (.*) - gets all after \n incl lines
    if match:
        return match.group(1)
    return None
