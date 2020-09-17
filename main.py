user_variables = []


def delete_spaces_if_exists(string):
    new_string = string.split(" ")
    return new_string[0]


def read_input():
    with open("input.txt", "r") as f:
        context = f.readlines()

        for line in context:
            line_context = line.strip()
            edited_line = line_context.split("=")
            user_variables.append(delete_spaces_if_exists(edited_line[0]))


def create_output():
    with open("output.txt", "w") as f:
        f.write("----- Getters & Setters -----\n\n")
        for variable in user_variables:
            f.write(f"def get_{variable}(self):\n")
            f.write(f"\treturn self.{variable}\n\n")

        for variable in user_variables:
            f.write(f"def set_{variable}(self, {variable}):\n")
            f.write(f"\tself.{variable} = {variable}\n\n")


if __name__ == "__main__":
    read_input()
    create_output()