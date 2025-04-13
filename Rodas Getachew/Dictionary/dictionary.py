# dictionary = a collection of {key:value} pairs ordered and changeable. No duplicates

capitals= {'USA': 'Washington D.C.',
            'India':'New Delhi',
            'china': 'Beijing',
            'Russia': 'Moscow'}

#print(dir(capitals))
#print(help(capitals))

#print(capitals.get('India'))


#if capitals.get('Russia'):
#  print('That capital exists')
#else:
#  print('That capital does not exists')


#capitals.update({'Germany': 'Berlin'})       # we can add new keys pair

#capitals.update({'USA':'Berlin'})            # edit keys pair

#capitals.pop('china')                        #to renove a key value pair you can use the pop method

#capitals.popitem()                           #you can remove the letest key value pair

#capitals.clear()


#keys=capitals.keys()

items = capitals.items()

print(items)


