'''
Average age of a group of 30 boys is 16 years. A boy of age 19 leaves the group and a new boy joins the group. If the new average age of the group is 15.8 years, find the age of the new boy.
12 years
13 years
14 years
15 years
'''

members=int(input("Enter the total members:"))
dec_wgt=int(input("Enter thee average decresed weight:"))
replace_weight=int(input("Enter the replacable weight:"))
step1=members*dec_wgt
step2=replace_weight-step1
newman_weight=step2
print("The new man weight is :",newman_weight)




