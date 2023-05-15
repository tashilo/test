import re

def find_all_phones(text):
    result = re.findall(r"(\+380\(\d{2}\)\d{3}-\d{2}-\d{2}|\+380\(\d{2}\)\d{3}-\d{1}-\d{3})", text)
    return result

text = 'Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787'
print(find_all_phones(text))


