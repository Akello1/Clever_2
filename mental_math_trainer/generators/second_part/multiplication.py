import random

def level1(): a=random.randint(2,9); b=random.randint(2,9); return f"{a} \\times {b}", str(a*b)
def level2(): a=random.randint(2,9); b=random.randint(1,9); c=random.randint(0,9); return f"{a} \\times ({10*b + c})", str(a*(10*b+c))
def level3(): a,b,c,d=(random.randint(1,9) for _ in range(4)); return f"({10*a+b}) \\times ({10*c+d})", str((10*a+b)*(10*c+d))
def level4(): a=random.randint(2,5); b=random.randint(1,4); c=random.randint(0,9); d=random.randint(0,9); return f"{a} \\times ({100*b+10*c+d})", str(a*(100*b+10*c+d))
def level5(): a,b=(random.randint(1,9) for _ in range(2)); c=random.randint(1,3); d,e=(random.randint(0,9) for _ in range(2)); return f"({10*a+b}) \\times ({100*c+10*d+e})", str((10*a+b)*(100*c+10*d+e))
def level6(): a,c=random.randint(1,3),random.randint(1,3); b,d,e,f=(random.randint(0,9) for _ in range(4)); return f"({100*a+10*b+c}) \\times ({100*d+10*e+f})", str((100*a+10*b+c)*(100*d+10*e+f))
def level7(): a=random.randint(1,9); b=random.randint(0,9); c=random.randint(1,9); res=(a+b/10)*c; return f"{a}.{b} \\times {c}", f"{res:.1f}"
def level8(): a,c=random.randint(1,5),random.randint(1,5); b,d=random.randint(0,9),random.randint(0,9); res=(a+b/10)*(c+d/10); return f"{a}.{b} \\times {c}.{d}", f"{res:.2f}"
def level9(): a=random.randint(1,20); b=random.randint(1,20); return f"(100 - {a}) \\times (100 - {b})", str((100-a)*(100-b))
def level10(): x=round(random.uniform(10,50),1); y=round(random.uniform(10,50),1); return f"{x} \\times {y}", f"{x*y:.2f}"

templates = [level1, level2, level3, level4, level5, level6, level7, level8, level9, level10]