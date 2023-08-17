class IDException(Exception):
    pass

def add_id(id_list, employee_id):
    if not employee_id.startswith('01'):
        raise IDException("Идентификатор сотрудника должен начинаться с '01'")
    id_list.append(employee_id)
    return id_list

# Пример использования
id_list = ['0101', '0102']
try:
    new_list = add_id(id_list, '0203')
except IDException as e:
    print(f"Произошла ошибка: {e}")
else:
    print(f"Обновленный список ID: {new_list}")
