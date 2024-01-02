import random
names=input("names of the persons: ")
split_names=names.split(" ")
print(split_names)
length_names=len(split_names)
a=random.randint(0, length_names-1)
print(f"{split_names[a]}, will pay the bill today")