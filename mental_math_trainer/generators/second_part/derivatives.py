import random

def level1(): a=random.randint(2,9); b=random.randint(-5,5); return f"{a}x + {b}", str(a)
def level2(): a=random.randint(1,4); b=random.randint(-3,3); c=random.randint(-5,5); return f"{a}x^2 + {b}x + {c}", f"{2*a}x + {b}" if b!=0 else f"{2*a}x"
def level3(): k=random.randint(1,5); return f"\\sin({k}x)", f"{k}\\cos({k}x)"
def level4(): k=random.randint(1,5); return f"\\cos({k}x)", f"-{k}\\sin({k}x)"
def level5(): k=random.randint(1,3); return f"e^{{{k}x}}", f"{k}e^{{{k}x}}"
def level6(): k=random.randint(1,4); return f"\\ln({k}x)", "\\frac{1}{x}"
def level7(): a=random.randint(1,3); b=random.randint(-4,4); return f"{a}x^3 + {b}x", f"{3*a}x^2 + {b}" if b!=0 else f"{3*a}x^2"
def level8(): return "x \\sin x", "\\sin x + x \\cos x"
def level9():
    a,b,c,d = (random.randint(1,5) for _ in range(4))
    while a*d == b*c: a,b,c,d = (random.randint(1,5) for _ in range(4))
    num = a*d - b*c; denom = f"({c}x + {d})^2"
    return f"\\frac{{{a}x + {b}}}{{{c}x + {d}}}", f"\\frac{{{num}}}{{{denom}}}"
def level10(): a=random.randint(1,3); b=random.randint(-3,3); return f"\\sin({a}x^2 + {b})", f"{2*a}x \\cos({a}x^2 + {b})"

templates = [level1, level2, level3, level4, level5, level6, level7, level8, level9, level10]