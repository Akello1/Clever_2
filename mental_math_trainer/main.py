import os
from generators.first_part import generate_first_part
from generators.second_part import derivatives, antiderivatives, multiplication, square_completion, quadratic_roots
from formatters.markdown_formatter import build_tasks_md, build_answers_md
from utils.file_utils import format_date, get_next_file_number, convert_to_pdf

topics = {
    "1": ("Производные", derivatives.templates),
    "2": ("Первообразные", antiderivatives.templates),
    "3": ("Сложное умножение", multiplication.templates),
    "4": ("Выделение полного квадрата", square_completion.templates),
    "5": ("Корни квадратного уравнения", quadratic_roots.templates)
}


def generate_second_part(templates):
    tasks = []
    for gen in templates:
        task, answer = gen()
        tasks.append((task, answer))
    return tasks


def main():
    print("=== Генератор задач для устного счета ===")
    while True:
        print("\nВыберите тему для второй части (11–20):")
        print("1. Производные")
        print("2. Первообразные")
        print("3. Сложное умножение")
        print("4. Выделение полного квадрата")
        print("5. Корни квадратного уравнения")
        choice = input("Введите номер (1-5): ").strip()

        if choice not in topics:
            print("Неверный выбор. Попробуйте снова.")
            continue

        topic_name, templates = topics[choice]
        first = generate_first_part()
        second = generate_second_part(templates)

        date_str = format_date()
        next_num = get_next_file_number(date_str)
        tasks_filename = f"tasks_{date_str}_{next_num}.md"
        answers_filename = f"answers_{date_str}_{next_num}.md"

        tasks_path = os.path.join("generated", tasks_filename)
        answers_path = os.path.join("generated", answers_filename)

        tasks_content = build_tasks_md(first, second, topic_name)
        answers_content = build_answers_md(first, second)

        with open(tasks_path, "w", encoding="utf-8") as f:
            f.write(tasks_content)
        with open(answers_path, "w", encoding="utf-8") as f:
            f.write(answers_content)

        print(f"\nФайлы сохранены в папке 'generated':")
        print(f"  {tasks_filename}")
        print(f"  {answers_filename}")

        if input("\nСоздать PDF для обоих файлов? (y/n): ").strip().lower() == 'y':
            print("Конвертация tasks.md...")
            if convert_to_pdf(tasks_path):
                print(f"  PDF сохранён: {tasks_filename.replace('.md', '.pdf')}")
            print("Конвертация answers.md...")
            if convert_to_pdf(answers_path):
                print(f"  PDF сохранён: {answers_filename.replace('.md', '.pdf')}")

        cmd = input("\nНажмите Enter для выхода или введите 'new' для новой генерации: ").strip().lower()
        if cmd != 'new':
            break


if __name__ == "__main__":
    if not os.path.exists("generated"):
        os.makedirs("generated")
    main()