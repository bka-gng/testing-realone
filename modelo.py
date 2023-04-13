def main():
    n1 = float(input("First number: "))
    n2 = float(input("Second number: "))
    even_odd(n1, n2)

def even_odd(a,b):
    _ = a/b
    print(f"The first number divided by the second number is {_}.")

main()