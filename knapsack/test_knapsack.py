from knapsack.knapsack import Item, knapsack

rice = Item('rice', 10, 10)
beans = Item('beans', 100, 10)
water = Item('water', 15, 10)

def test_knapsack():
    assert knapsack([rice, beans, water], 10)[0].name == 'beans'
    assert knapsack([rice, water], 10)[0].name == 'water'

    all = knapsack([rice, beans, water], 30)
    assert len(all) == 3

    big_bag = knapsack([rice, beans, water], 100)
    assert len(big_bag) == 3

    fractional = knapsack([rice, beans, water], 15)
    assert fractional[0].name == 'beans'
    assert fractional[0].weight == 10
    assert fractional[1].name == 'water'
    assert fractional[1].weight == 5

    fractional2 = knapsack([rice, beans, water], 5)
    assert fractional2[0].name == 'beans'
    assert fractional2[0].weight == 5
