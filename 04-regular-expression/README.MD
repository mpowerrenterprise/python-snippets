# 04-regular-expression Snippets

## example-1.py

```python

import re

print("\tap") # This will print the text with TAP with the line space since it used \t as ap

print(r"\tap") # This r will prevent the behaviour of r, and will print without the tap line space



```
## output

![Image](media/1.png)



## example-2.py

```python

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





```
## output

![Image](media/2.png)



## example-3.py

```python

import re 

# . ^ $ * + ? { } [ ] \ | ( )
#
# Note: These characters have to be escaped when using in Regular Expression Searching

sentence = "In order learn web technologies, please visit www.w3school.com"

pattern = re.compile(r'www\.w3school\.com')

matches = pattern.finditer(sentence)

for match in matches:
	print(match)

```
## output

![Image](media/3.png)

## example-4.py

```python

import re

sen = "This is my computer. I work technoBrain"

pattern = re.compile(r'[cor]') # Example: [a-zA-Z] [0-9]

matches = pattern.finditer(sen)

for match in matches:
	print(match)



```
## output

![Image](media/4.png)

## example-5.py

```python

import re

sentance = "my phone number is 0756800519"

pattern = re.compile(r'\d') # [0-9] 

instances = pattern.finditer(sentance)

for instance in instances:
	print(instance)


```
## output

![Image](media/5.png)