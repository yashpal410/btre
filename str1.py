str1 = "Ramu is a gooda boy"
str2 = "hello {0}, You have {1:4.3f} balance"
str3= "Rahul"
str4="R1hul"
str5="12345"
str6=" dssf c "
str7='abc'
str8='def'
str9='abd'
str10='abc'
str11='abcdef'
str12 = "Ramu, is, a, gooda, boy"
str14= 'this is\n a docstring'
point = {'x':4,'y':-5, 'z': 0}
print('format_map {x} {y} {z}'.format_map(point))
print("capitalize",str1.capitalize())
print("center",str1.center(20,'*'))
print("center",str1.center(20))
print("casefold",str1.casefold())
print("count",str1.count('a'))
print("endswith",str1.endswith('boy'))
print("endswith",str1.endswith('a',4,9))
print("expandtabs",str1.expandtabs())
print("encode",str1.encode())
print("find",str1.find('a'))
print("index",str1.index('a'))
print("find",str1.find('p'))
#print("index",str1.index('p'))
print("format",str2.format("Rahul",240.47449))
print("isalnum",str3.isalnum(),str4.isalnum(),str5.isalnum())
print("isalpha",str3.isalpha(),str4.isalpha(),str5.isalpha())
print("isdecimal",str3.isdecimal(),str4.isdecimal(),str5.isdecimal())
print("isdigit",str3.isdigit(),str4.isdigit(),str5.isdigit())
print("isidentifier",str3.isidentifier(),str4.isidentifier(),str5.isidentifier())
print("islower",str3.islower(),str4.islower(),str5.islower())
print("isupper",str3.isupper(),str4.isupper(),str5.isupper())
print("istitle",str3.istitle(),str4.istitle(),str5.istitle())
print("isnumeric",str3.isnumeric(),str4.isnumeric(),str5.isnumeric())
print("isprintable",str3.isprintable(),str4.isprintable(),str5.isprintable())
print("isspace",str3.isspace(),str4.isspace(),str5.isspace())
print("lower",str1.lower())
print("upper",str1.upper())
print("swapcase",str1.swapcase())
print("join",str4.join(str5))
print("strip",str6.strip())
print("strip",str6.strip('cf'))
print("strip",str6.strip(' cf '))
print("strip",str6.strip(' cf'))
print("lstrip",str6.lstrip('cf'))
print("lstrip",str6.lstrip(' cf'))
print("rstrip",str6.rstrip('cf'))
print("rstrip",str6.rstrip('cf '))
print("partition",str1.partition(' a '))
print("partition",str1.partition('is'))
print("rpartition",str1.rpartition('is'))
#print("maketrans",str10.maketrans(str7)) if no of param is 1 then param must be dict
print("maketrans",str10.maketrans(str7,str8))
print("maketrans",str10.maketrans(str7,str8,str9))
print("translate",str11.translate(str10.maketrans(str7,str8,str9)))#
print("replace",str1.replace('is','was'))
print("replace",str1.replace('a','an',2))
print("rfind",str1.rfind('a'))
print("replace",str1.rindex('a'))
print("rfind",str1.rfind('amd'))
#print("replace",str1.rindex('amd'))
print("split",str12.split(","))
print("rsplit",str12.rsplit(","))
print("startswith",str1.startswith('Ra'))
print("startswith",str1.startswith('Ra '))
print("title",str1.title())
print("zfill",str1.zfill(40))
print("splitlines",str14.splitlines())
print(str1)





