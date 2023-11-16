#Test1
sentence = input('Please enter a sentence:')
 
lst_sentence = list(sentence)
 
lst_sentence.reverse()
 
for i in lst_sentence:
    print(i,end='')
 
 
#Test3
sentence = input('Please enter the sentence:').split(',')
 
filt_lst = []
 
for i in sentence:
    if i not in filt_lst:
        filt_lst.append(i)
 
print(filt_lst)
 
 
 
 
# #Test4
# import csv
 
# with open('Test.csv', newline='') as csvfile:
   
#   rows = csv.reader(csvfile)
 
#   lst_grades = []  
 
#   for row in rows:
#     lst_grades.append(row)
 
 
  
# lst = list(range(60,101))
 
# print('> 60')
 
# for i in lst_grades:
#     if i not in lst:
#        lst_grades.remove(i)
     
 
 
# print(lst_grades,end='\n')
 
 
 
 
 
 
# #Test2
# a = input('Please enter a number:')
# a = int(a)
# b = 1
# for i in range (1, a+1):
#    b = b * i
# print (b)
 
 
 
# #Test5
# class Person:
#     def age(self):
#         print('12')
#     def name(self):
#         print('Billy')
#     def address(self):
#         print('Taipei')
 
 
# class Student(Person):
#     def StudentID(self):
#         print('4b0g')
#     def major(self):
#         print('Computer Science')
 
 
# student = Student()
 
# student.age()
 
# student.StudentID()