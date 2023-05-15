def formatted_numbers():
    # Создаем заголовок таблицы
    table_title = "|{0:^10}|{1:^10}|{2:^10}|".format("decimal", "hex", "binary")
    # Создаем строки таблицы для каждого числа
    table_strs = []
    for i in range(16):
        hex_num = hex(i)[2:]
        bin_num = bin(i)[2:]
        table_str = "|{0:<10}|{1:^10}|{2:>10}|".format(i, hex_num, bin_num)
        table_strs.append(table_str)
    return [
        table_title,
    ] + table_strs


for el in formatted_numbers():
    print(el)
