import re

def replace_spam_words(text, spam_words):
    # Проходимся по списку запрещенных слов
    for spam_word in spam_words:
        # Создаем шаблон замены - символы '*' равные по длине запрещенному слову
        replacement = '*' * len(spam_word)
        
        # Вызываем функцию re.sub() для замены запрещенного слова на шаблон замены
        # Аргументы функции:
        #   - spam_word: регулярное выражение для поиска (запрещенное слово)
        #   - replacement: строка для замены (шаблон замены)
        #   - text: текст, в котором будет произведена замена
        #   - flags=re.IGNORECASE: флаг для игнорирования регистра при поиске
        text = re.sub(spam_word, replacement, text, flags=re.IGNORECASE)
    
    # Возвращаем текст с замененными запрещенными словами
    return text

# Пример использования
text = "This is a sample text with bad words such as profanity and offensive language."
spam_words = ["profanity", "offensive"]

result = replace_spam_words(text, spam_words)
print(result)


