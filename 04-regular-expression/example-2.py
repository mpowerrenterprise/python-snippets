import re

sentance = "My name is Gunarakulan, But also call me Guna Joker Hacker Software Engineer"

pattern = re.compile(r'Guna')

matches = pattern.finditer(sentance)

for match in matches:
	print(match)



#####OUTPUT######
'''

<re.Match object; span=(11, 15), match='Guna'>
<re.Match object; span=(41, 45), match='Guna'>


(11, 15) = It is the first occurance that starts from 11 to 15 in the sentance text
(41, 45) = It is the first occurance that starts from 41 to 45 in the sentance text


'''

