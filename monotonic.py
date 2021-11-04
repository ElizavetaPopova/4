#Вводим функцию
print("Введите элементы списка в строчку:")
num = input()
nums = num.split()
nums = list(map(int, nums))
f = len(nums)
print('nums =', nums)
#Используем след. синтаксис 
def is_monotonic(nums):
    k = 1
    counter = 0
    for k in range(1,f):
        if min(nums) == nums[0]:
            if nums[k] >= nums[k-1]:
                continue
            else:
                counter += 1
        elif max(nums) == nums[0]:
            if nums[k] <= nums[k-1]:
                continue
            else:
                counter += 1
        else:
            return False
    if counter == 0:
        return True
    else:
        return False

print(is_monotonic(nums))
