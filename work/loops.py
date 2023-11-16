
# while loop
i = 1
while i<= 10:
    print(i)
    print(i * '*')
    i = i+ 1



numbers = [1,2,3,4,5]

for item in numbers:
    print(item)

#------------------
print("----------------")
i= 0
while i< len(numbers):
    print(numbers[i])
    i= i+1


# range object

print("----------------")
for number in range(5):
    
    print(number)


numbers = range(5)
print("----------------")
for number in numbers:
    
    print(number)

numbers = range(5, 10)
print("----------------")
for number in numbers:
    
    print(number)


numbers = range(5, 10, 2)
print("----------------")
for number in numbers:
    
    print(number)