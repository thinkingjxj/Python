import pandas as pd


t = {'id':[1,1,2,3,3,4,5,5],
     'price':[5,6,8,3,4,6,9,5],
     'amount':[1,1,2,1,1,1,2,1],
     'status':['sale','sale','no','no','sale','no','sale','no']}

print(t)

index = {'id', 'price', 'amount'}
t1 = {key:value for key,value in t.items() if key in index}

print(t1)

print(pd.DataFrame(t1))
print(pd.DataFrame(t))


