def main():
    print("Convert Dollars to Pounds")
    print()

    dollars = eval(input("Dollar amount: "))

    convert_dollars = lambda dollars : dollars * 0.82

    pounds = convert_dollars(dollars)

    print("The pounds amount is: ", pounds, "pounds")

main()