import random

def level1(): a=random.randint(1,5); return f"x^2 + {2*a}x + {a*a}", f"(x + {a})^2"
def level2(): a=random.randint(1,5); return f"x^2 - {2*a}x + {a*a}", f"(x - {a})^2"
def level3(): b=random.choice([2,4,6,8]); return f"x^2 + {b}x + {b*b//4}", f"(x + {b//2})^2"
def level4(): b=random.randint(3,7); c=b*b//4+random.randint(1,3); h=b/2; k=c - (b*b)/4; return f"x^2 + {b}x + {c}", f"(x + {h})^2 + {k}"
def level5(): a=random.randint(2,4); b=random.randint(1,4); return f"{a}x^2 + {2*a*b}x + {a*b*b}", f"{a}(x + {b})^2"
def level6(): a=random.randint(2,4); b=random.randint(1,4); return f"{a}x^2 - {2*a*b}x + {a*b*b}", f"{a}(x - {b})^2"
def level7(): a=random.randint(2,3); b=random.randint(2,6); c=(b*b)//(4*a)+random.randint(1,3); h=b/(2*a); k=c - (b*b)/(4*a); return f"{a}x^2 + {b}x + {c}", f"{a}(x + {h})^2 + {k}"
def level8(): a=random.randint(2,5); return f"-x^2 + {2*a}x - {a*a}", f"-(x - {a})^2"
def level9(): return "2x^2 + 6x + 5", "2(x + 1.5)^2 + 0.5"
def level10(): return "3x^2 - 12x + 13", "3(x - 2)^2 + 1"

templates = [level1, level2, level3, level4, level5, level6, level7, level8, level9, level10]