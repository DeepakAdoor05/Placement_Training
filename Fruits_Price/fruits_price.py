def calculate_sales(Fruits):
    Total_sales = 0
    Total_items = 0
    for fruit in Fruits:
        price = int(fruit[1])
        quantity = int(fruit[2])
        Total_sales += price*quantity
        Total_items += quantity
        Average_sales = Total_sales/Total_items
    print(f"Total Sales: {Total_sales}")
    print(f'Average Sales: {Average_sales:.3f}')


Fruits = [
    ["Apple","10","2"],
    ["Orange","20","4"]
]
calculate_sales(Fruits)