
name = ['jack', 'tom', 'bob', 'simon']
for i in name:
    print(i.title() + ' is a boy.')

print(name.pop())
# Cannot print
print(i.title() for i in name)

print(name.pop(0))
print(name)

del name[0]
print(name)

name.append('simon')
print(name)
name.remove('bob')
print(name)
name.insert(0, 'jack')
print(name)

cars = ['bmw', 'honda', 'audi', 'toyota', 'subaru']
print(cars.sort())
print(cars)
cars.sort(reverse=True)
print(cars)

print('Here is the original list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print('Here is the present list:')
print(cars)

cars.reverse()
print(cars)
print(len(cars))

print(cars[-1])
