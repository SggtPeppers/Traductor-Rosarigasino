pyg = 'gas'

original = input('Enter a Word:')

if len(original) > 0 and original.isalpha():
	word = original.lower()
	first = word[0]
	new_word = word[0:2] + pyg + word[1] + word[2:5]
	print(new_word)
else:
	print('empty')

