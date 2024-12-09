def removeElement(nums, val):
    i=0
    while(i<len(nums)):
        if nums[i] == val:
            print("removing: ", nums[i])
            print("i: ", i)
            i-=1
            nums.remove(val)
        i+=1
    return len(nums), nums

l = [1,2,3,4,5,5,2,2]
v = 2
print(removeElement(l, v))