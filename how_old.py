from datetime import datetime, timedelta

today = datetime.now()

print("Type in Date of Birth Please?! (YEAR-MONTH-DATE eg:2000-05-14):")

dob = input()

bday = datetime.strptime(dob, "%Y-%m-%d")

diff = today - bday

age = diff.days // 365

print(f"You are {age} years old.")
