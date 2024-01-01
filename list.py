roll_number=[1,2,3,4,5,6,7,8,9,10]
name=["Ganesh", "Karthik", "Kerrthi", "Hema", "Sriram", "Goutham", "Rajesh", "Swami", "Baba", "Chanti"]
mix_list=["Ganesh", 1,2, True, 5.8, 1.7678]
print(roll_number[3])
print(name[3])
print(mix_list)

print(len(roll_number))
print(len(mix_list))
print(roll_number[1:10:3])
print(name[0:4])
numbers=[1,3,8,9,6,4]
print(numbers)
numbers.reverse()
numbers.append(85)
numbers.insert(1,45)
numbers.extend([70,71,72,73])
print(numbers)

#change the number at desired place
print(numbers)

numbers[1:3]=[45,46,47]
print (numbers)
print(max(numbers))
print(min(numbers))

# remove only first occurence element
numbers.remove(9)
print(numbers)

#remove last element in list
numbers.pop()
print(numbers)

#remove desired number frim desired position.
numbers.pop(2)
#2 is the position in list
print(numbers.count(2))