# Attribute Assignment and Deletion
class Accesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value + 10
        else:
            raise AttributeError(attr + ' not allowed')

X = Accesscontrol()
X.age = 40
print(X.age)
# X.name = 'Bob'
# print(X.name)  wrong





# Emulating Privacy for Instance Attributes: Part 1
class PrivateExc(Exception): pass

class Privacy:
    def __setattr__(self, attrname, value): # On self.attrname = value
        if attrname in self.privates:
            raise PrivateExc(attrname, self) # Make, raise user-define except
        else:
            self.__dict__[attrname] = value # Avoid loops by using dict key
class Test1(Privacy):
    privates = ['name']

class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__dict__['name'] = 'Tom'
if __name__ == '__main__':
    x = Test1()
    y = Test2()
    x.age = 27
    y.age = 30
    print(x.age, y.age)

# String Representation: __repr__ and __str__
class adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        self.data += other
X = adder()
print(X)
print(X.data)
X.__add__(1000)
print(X.data)
X.__add__(1000)
print(X.data)

class addrepr(adder): # Inherit __init__, __add__
    def __repr__(self): # Add string representation
        return 'addrepr(%s)' % self.data # Convert to as-code string
x = addrepr(2)
print(x)


def twoSum(nums, target: int):
    for i in range(len(nums)):
        a = target - nums[i]
        if a in nums:
            for j, value in enumerate(nums):
                if value == a:
                    if i < j:
                        print([i, j])

twoSum([3, 3, 13, 3, 3, 3, 3, 3, 3, 3, 3, 3232, 33, 493, 2999, 1, 23, 1222, 111], 6)

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i < j:
#                     if (nums[i] + nums[j]) == target:
#                         return [i, j]



# Link second Node to third node
a = [1,3,2,5,6,4,9,3,4,6]
b = [12,3,44,55,4,5,6,2,8,10,5,8]
c = sorted(a + b)
l = len(c)
def findMedianSortedArrays(nums1, nums2):
    a = sorted(nums1 + nums2)
    l = len(a)
    if l%2 == 0:
        return (a[int(l/2)-1]+a[int(l/2+1)-1])/2
    else: return a[int((l+1)/2)-1]

print(findMedianSortedArrays([1,2],[3,4]))
a = "dwidjwi"
print(enumerate("dwidjwi"))
[print(i) for (i,j) in enumerate("dwidjwi") if j == a[2]]


# def lengthOfLongestSubstring(s):
#     idx = []
#
#     def index(list):
#         index = []
#         for i in range(len(list)):
#             if list[i] not in index:
#                 index.append(list[i])
#             else:
#                 break
#         return len(index)
#
#     for j in range(len(s)):
#         idx.append(index(s[j:]))
#     return max(idx)
#
# a = "aaaaaaa"
# print(lengthOfLongestSubstring(a))

def lengthOfLongestSubstring(s):
    idx = []

    def index(list):
        index = []
        i = 0
        while i < len(list):
            if list[i] not in index:
                index.append(list[i])
                i = i + 1
            else: break
        return len(index)

    if len(s) != 0:
        for j in range(len(s)):
            idx.append(index(s[j:]))
        return max(idx)
    else:
        return 0

print( lengthOfLongestSubstring("awdwwdwdw"))
# list = "bcs"
# print(list[1])







