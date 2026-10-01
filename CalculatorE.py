def gcd(a, b):
    while b != 0:
        remainder = a % b
        print(a, "÷", b, "=", a // b, "remainder", remainder)
        a = b
        b = remainder
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


print("=== GCD AND LCM CALCULATOR ===")

first = int(input("Enter First Integer: "))
second = int(input("Enter Second Integer: "))

choice = input("Do you have a third integer to input? (Y/N): ")

if choice == "Y" or choice == "y":

    third = int(input("Enter Third Integer: "))

    print("\n=== GCD COMPUTATION ===")

    print("GCD of", first, "and", second, ":")
    gcd_first_second = gcd(first, second)

    print("GCD(", first, ",", second, ") =", gcd_first_second)

    print("\nGCD of", gcd_first_second, "and", third, ":")
    final_gcd = gcd(gcd_first_second, third)

    print("GCD(", gcd_first_second, ",", third, ") =", final_gcd)

    print("\nGCD =", final_gcd)

    print("\n=== LCM COMPUTATION ===")

    first_lcm = lcm(first, second)
    print("LCM(", first, ",", second, ") =", first_lcm)

    final_lcm = lcm(first_lcm, third)
    print("LCM(", first_lcm, ",", third, ") =", final_lcm)

    print("\nLCM =", final_lcm)

else:

    print("\n=== GCD COMPUTATION ===")

    final_gcd = gcd(first, second)

    print("GCD(", first, ",", second, ") =", final_gcd)
    print("\nGCD =", final_gcd)

    print("\n=== LCM COMPUTATION ===")

    final_lcm = lcm(first, second)

    print("LCM(", first, ",", second, ") =", final_lcm)
    print("\nLCM =", final_lcm)