def build_tasks_md(first_tasks, second_tasks, topic_name):
    lines = ["# Тренировка устного счета\n", "Решите задачи и запишите ответы в отведенные поля.\n", "<table>"]
    lines.append("  <tr>\n    <th>Задачи 1–10</th>\n    <th>Ответы 1–10</th>\n    <th>Задачи 11–20 (" + topic_name + ")</th>\n    <th>Ответы 11–20</th>\n  </tr>")
    lines.append("  <tr>")
    t1 = "<br>".join([f"{i+1}. ${first_tasks[i][0]}$" for i in range(10)])
    a1 = "<br>".join([f"{i+1}. " for i in range(10)])
    t2 = "<br>".join([f"{i+11}. ${second_tasks[i][0]}$" for i in range(10)])
    a2 = "<br>".join([f"{i+11}. " for i in range(10)])
    lines.append(f"    <td>{t1}</td>\n    <td>{a1}</td>\n    <td>{t2}</td>\n    <td>{a2}</td>")
    lines.append("  </tr>\n</table>")
    return "\n".join(lines)

def build_answers_md(first_tasks, second_tasks):
    lines = ["# Ответы к тренировке устного счета\n", "<table>"]
    lines.append("  <tr>\n    <th>Ответы 1–10</th>\n    <th>Ответы 11–20</th>\n  </tr>")
    lines.append("  <tr>")
    a1 = "<br>".join([f"{i+1}. ${first_tasks[i][1]}$" for i in range(10)])
    a2 = "<br>".join([f"{i+11}. ${second_tasks[i][1]}$" for i in range(10)])
    lines.append(f"    <td>{a1}</td>\n    <td>{a2}</td>")
    lines.append("  </tr>\n</table>")
    return "\n".join(lines)