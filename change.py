def change():
    expense = 23.75
    money = 100
    vuelto_pesos = int(money-expense)
    vuelto_centavos = int((money-expense-vuelto_pesos)*100)
    print(f"Ingresar gasto:\n{expense}")
    print(f"Dinero recibido\n{money}")
    print("\nVuelto\n")
    print(f"Pesos:\n{vuelto_pesos}")
    print(f"Centavos:\n{vuelto_centavos}")