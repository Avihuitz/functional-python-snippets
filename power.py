def make_power(base, pow):

    def get_base(): return base
    def get_pow(): return pow

    def print_power():

        if pow == 0: return "1"
        elif pow == 1: return str(base)
        else: return f"{base}^{pow}"

    def calc_power(): return base ** pow

    def mul_power(other):

        b2, p2 = other("base"), other("power")
        if base == b2: return make_power(base, pow + p2)
        return make_power(calc_power() * other("calc_power"), 1)

    def div_power(other):

        b2, p2 = other("base"), other("power")
        if base == b2: return make_power(base, pow - p2)
        return make_power(calc_power() / other("calc_power"), 1)

    def improve_power():
        for root in range(2, base):
            k, value = 1, root
            while value < base:
                value *= root
                k += 1
            if value == base:
                return make_power(root, pow * k)
        return dispatch

    def dispatch(msg):
        return {
            "base": get_base,
            "power": get_pow,
            "print_power": print_power,
            "calc_power": calc_power,
            "mul_power": lambda: mul_power,
            "div_power": lambda: div_power,
            "improve_power": improve_power
        }.get(msg, lambda: "unknown command")()

    return dispatch

def base(x): return x("base")
def power(x): return x("power")
def print_power(x): return x("print_power")
def calc_power(x): return x("calc_power")
def mul_power(x, y): return x("mul_power")(y)
def div_power(x, y): return x("div_power")(y)
def improve_power(x): return x("improve_power")