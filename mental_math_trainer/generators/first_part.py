import random

def level1():
    a = random.randint(2, 9); b = random.randint(2, 9)
    return f"{a} \\times {b}", str(a*b)

def level2():
    a = random.randint(10, 50); b = random.randint(10, 50)
    return f"{a} + {b}", str(a+b)

def level3():
    a = random.randint(20, 99); b = random.randint(10, a-10)
    return f"{a} - {b}", str(a-b)

def level4():
    a = random.randint(2, 9); b = random.choice([10, 100])
    return f"{a} \\times {b}", str(a*b)

def level5():
    a = random.randint(10, 99); b = random.randint(2, 9)
    return f"{a} \\times {b}", str(a*b)

def level6():
    a = random.randint(2, 9); b = random.randint(2, 9)
    return f"{a*b} : {a}", str(b)

def level7():
    angle = random.choice([30,45,60]); func = random.choice(["sin","cos"])
    if angle==30: val = "\\frac{1}{2}" if func=="sin" else "\\frac{\\sqrt{3}}{2}"
    elif angle==45: val = "\\frac{\\sqrt{2}}{2}"
    else: val = "\\frac{\\sqrt{3}}{2}" if func=="sin" else "\\frac{1}{2}"
    return f"\\{func} {angle}^\\circ", val

def level8():
    a = random.randint(20,200)
    return f"10\\% \\text{{ от }} {a}", str(a/10)

def level9():
    a = random.randint(5,15)
    return f"{a}^2", str(a*a)

def level10():
    a = random.randint(2,12)
    return f"\\sqrt{{{a*a}}}", str(a)

first_part_generators = [level1, level2, level3, level4, level5,
                         level6, level7, level8, level9, level10]

def generate_first_part():
    return [gen() for gen in first_part_generators]