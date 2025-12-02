def search_big_number(x: int, y: int) -> int:
    """
    Функція приймає на вхід два цілих числа і повертає більше їх. 
    Якщо числа дорівнюють, повертається будь-яке з них. 

    :param x: Перше ціле число 
    :param y: Друге ціле число 
    :return: Більше з двох чисел
    """
    if x >= y:
        return x
    else:
        return y
    
#test = search_big_number(10, 5)
#print(test) 