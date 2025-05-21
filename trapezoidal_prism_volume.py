#!/usr/bin/env python3

# Created By: Luke Di Bert
# Date: May 21, 2025

# adds math module
import math


# function calculating the area of the base
def area_calc(array):
    area = 0.5 * (array[0] + array[1]) * array[2]

    # returns calculated area
    return area


# main function
def main():

    # loop to stop code at points
    while True:
        print("Welcome to Luke's volume of a trapezoidal prism calculator!")

        # array used to store dimension (0 = base1, 1 = base2, 2 = height, 3 = length)
        dimension = [0, 0, 0, 0]
        try:
            # gather dimension and put into respective spots in array
            dimension[0] = float(input("Enter base 1 of the trapezoidal prism (cm): "))
            dimension[1] = float(input("Enter base 2 of the trapezoidal prism (cm): "))
            dimension[2] = float(input("Enter height of the trapezoidal prism (cm): "))
            dimension[3] = float(input("Enter length of the trapezoidal prism (cm): "))

            # compound boolean if statement to find if dimensions are 0
            if (
                dimension[0] <= 0
                or dimension[1] <= 0
                or dimension[2] <= 0
                or dimension[3] <= 0
            ):
                print("Dimension have to be greater than 0!")
                break

            # calls area_calc function using dimension array in the parameter
            base_area = area_calc(dimension)

            # calculates base volume using base_area calculated from area_calc function
            volume = base_area * dimension[3]

            # prints volume
            print(
                "The volume of your trapezoidal prism is:",
                str(round(volume, 2)) + "cm^3",
            )

            # catch for invalid input
        except:
            print("Oops, you entered invalid input! please use numbers only")
        try:
            # asks user if they want to run program again
            run_again = str(
                input("Would you like to run the program again? yes(0), no(1): ")
            )

            # ends loop if they chose no
            run_again_int = int(run_again)
            if run_again_int == 1:
                print("Have a good day")
                break

        # catch for invalid input
        except:
            print(run_again, "was not valid input")
            break


if __name__ == "__main__":
    main()
