fruits=['apples','ovacadoes','bananas','mangoes','cherry']
print(fruits)

fruits=['apples','ovacadoes','bananas','mangoes','cherry']
print(len(fruits))

#list can be of any data type:
list1=['apples','ovacadoes','bananas']
list2=[1,2,3,4,5]
list3=[True,False,True]

print(list1)
print(list2)
print(list3)

#a list can contain different data types
list=['kinuthia',34,True, 40,"Male"]
print(list)

#access list items
list=['apples','banana','cherry']
print(list[1])
 #negative indexing(-1 refers to the last term ,-2 refers to the second last)
list=['apples','banana','ovacado']
print(list[-1])
 #range of indexes
list=['appples','mangoes','bananas','paw paw','ovacadoes','melons','oranges']
print(list[2:5]) 
print(list[:4])
print(list[2:])
print(list[-4:-1])


list=['apples','ovacado','paw paw','banana']
if 'banana' in list:
    print("yes, 'banana', is in the list")

list=['apple','banana','cherry','oranges','kiwi','mango']    
list[1]='sprite'
print(list)

list[1:3]=['blackcurrant','watermelon']
print(list)

list=['apple','banana','cherry','oranges','kiwi','mango']    
list[1:2]=['blackcurrant','watermelon']
print(list)

#to insert a list item at a specified index, use the insert() method:  
list=['apples','ovacado','paw paw','banana']
list.insert(2,'watermelon')

#to add an item to the end of the list ,use the append() method:
list=['apples','banana',"cherry"]
list.append("oranges")
print(list)

fruits=['apples','banana','oranges']
proteins=['meat','eggs','milk']
fruits.extend(proteins)
print(fruits)

list=['apples','oranges','banana']
stuple=["kiwi","orange"]
list.extend(stuple)
print(list)

#remove() method
fruits=['apples','banana','mangoes']
fruits.remove('banana')
print(fruits)

fruits=['apples','banana','mangoes','ovacado','banana','paw paw']
fruits.remove('banana')
print(fruits)

#The POP() method removes the specified index 
fruits=['apples','ovacadoes','oranges','pineapples']
fruits.pop(0)
print(fruits)
  #if you do not specify the index, the pop() removes the last item.
fruits=['apples','ovacadoes','oranges','pineapples']
fruits.pop()
print(fruits)


#DEL keyword also removes the specified index:
proteins=['meat','eggs','milk','liver']
del proteins[2]
print(proteins)
  #del keyword can completely delete the list
#proteins=['meat','eggs','milk','liver']
#del proteins 
#print(proteins)

#CLEAR() method empties the list:
proteins=['meat','eggs','milk','liver']
proteins.clear()
print(proteins)