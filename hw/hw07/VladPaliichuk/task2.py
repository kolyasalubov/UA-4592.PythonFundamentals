print("""
      1. Площа прямокутника
      2. Площа Трикутника
      3. Площа Кола""")
number = int(input("Введіть відповідний номер: "))

match number:
    case 1:
        a = int(input("Введіть а: "))
        b = int(input("Введіть b: "))
        print("Площа прямокутника: ",a * b)
    case 2:    
        a = int(input("Введіть основу: "))
        b = int(input("Введіть висоту: "))
        print("Площа трикутника: ",(1/2) * a * b)
    case 3:    
        import math
        r = int(input("Введіть радіус: "))
        print("Площа кола: ",round(math.pi * r**2, 2))