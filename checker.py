def is_primitive_root(g, p):
    tracker = []
    for i in range(1, p):
        eq = pow(g, i) % p
        if (eq in tracker):
            print(f"{g} is NOT a primitive root of {p}.")
            break
        else:
            tracker.append(eq)
        if (i == p-1):
            print(f"{g} is a primitive root of {p}.")