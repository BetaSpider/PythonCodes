#append()

MyList=[89,85,23,'hello']
print("printing the list:\n",MyList)


MyList.append(2)

print("After appending:\n",MyList)

#extend()
MyList=[89,85,23,'hello']
print("printing the list:\n",MyList)


MyList.extend([2,'Welcome','hi'])

print("After using extend function:\n",MyList)



#insert()
MyList=[89,85,23,'hello']
print("printing the list:\n",MyList)

#insert the element in 2nd index

MyList.insert(2,'Welcome')

print("After inserting:\n",MyList)


#remove()

MyList=[89,85,23,'hello']
print("printing the list:\n",MyList)


MyList.remove('hello')

print("After removing:\n",MyList)


#pop()

MyList=[89,85,23,'hello']
print("printing the list:\n",MyList)


MyList.pop(2)

print("After removing the 2nd index's value:\n",MyList)

#clear()
MyList=[89,85,23,'hello']
print("printing the list:\n",MyList)


MyList.clear()

print("After clearing the list:\n",MyList)


#del

MyList=[89,85,23,'hello']
print("printing the list:\n",MyList)

del MyList

print("After deleting:\n",MyList)
 
