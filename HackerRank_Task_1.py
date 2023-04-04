from collections import Counter

no_of_shoe = int(input('shoes num'))

shoe_size_list = Counter(map(int, input('shoes size list').split()))

no_of_customers = int(input('no_of_customers'))

earned = 0

for i in range(no_of_customers):
    size, price = map(int, input('size and price').split())
    if (shoe_size_list[size]):
        earned += price
        shoe_size_list[size] -= 1


print(earned)
print(shoe_size_list)
