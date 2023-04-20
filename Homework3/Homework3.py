#Task 16


#import random

#size = int(input('Enter the size of the list: '))
#my_list = [random.randint (0,10) for i in range (size)]
#print (my_list)

#num = int(input('Enter a number you are searching: '))
#count = 0

#for i in my_list:
#    if i == num:
#        count += 1
        
#print(f'Your number occurs {count} times')




#task 18

#import random

#size = int(input('Enter the size of the list: '))
#the_list = [random.randint(1, 10) for i in range(size)]
#print(the_list)

#num = int(input('Enter a number you are searching: '))
#index_value = 0
#min_value = abs(the_list[0] - num)

#for i in range(1, size):
#    temp_value = abs(the_list[i] - num)

#    if temp_value < min_value:
#        min_value = temp_value
#        index_value = i
#print(f'The nearest element to the number "{num}" is the number "{the_list[index_value]}"')



#task 20



#points_table = {1:"AEIOULNSTRÀÂÅÈÍÎĞÑÒ",2:"DGÄÊËÌÏÓ",3:"BCMPÁÃ¨Üß",4:"FHVWYÉÛ",5:"KÆÇÕÖ×",8:"JXØİŞ",10:"QZÔÙÚ"}

#my_word = input("Enter a word: ").upper()
#score = 0

#for i in my_word:
#    for point, value in points_table.items():
#        if i in value:
#            score += point
            
#print(f'You have scored {score} points')
