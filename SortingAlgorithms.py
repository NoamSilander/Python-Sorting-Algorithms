import time
number_list = []

def pick_numbers():
    while True:
        user_number = input('Write a number you want to add to the sorting list (q to exit): ').lower()
        if user_number == 'q':
            break
        try:
            number_list.append(int(user_number))
            print(f'Current list consists of: {number_list}')
        except Exception:
            print('Must be a whole number.')
 
def bubble_sort():
    swaps = True
    swap_count = 0
    while swaps:
        swaps = False
        for i, number in enumerate(number_list):
            try:
                if number_list[i] > number_list[i + 1]:
                    number_list[i], number_list[i + 1] = number_list[i + 1], number_list[i]
                    swap_count += 1
                    swaps = True
            except IndexError:
                pass
        time.sleep(0.05)
        print(number_list)
    print(f'{swap_count} swaps in total.')




pick_numbers()
bubble_sort()
