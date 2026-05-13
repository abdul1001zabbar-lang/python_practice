# x="abdul"
# for ch in x:
#     print(ch,end=" ")
# print()
# y="Banana"
# for i in range(len(y)):
#     print(i,":",y[i])
# print()
# x="ananaB"
# for i in reversed((x)):
#     print(i,end="")
# print()
# x="ananaB"
# y=x[::-1]
# print(y)

# x="ananaB"
# rev =""
# for ch in x:
#     rev = ch + rev
# print(rev)

# z="abdul"
# for i in range(len(z)-1,-1,-1):
#     print(z[i],end=" ")
# print()

# x = "abdul"
# for i in range(len(x)):
#     if i%2==0:
#         print(x[i],end=" ")
# print()
# y = "abdul" 
# for i in range(len(y)):
#     if i%2!=0:
#         print(y[i],end=" ")
# print()

# #anagram

# x="listen"
# y="silent"
# if sorted(x)==sorted(y):
#     print("anagram")
# else:
#     print("not anagram")


# #slpitting a string
# x = "banana"
# print(list(x))

# x="hello world"
# y=x.split()
# print(y)
# x="hello world"
# y=x.split()
# print(y[0])   


# #reverse a string using split and join
# x="hello world"
# y=x.split()
# y.reverse()
# z=" ".join(y)
# print(z)

# x= "abdul zabbar is living in hyderabad"
# print(" ".join(x.split()[::-1]))


# x= "abdul zabbar is living in hyderabad"
# print(" ".join(reversed(x.split())))

# x= "abdul zabbar is living in hyderabad"
# print(" ".join(word[::-1] for word in x.split()))

# x="abdul"
# vowels="aeiou"
# for ch in x:
#     if ch in vowels:
#         print(ch,end=" ")
# print()        

# x="abdul"
# vowels="aeiou"
# for ch in x:
#     if ch not in vowels:
#         print(ch,end=" ")
# print()

# x="Banana"
# vowels="AEIOUaeiou"
# for ch in x:
#     if ch in vowels:
#         print("*",end=" ")
#     else:
#         print(ch,end=" ")
# print()
# x="Banana"
# vowels="AEIOUaeiou"
# for ch in x:
#     if ch in vowels:
#         print(ch,end=" ")
#     else:
#         print("*",end=" ")  

# print()



# x="Banana"
# result=""
# for ch in x:
#     if ch not in result:
#         result+=ch
# print(result)

# x="Banana"
# fre={}
# for ch in x:
#     if ch in fre:
#         fre[ch]+=1
#     else:
#         fre[ch]=1

# print(fre)

# x="Banana"
# fre={}
# for ch in x:
#     fre[ch]=fre.get(ch,0)+1
# print(fre)

# x="swiss"
# for ch in x:
#     if x.count(ch)==1:
#         print(ch,end=" ")
#         break
# print()

# x="swiss"
# for ch in x:    
#     if x.count(ch)>1:
#         print(ch,end=" ")
#         break
# print() 

# x="abdul zabbar"
# print(x.count("a"))

# x="abdul zabbar"
# print(x.replace(" ","-"))

# x="abdul zabbar is living in hyderabad"
# words = x.split()
# result=[]
# for word in words:
#     if len(word)>5:
#         result.append(word)
# print(result)

# x="abdul zabbar is living in hyderabad"
# words = x.split()
# longest=words[0]
# for word in words:
#     if len(word)>len(longest):
#         longest=word
# print(longest)

# x="abdul zabbar is living in hyderabad"
# words = x.split()
# shortest=words[0]
# for word in words:
#     if len(word)<len(shortest):
#         shortest=word
# print(shortest)

# x = "aBDUL"
# result=""
# for ch in x:
#     if ch.isupper():
#         result+=ch.lower()
#     elif ch.islower():
#         result+=ch.upper() 
# print(result) 

# x ="abdul zabbar"
# vowels="AEIOUaeiou"
# vowels_count=0
# consonants_count=0
# for ch in x:
#     if ch in vowels:
        
#         vowels_count+=1
#     else:
        
#         consonants_count+=1
# print("vowels count:",vowels_count)
# print("consonants count:",consonants_count)

# x = "abdul zabbaR"
# print (x.upper())
# print(x.lower())
# print(x.capitalize())
# print(x.title())
# print(x.swapcase())
# print(x.isupper())
# print(x.islower())
# print(x.isalpha())
# print(x.isdigit())
# print(x.isalnum())
# print(x.startswith("a"))
# print(x.endswith("R"))
# print(x.find("d"))
# print(x.count("a"))
# print(x.replace("a","@"))
# print(x.split())
# print(x.split("b"))
# print(x.strip("a"))
# print(x.strip("l"))
# print(x.strip("a").strip("l"))
# print(x.center(20))
# print(x.ljust(20))
# print(x.rjust(20))
# print(x.zfill(20))
# print(x.rfind("d"))
# print(x.rindex("d"))
# print(x.partition("d"))
# print(x.rpartition("d"))
# print(x.isnumeric())
# print(x.isdecimal())
# print(x.isidentifier())
# print(x.isprintable())
# print(x.isascii())

