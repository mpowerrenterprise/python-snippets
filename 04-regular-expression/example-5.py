import re

sentance = "my phone number is 0756800519"

pattern = re.compile(r'\d') # [0-9] 

instances = pattern.finditer(sentance)

for instance in instances:
	print(instance)