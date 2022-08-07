###### lists helper functions 
myFriends = ['belal','mostafa','ahmed', 'mahamad','ali', 'hend']
myweapons=['m4','akm','osey','krosy','pekessy']
newFriends =['joe', 'jack']
# 1. myFriends.extend()  لاضافة ليست جيديده على الليست القديمة 
myFriends = myFriends + newFriends

print(myFriends)

#myfrieds.pop() لحذف اخر عنصر من الليست 
myFriends.pop()
print(myFriends)

# myfriends.append() لاضافة عنصر جديد ف اخر الليست 
myFriends.append('jack')
print(myFriends)

# myfriends.insert(position, value) لاضافة عصنر ولكن ف اي مكان ف الليست 

myFriends.insert(2, 'youssef')
print(myFriends)
myFriends.insert(0, 'youssef')
print(myFriends)

#myfriends.remove(value)
myFriends.remove('youssef')
print(myFriends)
myFriends.remove('youssef')
print(myFriends)

# myfriends.count()  

print(myFriends.count('ahmed'))
myFriends.append('ahmed')
print(myFriends.count('ahmed'))
print(myweapons[4])



























