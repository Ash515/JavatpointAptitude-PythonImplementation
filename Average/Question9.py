'''
9) The average age of the committee of 10 members is 40 years. A member of age 52 retires and a new member of age 38 takes his place. What is the average age of the present committee?
38.6 years
33.5 years
35.5 years
37.5 years
'''
members=int(input("Enter the total members in commite: "))
Average_age=int(input("Enter the average age of the commitee members:"))
Expired_member_age=int(input("Enter the retired person age:"))
replacable_person_age=int(input("Enter the replacable person age:"))
step1=members*Average_age
step2=Expired_member_age-replacable_person_age
result=(step1-step2)/10
print("The average age of the present committee is",result,"years")

#Output=>The average age of the present committee is 38.6 years
