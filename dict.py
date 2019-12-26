dict1 = {'a':1,'b':2,'c':3}
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'

vowels = dict.fromkeys(keys, value)
print(vowels)
print("get",dict1.get('a'))
print("items",dict1.items())
print("keys",dict1.keys())
#print("pop",dict1.pop()) pop needs 1 argument
print(dict1)
print("pop",dict1.pop('a'))
print(dict1)
print("pop",dict1.pop('d',4))
print(dict1)
#print("pop",dict1.pop('d')) #keyerror
#print(dict1)
print("popitem",dict1.popitem())
print(dict1)
print("values",dict1.values())
print("setdefault",dict1.setdefault('d',4))
print(dict1)
print("update",dict1.update(vowels),dict1)