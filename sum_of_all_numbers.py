#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Oct 2021
# This program adds all numbers together
#   with user input


def sum_of_numbers(list_of_numbers):
    # This function adds all numbers
    total = 0

    for each_loop in list_of_numbers:
        total += each_loop

    return total


def main():
    # This function prints the final answer

    list_of_numbers = []
    second_input_int = None

    # input
    first_input = input("How many numbers do you want to add?: ")
    print("")

    try:
        first_input_int = int(first_input)
        for second_each_loop in range(0, first_input_int):
            second_input_str = input("Enter the number: ")
            second_input_int = int(second_input_str)
            list_of_numbers.append(second_input_int)

        # call function
        final_answer = sum_of_numbers(list_of_numbers)
        print("\nThe sum of all numbers is {0}.".format(final_answer))

    except Exception:
        print("\nInvalid input, try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
