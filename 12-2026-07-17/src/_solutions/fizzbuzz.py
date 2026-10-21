for i in range(100):
    fizzbuzz = ""
    if i % 3 == 0:
        fizzbuzz = fizzbuzz + "Fizz"
    if i % 5 == 0:
        fizzbuzz = fizzbuzz + "Buzz"
    if len(fizzbuzz) > 0:
        print(fizzbuzz)
    else:
        print(i)