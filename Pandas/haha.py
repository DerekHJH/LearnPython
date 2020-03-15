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
i = "a b c a".split()
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

#functions for Series
'''
idx = "hello the cruel world".split()
val = [1, 2, 3, 4]
t = pd.Series(val, index = idx);
#print(t.get('the'))
#print(t.get_value('the'))
#print(t.get('The'))# If not found, return None
#print(t.get_value('The'))#Error occurs and do not use get_value for newer version of python
s = pd.Series([9, 9, 9, 9], index = idx)
#print(t.add(s))#Add the value which has the same label
#print(t + 9)
#print(t.append(s))#Do not add together values with the same label
t = pd.Series([9, None, 5, 8], index = idx)
#print(t.count())#calculate the number of non-None values
#print(t.sort_index())#By default we create a copy --- sort by index 
#print(t.sort_values(inplace = True))#We change the original series
#print(t)
#print(t.reset_index())
#print(t.reset_index(drop = True))#remove original index
#print(t)
idn = "hello python nice world".split()
#print(t)
#print(t.reindex(idn))
#print(t.reindex(idn, fill_value = -1))
#print(t)
'''

#statistical functions for Series
'''
idx = "hello the cruel world".split()
val = [1, 2, None, 3]
t = pd.Series(val, index = idx)
#print(t.sum())#treat None as 0
#print(t.mean()) #by default skipna = True, do not count None
#print(t.mean(skipna = False))
t = pd.Series([1, 2, 3, 4], index = idx)
#print(t.quantile())
#print(t.quantile(0.5))
#print(t.quantile(0.25))
#print(t.quantile(0.75))
#print(t.describe())#Boss!! run for it
#print(t.max())#and alsi t.min()
#print(t.idxmax())#return the index of the max number
#print(t.var())#the denoinator is n - 1
#print(t.std())
#print(t.mad()) #mean absolute deviation and the denominator is n
'''

#statistical functions for Series 2
'''
idx = "hello the cruel world".split()
val1 = [1, 2, 3, 4]
x = pd.Series(val1, index = idx)
val2 = [5, 6, 7, 8]
y = pd.Series(val2, index = idx)
#print(x.corr(y))#covariance and the denominator is n - 1
#kert and skew functions are not presented here
print(x)
print(x.cumsum())#prefix sum
print(x.cumprod())#prefix product
print(x.cummin())
'''

#Dataframe --- 2D --- each column is a Series








