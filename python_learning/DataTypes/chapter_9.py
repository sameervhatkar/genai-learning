#Learning List

nums = [43, 56, 78, 19, 20, 15]
print(nums)

nums.append(34)
print(nums)

nums.remove(56)
print(nums)

nums.insert(6, 21)
print(nums)

nums.pop()
print(nums)

nums.reverse()
print(nums)

nums.sort()
print(nums)

maxi = max(nums)
print(maxi)

mini = min(nums)
print(mini)

ele = ['a', 'b', 'c', 'd']
nums.extend(ele)
print(nums)

#Opertor Overloading
nums = [43, 56, 78, 19, 20, 15]
numsEle = nums + ele   #this is operator overloading, instead of adding we can combine 2 lists
print(numsEle)

strong_brew = ["black_tea", "water"] * 3
print(f"Strong brew {strong_brew}")
#output Strong brew ['black_tea', 'water', 'black_tea', 'water', 'black_tea', 'water']
