x = ["apple", "banana", "cherry"]

print(x[0])
print("#######################")
for xr in x:
    print(xr)
print ("#######################")
print ("####################### calculator")
print ("####################+")
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))
print ("####################x")

def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1,2,-8]))
print("############################# Max number")
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))
print("############################# Max number")
print("###################################################### length of the list##")
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
print("############################################")
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

for l1 in list1:
    for l2 in list2:
      for l3 in list3:
        print(l1,"=",l2,"=",l3)
print("############################################")
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
print("############################################")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print("############################################")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print("############################################")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
print("############################################")
family =['mom','dad','bro','sis','dog']
family[3]
family[-2]
print("############################################")
print("#################################### slicing")
example =[0,1,2,3,4,5,6,7,8,9]
example[4:8]
example[4:9]
example[-5:0]
example[-5:]
example[:7]
example[:]
example[1:8:2]
example[10:0:-2]
example[::-2]
print("############################################")
print("##############################Change element")
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)
print("###############################")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)
print("###############################")
thislist = ["apple", "banana", "cherry"]

thislist[1:3] = ["watermelon"]

print(thislist)
print("###############################")
thislist = ["apple", "banana", "cherry"]

c

print(thislist) 
print("###############################")
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)                     crud
print("###############################")
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")            crud
print(thislist)
print("###############################")
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
print("###############################")
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
print("###############################")
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
print("###############################")
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
print("###############################")
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
print("###############################")
thislist = ["apple", "banana", "cherry"]
del thislist
print("###############################")
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
print("###############################")
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
print("###############################")
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
print("###############################")
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] 
print("###############################")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 
print("###############################")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist) 
print("###############################")
newlist = [x for x in fruits if x != "apple"] 
print("###############################")
newlist = [x for x in fruits] 
print("###############################")
newlist = [x for x in range(10)] 
print("###############################")
newlist = [x for x in range(10) if x < 5] 
print("###############################")
newlist = [x.upper() for x in fruits] 
print("###############################")
newlist = ['hello' for x in fruits]
print("###############################")
newlist = [x if x != "banana" else "orange" for x in fruits] 
print("###############################")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
print("###############################")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
print("###############################")
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
print("###############################")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
print("###############################")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
print("###############################")
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
print("###############################")
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
print("###############################")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
print("###############################")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
print("###############################")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) 
print("###############################")
print("###############################list methods")
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry") 
print("###############################")
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print("###############################")