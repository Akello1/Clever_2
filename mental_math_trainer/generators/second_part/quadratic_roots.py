import random, math

def level1(): a=random.randint(2,7); return f"x^2 - {a*a} = 0", f"\\pm {a}"
def level2(): a=random.randint(3,8); return f"x^2 - {a}x = 0", f"0,\\; {a}"
def level3():
    a=random.randint(1,5); b=random.randint(1,5); while(a==b): b=random.randint(1,5); return f"x^2 - {a+b}x + {a*b} = 0", f"{a},\\; {b}"
def level4():
    a=random.randint(2,6); return f"x^2 - {2*a}x + {a*a} = 0", f"{a}"
def level5():
    a=random.randint(2,10); while int(math.sqrt(a))**2==a: a=random.randint(2,10); return f"x^2 - {a} = 0", f"\\pm \\sqrt{{{a}}}"
def level6(): a=random.randint(2,5); b=random.randint(2,5); return f"{a}x^2 - {a+b}x + {b} = 0", f"1,\\; \\frac{{{b}}}{{{a}}}"
def level7(): a=random.randint(2,4); return f"x^2 - ({a}+1/{a})x + 1 = 0", f"{a},\\; \\frac{{1}}{{{a}}}"
def level8():
    p=random.choice([0.5,1.5,2.5,3.5]); q=random.choice([0.5,1.5,2.5,3.5]); while p==q: q=random.choice([0.5,1.5,2.5,3.5]); return f"x^2 - ({p}+{q})x + {p*q} = 0", f"{p},\\; {q}"
def level9(): return "x^4 - 5x^2 + 4 = 0", "\\pm 1,\\; \\pm 2"
def level10(): return "6x^2 - 13x + 6 = 0", "\\frac{2}{3},\\; \\frac{3}{2}"

templates = [level1, level2, level3, level4, level5, level6, level7, level8, level9, level10]