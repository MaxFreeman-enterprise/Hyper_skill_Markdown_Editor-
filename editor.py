# solution for stage 4:


formatters_list = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list",
                   "new-line"]


def read_int_input(prompt, val_label, min_val=0, max_val=None):
    val = input(prompt)
    try:
        val = int(val)
    except ValueError:
        raise TypeError(f"The {val_label} should be "
                        + f"within the range of {min_val} to {max_val}" if max_val
                        else f"greater than zero" if min_val - 1 == 0
                        else f"greater than {min_val - 1}")

    if not (min_val <= val and (val <= max_val if max_val is not None else True)):
        raise ValueError(f"The {val_label} should be "
                         + f"within the range of {min_val} to {max_val}" if max_val
                         else f"greater than zero" if min_val - 1 == 0
                         else f"greater than {min_val - 1}")

    return val


def get_plain():
    text = input("Text: ")
    return text


def get_bold():
    text = input("Text: ")
    return "**" + text + "**"


def get_italic():
    text = input("Text: ")
    return "*" + text + "*"


def get_inline_code():
    text = input("Text: ")
    return "`" + text + "`"


def get_link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"


def get_header():
    try:
        level = read_int_input("Level: ", "level", 1, 6)
    except (TypeError, ValueError) as e:
        raise e

    text = input("Text: ")

    nl = formatter_functions_dict["new-line"]()
    return level * "#" + " " + text + nl


def get_new_line():
    return "\n"


def get_markdown_list():
    global user_command
    result = ""
    nl = formatter_functions_dict["new-line"]()

    number_of_rows = 0
    while number_of_rows <= 0:
        try:
            number_of_rows = read_int_input("Number of rows: ", "number of rows", 1)
        except (TypeError, ValueError) as e:
            print(e)
            number_of_rows = 0

    if user_command == "ordered-list":
        list_of_elements = []
        for i in range(number_of_rows):
            text = input(f"Row #{i + 1}: ")
            list_of_elements.append(text)
        for x, y in enumerate(list_of_elements):
            result += f"{x + 1}. {y}" + nl

    elif user_command == "unordered-list":
        for i in range(number_of_rows):
            text = input(f"Row #{i + 1}: ")
            result += f"* {text}" + nl

    return result


def help_():
    print("""Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done""")


def done(total_text):
    # solution stage 5: only add the file rows below
    my_file = open("output.md", "w", encoding="utf-8")
    my_file.write(f"{total_text}")
    my_file.close()
    exit()


user_command = ""

formatter_functions_dict = {"plain": get_plain, "bold": get_bold, "italic": get_italic, "header": get_header,
                            "link": get_link, "inline-code": get_inline_code, "ordered-list": get_markdown_list,
                            "unordered-list": get_markdown_list, "new-line": get_new_line}


def main():
    global user_command

    total_text = ""
    while True:

        user_command = input("Choose a formatter: ")
        if user_command == "!help":
            help_()

        elif user_command == "!done" or user_command == "":
            done(total_text)

        elif user_command in formatter_functions_dict:

            try:
                result = formatter_functions_dict[user_command]()
                total_text += result
                print(total_text)
            except (TypeError, ValueError) as e:
                print(e)

        else:
            print("Unknown formatting type or command. Please try again.")


if __name__ == '__main__':
    main()

# # solution for stage 3:
# #
# #     plain — a normal text without any formatting
# #     bold/italic — self-explanatory
# #     inline-code — for example, python editor.py
# #     link — for example, google.com
# #     header — look at the header of this stage.
# #     unordered-list — this very list is an example of an unordered list
# #     ordered-list — a list with enumerated elements
# #     new-line — switches to the next line
#
# formatters_list = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list",
#                    "new-line"]
#
#
# def get_plain():
#     text = input("Text: ")
#     return text
#
#
# def get_bold():
#     text = input("Text: ")
#     return "**" + text + "**"
#
#
# def get_italic():
#     text = input("Text: ")
#     return "*" + text + "*"
#
#
# def get_inline_code():
#     text = input("Text: ")
#     return "`" + text + "`"
#
#
# def get_link():
#     label = input("Label: ")
#     url = input("URL: ")
#     return f"[{label}]({url})"
#
#
# def get_header():
#     level = input("Level: ")
#     text = input("Text: ")
#
#     try:
#         level = int(level)
#     except ValueError:
#         raise TypeError("The level should be within the range of 1 to 6")
#
#     if not 1 <= level <= 6:
#         raise ValueError("The level should be within the range of 1 to 6")
#
#     nl = formatter_functions_dict["new-line"]()
#     return level * "#" + " " + text + nl
#
#
# def get_new_line():
#     return "\n"
#
#
# def help_():
#     print("""Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
# Special commands: !help !done""")
#
#
# def done():
#     exit()
#
#
# formatter_functions_dict = {"plain": get_plain, "bold": get_bold, "italic": get_italic, "header": get_header,
#                             "link": get_link, "inline-code": get_inline_code, "ordered-list": lambda: NotImplemented,
#                             "unordered-list": lambda: NotImplemented, "new-line": get_new_line}
#
#
# def main():
#
#     total_text = ""
#     while True:
#
#         user_command = input("Choose a formatter: ")
#         if user_command == "!help":
#             help_()
#
#         elif user_command == "!done":
#             done()
#
#         elif user_command in formatter_functions_dict:
#
#             try:
#                 result = formatter_functions_dict[user_command]()
#                 total_text += result
#                 print(total_text)
#             except (TypeError, ValueError) as e:
#                 print(e)
#
#         else:
#             print("Unknown formatting type or command. Please try again.")
#
#
# if __name__ == '__main__':
#     main()


# solution for stage 2:

# formatters_list = "plain bold italic header link inline-code ordered-list unordered-list new-line".split()


# def help_():
#     print("""Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
# Special commands: !help !done""")
#
#
# def done():
#     exit()
#
#
# def main():
#     while True:
#         user_command = input("- Choose a formatter: ")
#         if user_command == "!help":
#             help_()
#         elif user_command == "!done":
#             done()
#         elif user_command in formatters_list:
#             continue
#         else:
#             print("Unknown formatting type or command. Please try again.")
#
#
# if __name__ == '__main__':
#     main()

# solution for stage 1:

# print("""# John Lennon
# or ***John Winston Ono Lennon*** was one of *The Beatles*.
# Here are the songs he wrote I like the most:
# * Imagine
# * Norwegian Wood
# * Come Together
# * In My Life
# * ~~Hey Jude~~ (that was *McCartney*)
# """)
