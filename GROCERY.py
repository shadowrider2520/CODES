def disp_prods(products):          
                f = open("Y:/GROCERY/STORE.txt","r")
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts)==5:
                        id = parts[0].strip()
                        name = parts[1].strip()
                        category = parts[2].strip()
                        price = parts[3].strip()
                        quantity = parts[4].strip()
                        products.append({
                            "id":id,
                            "name":name,
                            "category":category,
                            "price":price,
                            "quantity":quantity})
                f.close()
def linear_search(products):
    lst = []
    tar = input("enter the category:")
    for i in products.keys():
        if i==tar:
            lst.append(i,products[i])
    return lst
def update_quan(products):
    
while True:
    products = []
    print("---------MENU------")
    print("1. display all products:")
    print("2. search by category:")
    print("3. update quantity of a product:")
    print("4. find the cosliest product:")
    print("5. generate category wise summary:")
    print("6. save updated data back to file:")
    print("7. exit:")
    option = int(input("enter your option:"))
    if option==1:
        disp_prods(products)
        print("ID  |  NAME  | CATEGORY | PRICE |  QUANTITY")
        print("------------------------------------------------------------------------------------")
        for x in products:
             for i in x.values():
                 print(i)
             print("\n")
             print(end= " ")
    if option == 2:
        print(linear_search(products))
    if option ==3:
        print(update_quan(products))
        
        
    if option == 7:
        print("exiting")
        break
         

        
