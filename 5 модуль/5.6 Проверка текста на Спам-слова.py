def is_spam_words(text, spam_words, space_around=False):
    """
    Функция проверяет наличие запрещенных слов в тексте.
    Аргументы:
    - text - текст для проверки;
    - spam_words - список запрещенных слов;
    - space_around - флаг, указывающий на необходимость поиска отдельных слов;
        по умолчанию равен False.
    Возвращает True, если найдено запрещенное слово, и False в противном случае.
    """
    # переводим текст в нижний регистр, чтобы искать слова независимо от регистра
    text_lower = text.lower()
    # приводим список запрещенных слов к нижнему регистру
    spam_words_lower = [word.lower() for word in spam_words]
    # если требуется искать отдельные слова
    if space_around:      
        # избавляемся от знаков припинания в тексте
        iskl = [".", ",", "!", "?", ":", ";"]
        text_lover_not_simv = ""
        for simv in text_lower:
            if simv not in iskl:
                text_lover_not_simv = text_lover_not_simv + simv
            else:
                continue    
        # разбить текст на отдельные слова и выяснить есть ли среди них спам-слово        
        list_words_text = text_lover_not_simv.split(" ")
        for word in spam_words_lower:
            if word in list_words_text:
                return True
            # если запрещенные слова не найдены, возвращаем False
            else:
                return False
    # если искомое слово не должно стоять отдельно
    else:
        # проверяем, есть ли запрещенное слово в тексте
        for word in spam_words_lower:
            if word in text_lower:
                return True
        # если запрещенные слова не найдены, возвращаем False
        return False





text1 = "Ты хорош, но выглядишь как лох."
text2 = "Молох бог ужасен."
spam_words1 = ["лох",]

print(is_spam_words(text1, spam_words1))  # True
print(is_spam_words(text1, spam_words1, True))  # True
print(is_spam_words(text2, spam_words1))  # True
print(is_spam_words(text2, spam_words1, True)) # False

