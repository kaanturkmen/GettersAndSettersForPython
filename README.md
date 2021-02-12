# Constructors, Getters, and Setters for Python

You do not need to import or install anything.

Example usage can be found in the input and output files.

Usage: delete all lines in the input file. Place all the attributes of your class in the input file. Run the following command, and the script will generate a Constructor, Getters, and Setters for your class. Note, it will generate them in two different styles.

`python3 create_Constructor_Getters_Setters.py`

The first style of output provides getters and setters for all attributes, regardless of whether they are public, protected, or private. NB Setters are really only required for non-public (i.e. protected or private) attributes. There is thus an option (found in the main() function) to change behaviour of this first style so that the script only outputs getters and setters for those non-public attributes. (Public attributes may be addressed directly from outside the class.)

The second style of output provides getters and setters only for those non-public attributes, and it provides them using property decorators. This style may not be used to provide setters and getters for public attributes, so that option is not available for the second style.

You may provide your list of attributes in any of the following styles.

* `attribute = value`
* `attribute=value`
* `attribute =`
* `_attribute`
* `__attribute = value`




