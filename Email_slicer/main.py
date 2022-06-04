username=""
domain=""
email=input("Introduce the email:")
for x in range(0,len(email)):
    if email[x]=="@":
        break
    else:
        username+=email[x]
for x in range(0,len(email)):
    if email[x]=="@":
        for i in range(x+1,len(email)):
            if email[i]==".":
                break
            else:
                domain+=email[i]


print("The e-mail is:",email)
print("The username is:",username)
print("Domain name is:",domain)