#28& 29 : maketrnas() & translate()
text: str = 'That is Bacon'
table = text.maketrans('B','😎')

print(table)
print(text.translate(table))