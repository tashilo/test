from collections import Counter

def get_count_visits_from_ip(ips):
    return Counter(ips) # Возвращает словарь, где ключ — это IP, а значение — количество вхождений

def get_frequent_visit_from_ip(ips):
    count = Counter(ips)
    return count.most_common(1)[0] # Возвращает кортеж с наиболее часто встречаемым IP и количеством его вхождений