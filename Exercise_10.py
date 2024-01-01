his_name=input("Enter His name: ")
her_name=input("Enter her name: ")
combine_name= his_name + her_name

lower_case_string= combine_name.lower()

t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e1=lower_case_string.count("e1")

true=t+r+u+e1

l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e2=lower_case_string.count("e2")

love=l+o+v+e2

love_score=int(str(true*10)) +int(str(love))



if 10<= love_score <=29:
    print(f"your love score is {love_score}, and you have low score")
elif 30<= love_score <=50:
    print(f"Your love score is {love_score}, and you have a average score")
else:
    print(f"Your love score is {love_score}, and you have best score")


print(love_score)
