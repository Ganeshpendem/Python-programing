height=input("Enter the persons heights: ")
a=height.split()
count=0
for x in a:
    count+=1
print(count)
for i in range(count):
    a[i]=int(a[i])
total=0
for person in a:
    total+=person
avg=total/count
print(round(avg))