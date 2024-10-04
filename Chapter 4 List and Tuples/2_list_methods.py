friends = ["Tejas","Aakash","Rohan",45,67,123.123,"Lol"]

print(friends)

friends.append("Harry")
print(friends)

nums = [1,2,3,-1,-2,-3]
nums.sort()
print(nums)

nums.reverse() # this reverses the list, returns None
print(nums)

nums.insert(3,123) # name.insert(index,value)
print(nums)


print(nums.pop(3))#123

# pop works this way, it returns the value when the function call is made and it take index as an argument
# gives index out of range as an error if index is greater than size of the list
print(nums)


print(nums.remove(1)) # removes the element if present.
print(nums)


