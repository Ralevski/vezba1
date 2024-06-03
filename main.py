# main.py
from swap import swap
from extras.desc import desc

if __name__ == "__main__":
    a = int(input("Please enter the first number (0-3): "))
    b = int(input("Please enter the second number (0-3): "))
    swapped_a, swapped_b = swap(a, b)
    print(f"The two swapped numbers are: {swapped_a} and {swapped_b}")

    n = int(input("Please enter a number to print in natural descending order: "))
    print(f"Natural descending order of {n} is:", end=" ")
    desc(n)

