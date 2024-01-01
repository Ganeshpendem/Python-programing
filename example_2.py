his_name=input("Give his Name: ")
her_name=input("Give her Name: ")
combine_names=his_name+her_name

low_string=combine_names.lower()

#flames
f=low_string.count("f")
l=low_string.count("l")
a=low_string.count("a")
m=low_string.count("m")
e=low_string.count("e")
s=low_string.count("s")

flames=f+l+a+m+e+s

love_score=(int(flames)*10)
print(love_score)

if 35 <= love_score <=40:
    print(f"Your Love Score is {love_score}, and you have low score.")
elif 41<= love_score <=50:
    print(f"Your Love Score is {love_score}, and you have average score.")
elif 51<= love_score <=100:
    print(f"Your Love Score is {love_score}, and you have Best score. ")
else:
    print(f"Your Love Score is {love_score}, and you have worst score.")

