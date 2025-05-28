from functools import reduce

def get_prices(store, products, sales):
    return tuple(map(lambda p: (p[0], p[1] - p[1] * dict(sales).get(store)), products))

def get_prices_dict(store, products, sales):
    return dict(map(lambda p: (p[0], p[1] - p[1] * sales.get(store)), tuple(products.items())))

def get_prices_by_type(store, products, sales, types):
    return dict(map(
        lambda p: (
            p[0],
            p[1] - p[1] * sales[store]['t1']
            if str(p[0]) in types['t1']
            else p[1] - p[1] * sales[store]['t2']
        ),
        products.items()
    ))

def prices_accumulate(store, products, sales, types, add):
    return add(reduce(add, get_prices_by_type(store, products, sales, types).values()), 0)