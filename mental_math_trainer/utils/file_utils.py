import os, re, datetime, subprocess, shutil

def format_date():
    return datetime.datetime.now().strftime("%d%m")

def get_next_file_number(date_str, folder="generated"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    pattern = re.compile(rf"tasks_{date_str}_(\d+)\.md")
    max_num = 0
    for f in os.listdir(folder):
        m = pattern.match(f)
        if m:
            num = int(m.group(1))
            if num > max_num:
                max_num = num
    return max_num + 1

def convert_to_pdf(md_path):
    if not shutil.which("pandoc"):
        print("Pandoc не найден. Установите pandoc (https://pandoc.org) и LaTeX.")
        return False
    cmd = ["pandoc", md_path, "-o", md_path.replace(".md", ".pdf"), "--pdf-engine=xelatex"]
    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True
    except:
        return False