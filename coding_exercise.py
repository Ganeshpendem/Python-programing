numbers=input("Please enter the numbers which you want: ")
a=numbers.split()
count=0
for i in a:
    count+=1
print(count)
for x in range(count):
    a[x]=int(a[x])
#print(a)
max_number=a[0]
for x in a:
    if x > max_number:
        max_number=x
print(f"the max number is: {max_number}")