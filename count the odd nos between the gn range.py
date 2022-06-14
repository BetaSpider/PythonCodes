low=int(input("Enter the low no:"))
high=int(input("Enter the high no:"))

print("The given range is:", low , "and" ,high)
count=0
for i in range(low,high+1):
    
    if i %2!=0:
        count=count+1
print("The total no of odd nos between the give nos is:",count)
        
  
