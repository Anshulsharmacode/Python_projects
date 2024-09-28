def print_kargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}: {value}")

print(print_kargs(name="sktiman"))