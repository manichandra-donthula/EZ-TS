l=[]
s=str(input("Enter parenthesis: "))
mapp = {"(":")", "[":"]", "{":"}"}
if (len(s)%2==0):
    for c in s:
        if (c in mapp.keys()):
            l.append(c)
        elif (c in mapp.values()):
            if ((c==")" and l[-1]=="(") or (c=="]" and l[-1]=="[") or (c=="}" and l[-1]=="{")):
                l.pop(-1)
    if (len(l)!=0):
        print("Not Valid Parenthesis!")
    else:
        print("Valid Parenthesis!")
else:
    print("Not Valid Parenthesis!")