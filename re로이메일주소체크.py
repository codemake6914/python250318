import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# 샘플 이메일 주소
emails = [
    "test.email@gmail.com",
    "user@domain.com",
    "user.name@domain.co.in",
    "user_name@domain.com",
    "username@domain.com",
    "username@domain.co",
    "username@domaincom",
    "username@domain.c",
    "username@domain..com",
    "username@domain.corporate"
]

# 이메일 주소 검사
for email in emails:
    if is_valid_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")