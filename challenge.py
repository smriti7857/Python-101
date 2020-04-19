list1=[]                           #List of positions
list2=[]                           #List of Strings
n=int(input(""))                   #Total no. of strings
for i in range(n):                 #Input for List1
    a=int(input(""))               
    list1.append(a)
for i in range(n):                 #Input for List2
    b=input("")
    list2.append(b)

#creating a dictionary by combinig list1 and list2
res = {}                           
res = {list1[i]: list2[i] for i in range(len(list1))} 

#sortig list1
list1.sort()    

#Creating a list f to specift at what position a particular string was taken                   
f={}                               
f = {list1[i]: list2[i] for i in range(len(list1))} 

#Creating one more list to sort the dictionary res according to the keys
m={}
for key in sorted(res.keys()):
    m[key]=res[key]

#Comparing the length of string with its position and whether there is any change in its position.
for key,value in m.items():
    if key==len(m[key]) and (m[key]!=f[key]): 
        print(m[key].upper())   
    elif key!=len(m[key]) and (m[key]!=f[key]):
        print(m[key].lower())   
    else:
        print(m[key])
      