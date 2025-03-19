#DemoStr.py
#문자열 메서드 연습
strA = "python is very powerful"
strB = "파이썬은 강력해"
print(len(strA))
print(len(strB))
print(strA.capitalize())

data = "  spam and ham  "
result = data.strip()
print(data)
print(result)
result = result.replace("spam", "spam and egg")
print(result)
lst = result.split(" ")
print(lst)
result = ":".join(lst)
print(result)

#정규표현식
import re

result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())

result = re.search("apple", "this is apple")
print(result)
print(result.group())

result = re.search("\d{4}", "올해는 2025년입니다")
print(result)
print(result.group())
