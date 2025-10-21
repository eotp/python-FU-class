a = pd.Series(data1, name ='Column1')

b = pd.Series(data2, name = 'Column2')

a = a[:3]

b = b[:3]

c = pd.concat([a,b], axis = 1)

c.index = ['x','y','z']
c