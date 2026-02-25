import random

def level1(): a=random.randint(2,9); return str(a), f"{a}x"
def level2(): n=random.choice([2,3,4,5]); return f"x^{{{n}}}", f"\\frac{{x^{{{n+1}}}}}{{{n+1}}}"
def level3(): a=random.randint(1,5); b=random.randint(1,5); return f"{a}x + {b}", f"\\frac{{{a}x^2}}{{2}} + {b}x"
def level4(): k=random.randint(1,5); return f"\\sin({k}x)", f"-\\frac{{\\cos({k}x)}}{{{k}}}"
def level5(): k=random.randint(1,5); return f"\\cos({k}x)", f"\\frac{{\\sin({k}x)}}{{{k}}}"
def level6(): k=random.randint(1,3); return f"e^{{{k}x}}", f"\\frac{{e^{{{k}x}}}}{{{k}}}"
def level7(): return "\\frac{1}{x}", "\\ln|x|"
def level8(): a=random.randint(1,3); b=random.randint(-3,3); n=random.choice([2,3]); return f"({a}x + {b})^{{{n}}}", f"\\frac{{({a}x + {b})^{{{n+1}}}}}{{{a*(n+1)}}}"
def level9(): return "\\sin^2 x", "\\frac{x}{2} - \\frac{\\sin 2x}{4}"
def level10(): a=random.randint(1,4); b=random.randint(1,5); return f"\\frac{1}{{{a}x + {b}}}", f"\\frac{1}{{{a}}}\\ln|{a}x + {b}|"

templates = [level1, level2, level3, level4, level5, level6, level7, level8, level9, level10]