from collections import OrderedDict

dct = OrderedDict({'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5})
print(dct)
print(id(dct))

dct.move_to_end(key='one')
dct.move_to_end(key='five', last=False)
del dct['two']
dct.update(three=3.0)
dct['new_key'] = 'new_value'

print(id(dct))
print(dct)
