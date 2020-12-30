'''
8) The average age of 30 boys in a class is 15 years. If we include the age of two teachers the average age increases by 1. Find the sum of ages of the two teachers.
55 years
58 years
62 years
64 years
'''
boys=int(input("Enter the number of boys: "))
boys_age=int(input("Enter the age of boys: "))
inclusion_staffs=int(input("Enter the number of inclusion staffs: "))

age_increses=int(input("Enter the incresing number after inclusion of teo guys:"))
step1=boys*boys_age
step2=(boys+inclusion_staffs)*(boys_age+1)
sum_of_ages_two_staffs=step2-step1
print("The sum of ages of the two teachers",sum_of_ages_two_staffs,"years")

#Output=> The sum of ages of the two teachers 62 years