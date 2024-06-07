from operator import itemgetter

users=[

	{'fname':'joker', 'lname':'hacker'},
	{'fname':'kuna', 'lname':'rakulna'},
	{'fname':'guna', 'lname':'doer'},
	{'fname':'aaker', 'lname':'hacker2'},

]

for x in sorted(users, key = itemgetter('fname')):
	print(x)