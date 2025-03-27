# 10: format_map()
coordinates: dict = {'x':10, 'y': -5}
text: str = 'coordinates: ({x}, {y})'
print(text.format_map(coordinates))
