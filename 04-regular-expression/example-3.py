import re 

# . ^ $ * + ? { } [ ] \ | ( )
#
# Note: These characters have to be escaped when using in Regular Expression Searching

sentence = "In order learn web technologies, please visit www.w3school.com"

pattern = re.compile(r'www\.w3school\.com')

matches = pattern.finditer(sentence)

for match in matches:
	print(match)