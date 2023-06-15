print("Enter your email")
e=input()
u=e[:e.index("@")]
d=e[e.index("@")+1:]
print(f'username : {u}'+'\n'+f'domain : {d}')
