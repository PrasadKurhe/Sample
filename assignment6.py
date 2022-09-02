#Write a Python program to remove all elements from a given list present in another list using lambda.
l1=[1,2,3,4,5,6]
l2=list(map(lambda x:x ,l1))
print(l2)