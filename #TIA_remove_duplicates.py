def remove_duplicates(string):
    duplicates=[]
    alpha='abcdefghijklmnopqrstuvwxyz'
    for i in alpha:
	if string.count(i)>1:
		duplicates.append((string.count(i)))
    unique = "".join(sorted(list(set(string))))
    dup_removed = sum(duplicates) - len(duplicates)
    return (unique,dup_removed)