def fizzbuzz(n):
    for i in range(1, n + 1):
        three = i % 3 == 0
        five = i % 5 == 0
        msg = ""
        if three:
            msg = "Fizz"
        if five:
            msg += "Buzz"
        else:
            if not msg:
                msg = "{}".format(i)
        print(msg)


fizzbuzz(30)