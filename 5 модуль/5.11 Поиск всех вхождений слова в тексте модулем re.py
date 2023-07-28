import re

def find_all_words(text, word):
    search_results = re.findall(word, text, flags=re.IGNORECASE)
    return search_results

# Пример использования
text = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. PyThoN is often described as a 'batteries included' language due to its comprehensive standard library."

word = "Python"

results = find_all_words(text, word)
print(results)

