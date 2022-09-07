from checker import is_primitive_root
while True:
    print("Input g (primitive root): ")
    try:
        g = int(input())
    except ValueError:
        print("Invalid")
    print("Input p (prime number): ")
    try:
        p = int(input())
        print(is_primitive_root(g, p))
    except ValueError:
        print("Invalid")
