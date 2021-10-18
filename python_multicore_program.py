#!/usr/bin/env python3


import multiprocessing
import os
from functools import partial
from datetime import datetime
import sys

"""


            Program Name: python_multicore_program.py
            Program Written By: M. Joseph Tomlinson

Creating a Multi-cored Python Program---simple file writing demo "How-To"

Programs first runs by pinging number of cores a computer has
and then creates a list of values (1-X) based on the number of cores
and sends out a simple file printing command to each core. This specific "command"
aka function can easily be modified in a user's program for more complex type analysis

Helpful Links for Understanding "multiprocessing" and "partial"

Official Python Links
https://docs.python.org/3/library/multiprocessing.html
https://docs.python.org/3/library/functools.html

Simple Stackoverflow Example Link
https://stackoverflow.com/questions/23537037/python-multicore-programming/23537302

"""


def print_numbers_in_file(number, date):

    """

    Prints a number in a file

    : Param number: Number

    : Return NONE:

    """

    # Create name for file
    output_file_name = "file_" + str(number) + ".txt"

    # Open the file
    output_file = open(output_file_name, 'w')

    # Write simple sentences to file
    output_file.write("\n")
    output_file.write("Multicore Program File_" + str(number) + "\n")
    output_file.write("Current Date: " + date + "\n")
    output_file.write("Hello World!\n")
    output_file.write("\n")

    # Close the file
    output_file.close()

    return ()


def main():

    print ("Starting Multicore Demo Program")
    print ("")

    # Get Currrent Date Ran
    date_ran = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    print ("Date and Time Program Ran: " + date_ran)
    print ("")

    # Get the number of cores
    core_count = os.cpu_count()
    print ("Number of cores: " + str(core_count))

    ### Create a list of values (starting 1) based on number of cores ###
    # Create empty list
    list_of_values = []
    # Loop over range of cores
    for x in range(core_count):
        # Add to list (value gets plus 1 to make easier for user)
        list_of_values.append(x+1)
    print ("Create list of values based on core count:")
    print (list_of_values)
    print ("")

    # Setup the pool---aka cores being used
    pool = multiprocessing.Pool(core_count)

    # Passing multiple variables to multi-cored function requires partial
    multi_core_function = partial(print_numbers_in_file, date=date_ran)

    # Run the function with multicore in python
    print ("Running Multicore function with 'map reduce' command")
    run_results = pool.map(multi_core_function, list_of_values)
    pool.close()
    pool.join()

    print ("")
    print ("Done Running Multicore Program")


if __name__ == "__main__":
    main()
