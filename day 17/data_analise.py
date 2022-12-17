orders = []
orders_height = []
with open("output_for_data.txt", "r") as file:
    for line in file:
        line = line.split(";")
        orders.append(int(str(line[0])+str(line[2])+str(line[4])+str(line[6])+str(line[8])))
        orders_height.append([int(line[1]),int(line[3]),int(line[5]),int(line[7]),int(line[9])])
for i in range(10_000):
    order = orders.pop(0)
    if order in orders and orders.index(order) == 348:
        print (f"{i} {order} {orders.index(order)+1} {orders_height[i-1][-1]} {orders_height[i+orders.index(order)+1][-1] - orders_height[i][-1]}")

