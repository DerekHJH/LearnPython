import pandas as pd


#Series == list
'''
a = pd.Series([2, 4, 6, 8])
#print(a)
#print(a[0])
#print(a[1: 3])
a = pd.Series([2, 4, 6, 8], index = list("abcd"))
#print(a)
#print(a[0])
#print(a[0: 3])
#print(a['a': 'c']) #Both left closed and right closed
a = pd.Series({'a': 100, 'b': 200, 'e': 300})
i = "a b c d".split()
v = [2, 4, 5, 7]
t = pd.Series(v, index = i, name = "col_name")
print(t['a'])#print both of the corresponding values
print(t.index)
a = pd.Series(v, index = v) #In this case 0-3 index cannot be used
'''

#More about index
'''
val = [2, 4, 5, 6]
ii = range(10, 14)
s0 = pd.Series(val)
s1 = pd.Series(val, index = ii)
idx = "hello the cruel world".split()
t = pd.Series(val, index = idx)
#print("s0", "*" * 11)
#print(s0.iloc[0])
#print(s0.loc[0])
#print(s0.iat[3])
#print(s0.at[3])
#with 'i' prefix, it's about position, without 'i' prefix, it's about label
#print("s1", "*" * 11)
#print(s1.iloc[1])
#print(s1.loc[11])
#print(s1.iat[2])
#print(s1.at[12])
#print("t", "*" * 11)
#print(t.ix[1])
#print(t.ix['the'])
#ix can take both position and label
#print(t.ix[['hello', 'the', 'world']]) #extract several pieces of data
#for x in t.iteritems():print(x)
'''

#add and delete
'''
idx = "hello the cruel world".split()
val = range(10, 14)
s = pd.Series(val, index = idx)
print(s)
s = s.append(pd.Series({"this": 9}))
s = s.append(pd.Series({"this": 10})) #Multiple same labels are allowed
s["this"] = 8
print(s)
t = s[s > 11]
print(t) #delete the part where the value is above 11
'''
