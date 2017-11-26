class Item:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

    def density(self):
        return self.value/self.weight

    def __str__(self) -> str:
        return '{}: value: {} weight: {}'.format(self.name, self.value, self.weight)

    def __repr__(self) -> str:
        return '{}: value: {} weight: {}'.format(self.name, self.value, self.weight)


def knapsack(items, capacity):
    out = []
    items.sort(key=lambda i: i.density())

    current_capacity = capacity

    print(items)

    while current_capacity > 0 and len(items) > 0:
        item = items.pop()
        if current_capacity >= item.weight:
            current_capacity -= item.weight
            out.append(item)
            continue

        item.weight = item.weight * (current_capacity/item.weight)
        current_capacity -= item.weight
        out.append(item)

    return out
