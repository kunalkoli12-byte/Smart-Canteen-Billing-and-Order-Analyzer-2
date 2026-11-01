print("\n==========SMART CANTEEN=========\n")

print("\nVeg Sandwich ->","(price: 60)")
print("\nMasala Dosa ->","(price: 80)")
print("\nChole Rice ->","(price: 90)")
print("\nPaneer Role ->","(price: 100)")
print("\nTea ->","(price: 20)")



total_cost = 0
while True:
    choose = input("Enter the item : ") 
    if choose == "OK":
            break
    
    quantity = int(input("Enter quantity of item: "))
    print("To complete order enter -> OK")
    
    

    if choose == "Veg Sandwich" :
        cost = 60*quantity
        total_cost += cost
    elif choose == "Masala Dosa" :
        cost = 80*quantity
        total_cost += cost
    elif choose == "Chole Rice":
        cost = 90*quantity
        total_cost += cost

    elif choose == "Paneer Role":
         cost = 100*quantity
         total_cost += cost
    elif choose == "Tea":
         cost = 20*quantity
         total_cost += cost
    else :
        print("INVALID")

print("\nYour Total Cost of food is : ",total_cost)
    