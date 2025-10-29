import os

def main():
    # Vulnerable: writes to file in mutable volume or filesystem
    with open("data/exploit.txt", "w") as f:
        f.write("This should not be allowed in immutable container!")

    print("File written to data/exploit.txt")

if __name__ == "__main__":
    main()
