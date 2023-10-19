limit = int(input("k: "))
first_number=0
second_number=1
temp=0
first_list=[]
end_sum=0
i=0
while(first_number<limit):
	print(first_number)
	first_list.append(first_number)
	temp=first_number+second_number
	first_number=second_number
	second_number = temp
while(i<len(first_list)):
	if 1%2==0:
		end_sum = end_sum + first_list[1]
	i = i+1
print("sum:", end_sum)