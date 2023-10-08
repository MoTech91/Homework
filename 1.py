
##Normal list##
# _____________________#
# Names=['mahmoud,farida,ali,hassan,mohamed,khaled,taha']
# for i in Names:
#     new_list=[i.replace('a',' ')]
# print(new_list)

##List comprehensio##
#___________________#
# Names=['mahmoud,farida,ali,hassan,mohamed,khaled,taha']
# new_list=[i.replace('a','') for i in Names]
# print(new_list)

##Functional Programing##
#___________________#
# Names=['mahmoud,farida,ali,hassan,mohamed,khaled,taha']
# def Remov_letter(name):
#     return name.replace('a',' ')

# new_list=list(map(Remov_letter,Names))
# print(new_list)


#$$$$$2.3$$$$$$$
####NORMAL_LIST####
Names=['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
new_list=[]

# new_list= [Names.pop()]
# print(new_list)
# print(Names)

####LIST COMPREHENSION####


# new_list=[n for n in Names if len(n)==4]
# print(new_list)


####FUNCTIONAL PROGRAMING####
def remmove(x):
    for n in Names:
        if x=='taha':
            return x
new_list=filter(remmove,'taha')
print(list(new_list))


    




