"""
Given an html, find all emails that lie on it and output them
into a csv
"""

import re

email_regex = re.compile(r'[0-9a-zA-Z._-]+@[a-zA-Z]+(?:\.[a-zA-Z]+)*\.[a-zA-Z]{2,}')

emails = []
with open("html_input.html") as htmlfile:
    for html_line in htmlfile:
        emails.extend(email_regex.findall(html_line))

# if repeated email found, just dedup
emails = list(set(emails)) # dedup
emails.sort()

with open("output.csv", '+w') as outputfile:
    outputfile.write("emails\n")
    for email in emails:
        outputfile.write(f"{email},\n")
