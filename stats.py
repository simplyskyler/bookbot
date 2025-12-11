def word_count(text):
	amount = text.split()
	return len(amount)

def number_of(text):
	chars = {}
	for c in text:
		lower = c.lower()
		if lower in chars:
			chars[lower] += 1
		else:
			chars[lower] = 1
	return chars

def sort_with(items):
	return items["num"]

def sort_dct(num_words):
	new_sort = []
	for x,y in num_words.items():
		i = {"char" : x ,"num" : y}
		new_sort.append(i)
		new_sort.sort(key=sort_with, reverse=True)
	return new_sort
