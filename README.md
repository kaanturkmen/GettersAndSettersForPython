# Setup
1. Clone this repository to your local machine.
2. Delete all lines in the input file.
3. Place all the attributes of your class in the input file.
4. Run the following command, and the script will generate a Constructor, Getters, and Setters for your class.

```
python3 create_Constructor_Getters_Setters.py
```

P.S. Example usage can be found in the input and output files. Also, this python script do not require to import or install any additional packages / applications.

# Output Styles

Running the script will generate output in two different styles.

1. The first style of output provides getters and setters for all attributes, regardless of whether they are public, protected, or private. NB Setters are really only required for non-public (i.e. protected or private) attributes. There is thus an option (found in the main() function) to change behaviour of this first style so that the script only outputs getters and setters for those non-public attributes. (Public attributes may be addressed directly from outside the class.)

2. The second style of output provides getters and setters only for those non-public attributes, and it provides them using property decorators. This style may not be used to provide setters and getters for public attributes, so that option is not available for the second style.

# Valid Input Formats

You may provide your list of attributes in any of the following styles.

* `attribute = value`
* `attribute=value`
* `attribute =`
* `_attribute`
* `__attribute = value`

# How to Contribute?
1. If you need an additional feature that you want to add, please create a pull request. 
2. If you want to request a feature, create an issue instead.

P.S. While sending a pull request, please be clear as possible (i.e. comment your code, explain what you have done.). Also, sent multiple pull requests if the change you will make is complicated and long.
