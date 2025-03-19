#ask user to input their full name 
user_string = input("input your full name = ")

#use replace to remove whitespaces, store in a variables
straight_string = user_string.replace(" ", "")

#initialize count
count = 0 

#use for loop to iterate through string characters
for i in straight_string:
    
    #add 1 to count for each iteration
    count += 1

#return value of count
print(count)