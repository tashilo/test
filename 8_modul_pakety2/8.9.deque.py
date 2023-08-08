from collections import deque

MAX_LEN = 10  # Просто пример. Задайте свое значение для ограничения.

lifo = deque(maxlen=MAX_LEN)

def push(element):
    lifo.appendleft(element)

def pop():
    if not lifo:
        return None
    return lifo.popleft()

