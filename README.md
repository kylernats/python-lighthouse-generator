# python-lighthouse-generator

This is a fun Python project where I built a lighthouse using only text characters like "X", "*", "/", and "\". The program prints a full lighthouse shape in the console, and the design changes based on a constant value at the top of the script. I created this to practice writing functions, using loops, and formatting printed output in Python.

I wanted to challenge myself by building something visual using only code and simple logic. Instead of drawing, I learned how to carefully control spacing and patterns using strings and print statements. The project helped me get better at thinking through code structure, breaking a problem into smaller parts, and keeping everything organized using functions.

The script works by calling a main function that runs a bunch of smaller functions in order. Each smaller function is responsible for printing a different part of the lighthouse. For example, 'top_stars()' prints the lights at the top, while 'eight_row()', 'six()', and 'twelve_row()' build out the lighthouse structure with "X" characters. The 'first_slash_row()' and 'second_slash_row()' functions create diagonal slashes to add shape to the lighthouse. At the bottom, 'bottom_row()' finishes the base.

There is a constant called 'Constant' at the top of the code. If you change this value, the size and scale of the lighthouse will adjust automatically. That makes the design flexible and fun to experiment with.
