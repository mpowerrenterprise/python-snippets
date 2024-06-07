from urllib import request

filepath='http://localhost/k.csv'

def downloadCSVfile(filep):
	response=request.urlopen(filep)
	csv=response.read()
	csv_str=str(csv)
	lines=csv_str.split("\\n")
	dest_url = r'goo.csv'
	fx=open(dest_url,'w')
	for line in lines:
		fx.write(line+"\n")
	fx.close()


downloadCSVfile(filepath)
