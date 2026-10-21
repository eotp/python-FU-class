xnew = np.linspace(start=0, stop=10, num=200)
# defaut uses linear interpolation
f1 = interp1d(x, y)


# specifying a cubic interpolation
f2 = interp1d(x, y, kind='cubic')

# quadratic Interpolation
f3 = interp1d(x, y, kind='quadratic')

# apply interpolation algorithm
inter1 = f1(xnew)
inter2 = f2(xnew)
inter3 = f3(xnew)

# plot results
fig, ax = plt.subplots(figsize=(12,4))
ax.plot(x, y, 'o', label='data')
ax.plot(xnew, inter1, linestyle='-', label='linear')
ax.plot(xnew, inter2 , linestyle='--', label='cubic')
ax.plot(xnew, inter3 , linestyle='--', label='quadratic')
ax.legend();