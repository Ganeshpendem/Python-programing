a=[1,1,1]
b=[1,1,1]
c=[1,1,1]
x=[a,b,c]
print(f"{a}\n{b}\n{c}")
z=input("enter the position number where you want to store your money: ")
row_number=int(z[0])
column_number=int(z[1])
row_selected=x[row_number-1]
row_selected[column_number-1]='X'
print(f"{a}\n{b}\n{c}")