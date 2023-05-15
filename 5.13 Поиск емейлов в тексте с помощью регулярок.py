import re

def find_all_emails(text):
    result = re.findall(r"[a-zA-Z][a-zA-Z0-9._-]{1,}@[a-zA-Z]{2,}\.[a-zA-Z]{2,}", text)
    return result

print(result)


