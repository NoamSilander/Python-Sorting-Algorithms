number_list = []

while True:
    try:
        user_number = int(input('Write a number you want to add to the sorting list: '))
        number_list.append(user_number)
        print(f'Current list consists of: {number_list}')
    except Exception:
        print('Must be a whole number.')