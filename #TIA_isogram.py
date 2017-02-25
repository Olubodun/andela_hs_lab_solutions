def is_isogram(word):
	if word==" ":
		return (word,False)
	elif type(word) != str:
		raise TypeError('Argument should be a string')
	else:
		for i in word:
			a=[word.count(x) for x in word]
		return tuple((word,len(word)==sum(a)))		
print is_isogram("")