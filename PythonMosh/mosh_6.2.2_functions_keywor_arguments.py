
def total_cost_fn(goods_cost, shipment_cost, discount):
    discout_amount = (goods_cost + shipment_cost) * discount
    cost = goods_cost + shipment_cost - discout_amount
    print(cost)


print("Start")
total_cost_fn(9, discount=0.1, shipment_cost=1)     # pokud mícháme keyword argumenty s positional argumenty,
                                                    # všechny positional argumenty musí být před keyword argumenty
print("Finish")

# but to improve readability of the code is better to use keyword arguments while handling with numbers:
total_cost_fn(goods_cost=9, discount=0.1, shipment_cost=1)