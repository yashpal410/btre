import re

txt = "The rain inn Spain"
num1 = "124589"
'''
x = re.findall("[arn]",txt)
print("if any letter matches", x)
x = re.findall("[a-n]",txt)
print("if any letter matches b/w", x)
x = re.findall("[^arn]",txt)
print("if other letter matches", x)
x = re.findall("[0123]",num1)
print("if any number matches", x)
x = re.findall("[0-9]",num1)
print("if any num matches b/w", x)
x = re.findall("[0-5][0-8]",num1)
print("if any num matches b/w", x)
x = re.findall("[a-zA-Z]",txt)
print("if alphabet matches", x)
x = re.findall("^The.*Spain$",txt)
print("start and end", x)
x = re.findall("in+",txt)
print("in substr", x)
x = re.findall("in{2}",txt)
print("if in matches", x)
x = re.findall("The | Spain",txt)
print("if either matches", x)
x = re.findall("\AThe",txt)
print("The at start", x)
x = re.findall(r"\bain",txt)
print("ain at end", x)
x = re.findall(r"ain\b",txt)
print("ain at end", x)
x = re.findall(r"ain\B",txt)
print("ain at middle", x)
x = re.findall(r"ain\B",txt)
print("ain at middle", x)
x = re.findall("\d",num1)
print("if any num matches ", x)
x = re.findall("\D",num1)
print("if no num matches ", x)
x = re.findall("\D",txt)
print("if any num matches b/w", x)
x = re.findall("\S",txt)
print("No space", x)
x = re.findall("\s",txt)
print("space", x)
x = re.findall("\w",txt)
print("any char", x)
x = re.findall("\W",txt)
print("no char", x)
x = re.findall("ain\Z",txt)
print("end", x)



print('search')
x = re.search("[arn]",txt)
print("if any letter matches", x)
if x:
	print(True)
else:
	print(False)
x = re.search("[a-n]",txt)
print("if any letter matches b/w", x)
if x:
	print(True)
else:
	print(False)
x = re.search("[^arn]",txt)
print("if other letter matches", x)
if x:
	print(True)
else:
	print(False)
x = re.search("[0123]",num1)
print("if any number matches", x)
if x:
	print(True)
else:
	print(False)
x = re.search("[0-9]",num1)
print("if any num matches b/w", x)
if x:
	print(True)
else:
	print(False)
x = re.search("[0-5][0-8]",num1)
print("if any num matches b/w", x)
if x:
	print(True)
else:
	print(False)
x = re.search("[a-zA-Z]",txt)
print("if alphabet matches", x)
if x:
	print(True)
else:
	print(False)
x = re.search("^The.*Spain$",txt)
print("start and end", x)
if x:
	print(True)
else:
	print(False)
x = re.search("in+",txt)
print("in substr", x)
if x:
	print(True)
else:
	print(False)
x = re.search("in{2}",txt)
print("if in matches", x)
if x:
	print(True)
else:
	print(False)
x = re.search("The | Spain",txt)
print("if either matches", x)
if x:
	print(True)
else:
	print(False)
x = re.search("\AThe",txt)
print("The at start", x)
if x:
	print(True)
else:
	print(False)
x = re.search(r"\bain",txt)
print("ain at end", x)
if x:
	print(True)
else:
	print(False)
x = re.search(r"ain\b",txt)
print("ain at end", x)
if x:
	print(True)
else:
	print(False)
x = re.search(r"ain\B",txt)
print("ain at middle", x)
if x:
	print(True)
else:
	print(False)
x = re.search(r"ain\B",txt)
print("ain at middle", x)
if x:
	print(True)
else:
	print(False)
x = re.search("\d",num1)
print("if any num matches ", x)
if x:
	print(True)
else:
	print(False)
x = re.search("\D",num1)
print("if no num matches ", x)
if x:
	print(True)
else:
	print(False)
x = re.search("\D",txt)
print("if any num matches b/w", x)
if x:
	print(True)
else:
	print(False)
x = re.search("\S",txt)
print("No space", x)
if x:
	print(True)
else:
	print(False)
x = re.search("\s",txt)
print("space", x)
if x:
	print(True)
else:
	print(False)
x = re.search("\w",txt)
print("any char", x)
if x:
	print(True)
else:
	print(False)
x = re.search("\W",txt)
print("no char", x)
if x:
	print(True)
else:
	print(False)
x = re.search("ain\Z",txt)
print("end", x)
if x:
	print(True)
else:
	print(False)
	
	
	
	
x = re.split("[arn]",txt)
print("if any letter matches", x)
x = re.split("[a-n]",txt)
print("if any letter matches b/w", x)
x = re.split("[^arn]",txt)
print("if other letter matches", x)
x = re.split("[0123]",num1)
print("if any number matches", x)
x = re.split("[0-9]",num1)
print("if any num matches b/w", x)
x = re.split("[0-5][0-8]",num1)
print("if any num matches b/w", x)
x = re.split("[a-zA-Z]",txt)
print("if alphabet matches", x)
x = re.split("^The.*Spain$",txt)
print("start and end", x)
x = re.split("in+",txt)
print("in substr", x)
x = re.split("in{2}",txt)
print("if in matches", x)
x = re.split("The | Spain",txt)
print("if either matches", x)
x = re.split("\AThe",txt)
print("The at start", x)
x = re.split(r"\bain",txt)
print("ain at end", x)
x = re.split(r"ain\b",txt)
print("ain at end", x)
x = re.split(r"ain\B",txt)
print("ain at middle", x)
x = re.split(r"ain\B",txt)
print("ain at middle", x)
x = re.split("\d",num1)
print("if any num matches ", x)
x = re.split("\D",num1)
print("if no num matches ", x)
x = re.split("\D",txt)
print("if any num matches b/w", x)
x = re.split("\S",txt)
print("No space", x)
x = re.split("\s",txt)
print("space", x)
x = re.split("\w",txt)
print("any char", x)
x = re.split("\W",txt)
print("no char", x)
x = re.split("ain\Z",txt)
print("end", x)'''
YASH = '5'
x = re.sub("[arn]",YASH,txt)
print("if any letter matches",YASH, x)
x = re.sub("[a-n]",YASH,txt)
print("if any letter matches b/w",YASH, x)
x = re.sub("[^arn]",YASH,txt)
print("if other letter matches",YASH, x)
x = re.sub("[0123]",YASH,num1)
print("if any number matches",YASH, x)
x = re.sub("[0-9]",YASH,num1)
print("if any num matches b/w",YASH, x)
x = re.sub("[0-5][0-8]",YASH,num1)
print("if any num matches b/w",YASH, x)
x = re.sub("[a-zA-Z]",YASH,txt)
print("if alphabet matches",YASH, x)
x = re.sub("^The.*Spain$",YASH,txt)
print("start and end",YASH, x)
x = re.sub("in+",YASH,txt)
print("in substr",YASH, x)
x = re.sub("in{2}",YASH,txt)
print("if in matches",YASH, x)
x = re.sub("The | Spain",YASH,txt)
print("if either matches",YASH, x)
x = re.sub("\AThe",YASH,txt)
print("The at start",YASH, x)
x = re.sub(r"\bain",YASH,txt)
print("ain at end",YASH, x)
x = re.sub(r"ain\b",YASH,txt)
print("ain at end",YASH, x)
x = re.sub(r"ain\B",YASH,txt)
print("ain at middle",YASH, x)
x = re.sub(r"ain\B",YASH,txt)
print("ain at middle",YASH, x)
x = re.sub("\d",YASH,num1)
print("if any num matches ",YASH, x)
x = re.sub("\D",YASH,num1)
print("if no num matches ",YASH, x)
x = re.sub("\D",YASH,txt)
print("if any num matches b/w",YASH, x)
x = re.sub("\S",YASH,txt)
print("No space",YASH, x)
x = re.sub("\s",YASH,txt)
print("space",YASH, x)
x = re.sub("\w",YASH,txt)
print("any char",YASH, x)
x = re.sub("\W",YASH,txt)
print("no char",YASH, x)
x = re.sub("ain\Z",YASH,txt)
print("end",YASH, x)