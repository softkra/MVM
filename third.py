import json
import re
import time
def sanitize_list(emails):
    if len(emails) > 100:
        print("Invalid list size...")
        return False
    for row in emails:
        if len(row) < 1 or len(row) > 100:
            print("Invalid email size...")
            return False
        if (not bool(re.search('^[a-zA-Z0-9@\.+]*$',row))) or len(re.findall('@',row)) != 1:
            print("Invalid email format...")
            return False
        splitted = row.split("@")
        if len(splitted[0]) == 0 or len(splitted[0]) == 0:
            print("Not allow empty names...")
            return False
        if splitted[0][0] == '+'  or splitted[1][-4:] != '.com':
            print("Invalid email format...")
            return False
    return True
def main():
    print(
        """
        ********************************************************************
            This is the third test.
            You have to put a list of emails
            Example: ["test1@leetcode.com","test2@leetcode.com"]
        ********************************************************************
        """
    )
    data = input("Emails: ")
    if type(data) == str:
        data = json.loads(data)
    #data = ["test1@leetcode.com","test2@leetcode.com"]
    if type(data) == list:
        if sanitize_list(data):
            validated = []
            for row in data:
                name, domain = row.split('@')
                local_name = name.split('+')[0].replace('.', '')
                email = f'{local_name}@{domain}'
                if not email in validated:
                    validated.append(email)
            print("Result: ", len(validated))
        else:
            print("Please validate format data and insert again...")
            time.sleep(2)
            main()
