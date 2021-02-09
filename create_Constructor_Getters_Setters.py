# 
# Date:       8 February 2021
# Description:  Creates a Constructor, Setters, and Getters for a
#                  given list of Class Attributes supplied in the 
#                  input file.
#               Input file format has two possible formats.
#                   <attribute name>
#                   <attribute name> = <initialisation the type>
#               Examples follow.
#                   context_name = ""
#                   num_images = 0
#                   friends = []
#                   __id

""" Updated 2021-02-07 to make allow for hidden attributes, and to include 
       creation of a Constructor.

    Have changed the indent of a tab to the PEP-008 recommended four spaces.
    Added the option to distinguish private and protected attributes from 
       public ones.
    In truth, only non-public attributes warrant a getter and a setter. 
    An option is present to allow creation of getters and setters for
       all attributes, or only those that are not public.
"""
import sys

def str2bool(stuff):
    """Converts a string to a Boolean as a human would expect."""
    return stuff.lower() in ("yes", "true", "y", "1")

def open_files(input_file_name, output_file_name):
    """
    Opens both the input and output files, 
    returning pointers to those files.
    """
    # Check that the input file is present and can be opened for reading.
    try:
        input_file = open(input_file_name, "r")
    except IOError as err:
        print(f"Cannot find or open the file: {input_file_name}.")
        sys.exit()

    # Check that we can open the output file for writing, 
    #    creating it first, if necessary.
    try:
        output_file = open(output_file_name, "w")
    except IOError as err:
        print(f"Cannot find or open the file: {output_file_name}.")
        sys.exit()

    return input_file, output_file

def read_input(input_file):
    """
    Reads the input file for a list of attributes of the Class, 
    returning said list.
    """
    class_attributes = []
    try:
        attributes_from_file = input_file.readlines()
    except IOError as err:
        print(f"Cannot read the list of attributes from the file: \
            {output_file_name}.")
        sys.exit()

    # We shall ignore any lines beginning with a hash ("#") and anything 
    #    following the first space.
    for each_line in attributes_from_file:
        """
        Create a list of the name and the name cleaned of 
        any prefixed underscores.
        """
        if (len(each_line.strip()) > 0) and (each_line[0] != "#"):
            attrib_names = []
            attrib_names.append(each_line.strip().split()[0])
            attrib_names.append(attrib_names[0].lstrip("_"))
            class_attributes.append(attrib_names)
    
    return class_attributes

def create_output(class_attributes, output_file, do_for_all_attributes):
    """ Write out the constructor, and those getters and setters required
    according to the arguments supplied.
    """
    try:
        # Added 2021-02-07 to create a Constructor
        output_file.write("#--------- Constructor --------\n\n")
        output_file.write("def __init__(")
        counter = 0
        # output Constructor declaration
        for each_var in class_attributes:
            counter += 1
            if counter == len(class_attributes):
                output_file.write(each_var[1] + "):\n\n")
            else:
                output_file.write(each_var[1] + ", ")
        # output initialisation of Attributes
        for each_var in class_attributes:
            output_file.write("    self." + each_var[0] + " = " + each_var[1] + "\n")
        output_file.write("\n\n")

        # output Accessors per Attribute
        output_file.write("#----------- Getters ----------\n\n")
        for each_var in class_attributes:
            if do_for_all_attributes:
                output_file.write(f"def get_{each_var[1]}(self):\n")
                output_file.write(f"    return self.{each_var[0]}\n\n")
            elif (each_var[0] != each_var[1]):
                output_file.write(f"def get_{each_var[1]}(self):\n")
                output_file.write(f"    return self.{each_var[0]}\n\n")
        output_file.write("\n\n")

        # output Mutators per Attribute
        output_file.write("#----------- Setters ----------\n\n")
        for each_var in class_attributes:
            if do_for_all_attributes:
                output_file.write(f"def set_{each_var[1]}(self, {each_var[1]}):\n")
                output_file.write(f"    self.{each_var[0]} = {each_var[1]}\n\n")
            elif (each_var[0] != each_var[1]):
                output_file.write(f"def set_{each_var[1]}(self, {each_var[1]}):\n")
                output_file.write(f"    self.{each_var[0]} = {each_var[1]}\n\n")
        output_file.write("\n\n")

        # line to show end of output
        output_file.write(("#" + "-" * 30) + "\n\n\n")
    except IOError as err:
        print(f"Cannot write to the file: {output_file_name}.")
        sys.exit()

def clean_up_and_close(*all_files):
    """Closes all files, whose pointers are sent as arguments."""
    try:
        for each_file in all_files:
            each_file.close()
    except IOError as err:
        # We do not care, if we cannot close the file. 
        # Python should manage this for us.
        pass

def main():

    # Constants
    INPUT_FILE_NAME = "input.txt"
    OUTPUT_FILE_NAME = "output.txt"
    # Getters and Setters for all, or only non-public attributes.
    #    This might be supplied as a command-line argument instead.
    DO_FOR_ALL_ATTRIBUTES = True 
    
    # Process the attribute information and create the code.
    input_file, output_file = open_files(INPUT_FILE_NAME, OUTPUT_FILE_NAME)
    class_attributes = read_input(input_file)
    create_output(class_attributes, output_file, DO_FOR_ALL_ATTRIBUTES)
    clean_up_and_close(input_file, output_file)
    print("\nCreation of Constructor, Accessors, and Mutators complete!")

if __name__ == '__main__':
    main()