# This program prints out a lighthouse out of "X"'s, "*"'s, "\"'s, and "/"'s.
# Created by Kyler Nats

#This constant changes the scale of the lighthouse
CONSTANT = 2

# This function runs the program
def main():
    top_stars()
    eight_row()
    twelve_row()
    eight_row()
    six_row()
    eight_row()
    first_slash_row()
    eight_row()
    six_row()
    eight_row()
    second_slash_row()
    eight_row()
    two_row()
    eight_row()
    eight_row()
    six_row()
    six_row()
    six_row()
    six_row()
    bottom_row()
    
# This function prints the first two lines that have only stars
def top_stars():
    # This for loop prints two lines of "*"'s and spaces them based on the constant
    for i in range(0,2):
        print(" " * (CONSTANT - 1), " " * CONSTANT, "**")

# This function prints rows with 8 X's
def eight_row():
    base_x_count = 4
    total_x_count = base_x_count + (CONSTANT * 2)
    print(" " * (CONSTANT - 1), "X" * total_x_count)

# This function prints rows with 12 X's
def twelve_row():
    base_x_count = 8
    total_x_count = base_x_count + (CONSTANT * 2)
    # This for loop prints two lines of "X"'s and spaces them based on the constant
    for i in range(0,2):
        if CONSTANT == 2:
            print("X" * total_x_count)
        else:
            print(" " * (CONSTANT - 3), "X" * total_x_count)

# This function prints rows with 3 X's, space, and then 3 X's
def six_row():
    base_x_count = -4
    total_x_count = base_x_count + (CONSTANT * 2)
    # This for loop prints a line of 3 "X"'s and spaces them before printing a second 3 "X"'s
    for i in range(1):
        print(" " * (CONSTANT - 1), "XXX", " " * total_x_count, "XXX")


# This function prints the first set of rows with slashes, starting each line with "\"
def first_slash_row():
    initial_slash_count = (CONSTANT * 2) - 1
    # This for loop is reliant on the constant with number of rows, "/"'s, "\"'s, and spacing
    for i in range(CONSTANT * 2 - 1):
        slash_count = initial_slash_count - (i)
        backslash_count = i + 1
        print(" " * CONSTANT, "X" + "\\" *
        backslash_count + "/" * slash_count + "X")


# This function prints the second set of rows with slashes, starting each line with "/"
def second_slash_row():
    initial_slash_count = (CONSTANT * 2) - 1
    # This for loop is reliant on the constant with number of rows, "/"'s, "\"'s, and spacing
    for i in range(CONSTANT * 2 - 1):
        slash_count = initial_slash_count - (i)
        backslash_count = i + 1
        print(" " * CONSTANT, "X" + "/" * slash_count + "\\" *
        backslash_count + "X")

# This function prints the row that has 2 X's, space, and then 2 X's
def two_row():
    base_x_count = -2
    total_x_count = base_x_count + (CONSTANT * 2)
    # This for loop prints one line of a pair of "XX"'s, with spacing in between based on the constant
    for i in range(1):
        print(" " * (CONSTANT - 1), "XX", " " * total_x_count, "XX")

# This function prints the bottom three rows, with all X's and no other characters
def bottom_row():
    base_x_count = 4
    total_x_count = base_x_count + (CONSTANT * 4)
    # The for loop prints three rows of total_x_count based on what the constant is
    for i in range(1,4):
        print("X" * total_x_count)

# This starts the program
main()
