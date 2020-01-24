##Problem1
s = 'fullstackslp'
print(s[0]) #'f'
print(s[-1]) #'p'
print(s[4:-3]) #'stack'
print(s[-3:]) #'slp'
print(s[-5:-2]) #'cks'
print(s[-12:]) #'Bonus'

##############################
##Problem 2
l = [3,7,[5,[1,4,'hello']]]
# Reassign "hello" to be "goodbye"
l[2][1][2] ='Goodbye'
print(l) #updated list

############################
###Problem 3
d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])


d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1])

#############################
### Problem 4

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
set(mylist)


#############################
### Problem 5
age = 45
name = "Kyle"

# Use print formatting to print the following string:
"Hello my dog's name is Kyle and he looks 45 years old"

print("Hello my dog's name is {} and he looks {} years old".format(name,age))
