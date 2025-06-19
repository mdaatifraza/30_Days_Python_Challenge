# Regular expression
import re

user_input = input("Please enter the email")
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.+(com|in)"

if re.search(pattern, user_input):
    print(f'✔️Valid email')
else:
    print(f'❌Invalid email')