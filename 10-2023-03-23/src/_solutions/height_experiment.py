heights = hf.sample_body_heights(200000)
xbar = np.mean(heights)
std = np.std(heights)
print(f'The mean of the sample is {xbar}')
print(f'The standard deviation of the sample is {std}')
fig, ax = plt.subplots()
ax.hist(heights, bins=25);