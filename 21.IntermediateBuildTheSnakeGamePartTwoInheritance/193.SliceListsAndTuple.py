
piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(piano_keys[2:5])
# ['c', 'd', 'e']

print(piano_keys[2:])
# ['c', 'd', 'e', 'f', 'g']

print(piano_keys[:5])
# ['a', 'b', 'c', 'd', 'e']

print(piano_keys[2:5:2])
# ['c', 'e']

print(piano_keys[::2])
# ['a', 'c', 'e', 'g']  -  every second item

print(piano_keys[::-1])
#reverce the list
#['g', 'f', 'e', 'd', 'c', 'b', 'a']


piano_tuple = ('do', 're', 'mi', 'fa', 'so', 'la', 'si')

print(piano_tuple[2:5])
('mi', 'fa', 'so')

print(piano_tuple[1:])