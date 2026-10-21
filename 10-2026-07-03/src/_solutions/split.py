df_example  = pd.DataFrame({"key" : ["A", "B", "C", "A", "B", "C"],
                    "data" : [1, 2, 3, 4, 5, 6]
                   })


df_example.groupby('key').sum()