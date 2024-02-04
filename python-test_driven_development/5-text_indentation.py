#!/usr/bin/python3
"""

    Function to add indentation to text based on certain punctuation marks.

"""


def text_indentation(text):
    """

    Args:
    - text (str): The text to be processed.

    Raises:
    - TypeError: If the input text is not a string.

    Prints:
    - The input text with extra indentation whenever one of
    the following punctuation marks is encountered: ':', '?', ','.
    - Each character of the text is printed without adding
    a new line until one of the specified punctuation marks is encountered.

    Example:
    text_indentation("Hello, how are you? I am fine. Thank you!")
    Hello,

    how are you?

    I am fine.

    Thank you!
    """

    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # List of punctuation marks to split the text on
    split = [".", "?", ":"]

    # Iterate through each character in the text
    i = 0
    te = ""
    while i < len(text):
        # Print the character without a newline
        te += text[i]

        # If the character is one of the specified punctuation marks
        if text[i] in split:
            if i + 1 < len(text):
                while text[i + 1] == " ":
                    i += 1
            te += "\n\n"
        i += 1
    print("{}".format(te), end="")
