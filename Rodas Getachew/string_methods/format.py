#9: format()
text: str = '{subject} is doning: {action}.'
print(text.format(subject='cat', action='meow'))

text: str = '{} is doing: {}.' # alternative
print(text.format('cat', 'meow'))