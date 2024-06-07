import re

sen = "This is my computer. I work technoBrain"

pattern = re.compile(r'[cor]') # Example: [a-zA-Z] [0-9]

matches = pattern.finditer(sen)

for match in matches:
	print(match)

