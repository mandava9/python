#in class week 4 nums.txt
#Q3

f= open('nums.txt')
nums = f.readlines()
f.close()
#find min and max, total and average
min= max= total = int(nums[0])
for num in nums[1:]:
	num = int(num)
	if num < min:
		min = num
	elif num > max:
		max = num
	total = total + num
count = len(nums)
print("The minumum number is ", str(min))
print("The maximum number is ", str(max))
print("The toatl of the numbers is ", str(total))
print("The average numbers is ", str(round((total/count),1)))
