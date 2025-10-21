import time
for number in range(10):
    count = 10-number
    print(count)
    time.sleep(1)
    if  count == 1:
        print("Engine start!")
