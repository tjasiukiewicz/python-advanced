
def fibo(index):
    if index == 0:
        return 0
    if index == 1 or index == 2:
        return 1

    else:
        return fibo(index - 1) + fibo(index - 2)

print(fibo(35))
