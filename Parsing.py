import re
def extract_email_addresses(file_path):
    #Read the contents of the file
    with open(file_path)as file:
        text=file.read()
    #define the regular expression pattern to match email addresses
    email_pattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b'
    #Find all email addresses in the text
    email_addresses=re.findall(email_pattern,text)
    return email_addresses
   #Example usage:
file_path = "emails.txt"
   #Replace with the path to your text file:
email_addresses=extract_email_addresses(file_path)
print("Email addresses found in the file:")
for email in email_addresses:
    print(email)
