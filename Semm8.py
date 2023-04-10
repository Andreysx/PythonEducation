filename = 'Semm8BD.txt'

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as data:
        data_array = []
        for line in data:
            item = line.replace('\n','').split(sep = ',')
            data_array.append(item)
    return data_array


def write_file(filename, data_array):
    with open(filename, 'w', encoding='utf-8') as data:
        for i in data_array:
            write_element = ', '.join(i)
            data.write(f'{write_element}\n')


def add_item(filename):
    data_array = read_file(filename)
    max_id = 0
    for i in range(1,len(data_array)):
        if max_id < int(data_array[i][0]):
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    print(next_id)
    lastname = input('Фамилия: ')
    firstname = input('Имя: ')
    secondname = input('Отчество: ')
    phone = input('Телефон: ')
    new_item = []
    new_item.append(str(next_id))
    new_item.append(lastname)
    new_item.append(firstname)
    new_item.append(secondname)
    new_item.append(phone)
    print(new_item)
    print(data_array)
    data_array.append(new_item)
    print(data_array)
    write_file(filename, data_array)


def show_all_items(filename):
    data_array = read_file(filename)
    for i in range(1,len(data_array)):
        print("ID: ", data_array[i][0],
              "Фамилия: ", data_array[i][1],
              "Имя: ", data_array[i][2],
              "Отчество: ", data_array[i][3],
              "Телефон: ", data_array[i][4])


def get_current_ids(data_array):
    """
    Возвращает массив всех имеющихся айдишников
    :param data_array:
    :return:
    """
    return [i[0] for i in data_array]


def change_some_writes(id: str):
    """
    Редактирует запись по id
    :param id:
    :return:
    """
    data_array = read_file(filename)
    ids = get_current_ids(data_array)
    for i in data_array:
        if id not in ids:
            print('ID не существует')
            break
        elif i[0] == id:
            i[1] = input('Фамилия: ')
            i[2] = input('Имя: ')
            i[3] = input('Отчество: ')
            i[4] = input('Телефон: ')
    return data_array


def delete_some_writes(id: str):
    """
    Удаляет запись по id
    :param id:
    :return:
    """
    data_array = read_file(filename)
    ids = get_current_ids(data_array)
    for i, value in enumerate(data_array):
        if id not in ids:
            print('ID не существует')
            break
        elif value[0] == id:
            data_array.pop(i)
    return data_array


def menu():
    while True: # Будет выполнять код, пока не сработает break
        print('Добро пожаловать в телефонный справочник!')
        print('1 - Показать все записи')
        print('2 - Добавить запись')
        print('3 - Изменить запись')
        print('4 - Удалить запись')
        print('5 - Закрыть телефонный справочник')
        user_operation = int(input())

        if user_operation == 1:
            show_all_items(filename)
        elif user_operation == 2:
            add_item(filename)
        elif user_operation == 3:
            write_id = input('Введите ID записи для изменений: ')
            new_array = change_some_writes(write_id)
            write_file(filename, data_array=new_array)
        elif user_operation == 4:
            write_id = input('Введите ID записи для удаления: ')
            new_array = delete_some_writes(write_id)
            write_file(filename, data_array=new_array)
        elif user_operation == 5:
            print('Пока')
            break


menu()
