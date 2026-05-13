# x= "abdul"
# for ch in x:
#     print(ch * 5)
# print()
# n=5
# for i in range(n):
#     for j in range(n):
#         print("*", end="")
#     print()
# print()  

# n=5
# for i in range(n):
#     for j in range(n):
#         print(i, end=" ")
#     print()
# print()  


# n=5
# for i in range(n):
#     for j in range(n):
#         print(j, end=" ")
#     print()
# print()


# n=5
# for i in range(n):
#     for j in range(n):
#         print(n-i,end=" ")    
#     print()    
# print()
# n=5
# for i in range(n):
#     for j in range(n):
#         print(n-j,end=" ")    
#     print()    
# print()


# n=5
# for i in range(n):
#     for j in range(n):
#         if j==0 or i ==n-1 :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  
#     print()          
# print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j ==n-3 :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  
#     print()          
# print()


# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j ==n-3 :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  
#     print()          
# print()


# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j ==0 or i== n-1 or j== n-1 :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  
#     print()          
# print()

# n=7
# for i in range(n):
#     for j in range(n):
#         if i==0 or j ==0 or i== n-1 or j== n-1 or i==j :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  
#     print()          
# print()


# n=7
# for i in range(n):
#     for j in range(n):
#         if i==0 or j ==0 or i== n-1 or j== n-1 or i==j or i+j == n-1 :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  
#     print()          
# print()

# n=7
# for i in range(n):
#     for j in range(n):
#         if j == 0 or i== n-1 or i==j :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  
#     print()          
# print()

# n=7
# for i in range(n):
#     for j in range(n):
#         if i==0 or j== n-1 or i==j :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  
#     print()          
# print()

#left angle traingle
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(i+1, end=" ")
#     print()
# print() 


# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print()
# print() 

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(n-i, end=" ")
#     print()
# print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(n-j, end=" ")
#     print()
# print()


#right angle traingle
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i+1):    
#         print(i+1, end=" ")
#     print()
# print()

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i+1):    
#         print(j+1, end=" ")
#     print()
# print()


# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i+1):    
#         print(n-i, end=" ")
#     print()
# print()

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i+1):    
#         print(n-j, end=" ")
#     print()
# print()



#inverse left angle traingle
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(i+1, end=" ")
#     print()
# print() 


# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(j+1, end=" ")
#     print()
# print() 

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(n-i, end=" ")
#     print()
# print() 
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(n-j, end=" ")
#     print()
# print() 

#inverse right angle traingle
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i,n):    
#         print(i+1, end=" ")
#     print()
# print() 


# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i,n):    
#         print(j+1, end=" ")
#     print()
# print() 

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i,n):    
#         print(n-i, end=" ")
#     print()
# print() 

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i,n):    
#         print(n-j, end=" ")
#     print()
# print()

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i):    
#         print(i+1, end=" ")
#     for j in range(i+1):    
#         print(i+1, end=" ")    
#     print()
# print()

#hollow traingles
# n = 7
# for i in range(n):
#     for j in range(i,n):
#         if i ==0 or j ==n-1 or i==j:
#             print("*", end = " ")
#         else:
#             print(" ",end=" ")    
#     print()  
# print() 


# n = 7
# for i in range(n):
#     for j in range(i+1):
#         if i ==0 or i== n-1 or j==0  or i==j :
#             print("*", end = " ")
#         else:
#             print(" ", end=" ")    
#     print()  
# print()


# n = 7
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         if i ==0 or i== n-1 or j==0  or i==j :
#             print("*", end = " ")
#         else:
#             print(" ", end=" ")    
#     print()  
# print()


#pyramid
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i):    
#         print("*", end=" ")
#     for j in range(i+1):    
#         print("*", end=" ")    
#     print()
# print()


# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i):    
#         print("*", end=" ")
#     for j in range(i+1):    
#         print("*", end=" ")    
#     print()
# print()




# n = 7
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         if i == 0 or j== n-1 or j==0  or i==j :
#             print("*", end = " ")
#         else:
#             print(" ", end=" ")    
#     print()  
# print()

#inverse pyramid
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i,n):    
#         print("*", end=" ")
#     for j in range(i, n-1):    
#         print("*", end=" ")    
#     print()
# print()

#left pyramid

#rohmbus
# n=5
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i+1):    
#         print("*", end=" ")
#     for j in range(i,n):    
#         print("*", end=" ")    
#     print()
# print()



# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i):    
#         print("*", end=" ")
#     for j in range(i+1):    
#         print("*", end=" ")    
#     print()
# for i in range(1,n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i,n):    
#         print("*", end=" ")
#     for j in range(i, n-1):    
#         print("*", end=" ")    
#     print()
# print()


# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()    
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()    

# print()
# n=5

# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print() 
# for i in range(n):
#     for j in range(i,n-1):
#         print("*",end=" ")
#     print()    
# print()

