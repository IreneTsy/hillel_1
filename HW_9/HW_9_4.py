
data = [
 {'country': 'UA', 'item': 'socks', 'name': 'Alisa', 'price': 15},
 {'country': 'UA', 'item': 'socks', 'name': 'Alisa', 'price': 25},
 {'country': 'US', 'item': 'pencil', 'name': 'Ben', 'price': 95},
 {'country': 'UA', 'item': 'pencil', 'name': 'Alisa', 'price': 45},
 {'country': 'GB', 'item': 'socks', 'name': 'Oleg', 'price': 100},
 {'country': 'US', 'item': 'pencil', 'name': 'Ben', 'price': 10}
]

st_worker = {data[i]['name'] for i in range(len(data))}
print(st_worker)

lst = []
name = [data[i]['name'] for i in range(len(data))]
price = [data[i]['price'] for i in range(len(data))]
#print(name, price)
for i in zip(name, price):
    lst.append(i)
#pprint.pprint(lst)
d = {}
[d.__setitem__(first, d.get(first, 0) + second) for first, second in lst]
print(d)