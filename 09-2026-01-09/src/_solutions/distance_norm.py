def distance_norm(a,b):
    return norm.ppf(b, loc=0, scale=1) - norm.ppf(a, loc=0, scale=1)

print(distance_norm(0.999,0.9999))

print(distance_norm(0.599,0.5999))