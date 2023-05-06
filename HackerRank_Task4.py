'''
You are the manager of a supermarket.
You have a list of  items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.
#The first line contains the number of items, .
#The next  lines contains the item's name and price, separated by a space.

sample_output:

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
'''

from collections import OrderedDict

items = OrderedDict()

n = int (input())


for count in range(n):
    item_name,item_price =input ().rsplit(maxsplit=1)
    items[item_name]=items.get(item_name,0) + int(item_price)
for item_name, item_price in items.items():
    print(f"{item_name} {item_price}")
