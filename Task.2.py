#tq
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$${2.1}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Names=['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
new_list=[]
#----------------------->>>>>>>>>>>>>>>>>>>>Normal list<<<<<<<<<<<<<<


#-------------------->>>>>>>>>>>>>>>>>>>>>>>List comprehension<<<<<<<<

new_names=[name.upper() for name in Names]
print(new_names)

#----------------------->>>>>>>>>>>>>>>>>Functional Programing<<<<<<<<<

def Capital(x):
    return x.upper()
new_names=map(Capital,Names)

print(list(new_names))
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$${2.2}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#------------------------>>>>>>>>>>>>>>>>>>Normal list<<<<<<<<

for i in Names:
    new_list=[i.replace('a',' ')]
print(new_list)

#----------------------->>>>>>>>>>>>>>>>>>List comprehension<<<<

new_list=[i.replace('a','') for i in Names]
print(new_list)

#----------------------->>>>>>>>>>>>>>>>>Functional Programing<<<<

Names=['mahmoud,farida,ali,hassan,mohamed,khaled,taha']
def Remov_letter(name):
    return name.replace('a',' ')

new_list=list(map(Remov_letter,Names))
print(new_list)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$${2.3}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#----------------------->>>>>>>>>>>>>>>>>>NORMAL_LIST<<<<<<<<<<<<

new_list= [Names.pop()]
print(new_list)
print(Names)

#-------------------->>>>>>>>>>>>>>>>>>>>LIST COMPREHENSION<<<<<<

new_list=[n for n in Names if len(n)==4]
print(new_list)

#----------------------->>>>>>>>>>>>>>>>>Functional Programing<<<<

def remmove(x):
    for n in Names:
        if x=='taha':
            return x
new_list=filter(remmove,Names)
print(list(new_list))

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$${2.4}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#----------------------->>>>>>>>>>>>>>>>>>>>Normal list<<<<<<<<<<<<<<

for name in Names:
    if name.count('a') >1 and len(name)>2:
        new_list.append(name)
print(new_list)

#-------------------->>>>>>>>>>>>>>>>>>>>LIST COMPREHENSION<<<<<<<<<<

new_list = [name for name in Names if name.count('a') > 1]
print(new_list)
# ----------------------->>>>>>>>>>>>>>>>>Functional Programing<<<<

new_list=list(filter(lambda name: name.count('a')>1, Names))
print(new_list)
    
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$${2.5}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#----------------------->>>>>>>>>>>>>>>>>>>>Normal list<<<<<<<<<<<<<<

for names in Names:
    new_list.append(len(names))
print(new_list)
# -------------------->>>>>>>>>>>>>>>>>>>>LIST COMPREHENSION<<<<<<<<<<

new_list=[(len(names))for names in Names ]
print(new_list)
# ----------------------->>>>>>>>>>>>>>>>>Functional Programing<<<<

def str_len(name):
    return len(name)

result= map(str_len,Names)
print(list(result))

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$${2.6,7,8,9}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


#----------------------->>>>>>>>>>>>>>>>>LIST UNPACKING<<<<<<<<

a,*b=Names
print(a)
print(b)

a,*c,b=Names
print(a,b)

a,b,*c=Names
print(a)
print(b)