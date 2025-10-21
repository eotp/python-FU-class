from itertools import combinations
diets = {"chick_diet1": chick_diet1, 
         "chick_diet2": chick_diet2, 
         "chick_diet3": chick_diet3, 
         "chick_diet4": chick_diet4}

for c in combinations(diets.keys(),2):
    _, p, _ = ttest_ind(diets.get(c[0]), diets.get(c[1]))
    print(f'Combination: {c[0]} vs. {c[1]}: p-value: {p}')