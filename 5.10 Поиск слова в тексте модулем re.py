import re


def find_word(text, word):
    search = re.search(word, text)
    if search:
        result = {
            "result": True,
            "first_index": search.start(),
            "last_index": search.end(),
            "search_string": search.group(),
            "string": text,
        }
    else:
        result = {
            "result": False,
            "first_index": None,
            "last_index": None,
            "search_string": word,
            "string": text,
        }
    return result


print(
    find_word(
        "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
        "Python",
    )
)

print(
    find_word(
        "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
        "Java",
    )
)
