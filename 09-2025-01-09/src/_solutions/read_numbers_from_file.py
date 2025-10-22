
my_storage = [] #list()
with open ("../data/interim/my_file.txt", "r") as f:
    for line in f:
        number = float(line.split()[1]) 
        my_storage.append(number)
my_storage
