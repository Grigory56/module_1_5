immutable_var=1,2.0,5,'record',True,[2,8]
print(immutable_var)
print(type(immutable_var))
#immutable_var[1]=0
mutable_list=[1,2.0,5,'record',True]
print(mutable_list)
print(type(mutable_list))
mutable_list[3]=3.14159
mutable_list[4]='nn'
print(mutable_list)
