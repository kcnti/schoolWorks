nums = int(input('how many: '))
lstName = []

for i in range(nums):
	_all = input("Put name and number: ")
	name = _all
	name = lstName.append(_all[0])
	number = [int(x) for x in _all.split() if x.isdigit()]

query_name = str(input("Who: "))

print(number)
print(lstName)

if query_name in lstName:
	print(sum(number)/len(number))


