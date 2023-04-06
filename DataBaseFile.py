import sqlite3

con = sqlite3.connect("DataBase.db", check_same_thread=False)
cur = con.cursor()

# Поиск по базе данных
def find(operand):
    return cur.execute(operand).fetchall()

def load_settings():
    settings = find('''SELECT difficulty, type1, type2 FROM Settings''')[0]
    return settings[0], [settings[1], settings[2]]

# Получение статистики
def load_statistics():
    result_true = cur.execute('''SELECT id FROM Tasks WHERE status=1''').fetchall()
    result_false = cur.execute('''SELECT id FROM Tasks WHERE status=0''').fetchall()
    result_skip = cur.execute('''SELECT id FROM Tasks WHERE status is null''').fetchall()

    true_total = len(result_true)
    false_total = len(result_false)
    skip_total = len(result_skip)

    return [true_total, false_total, skip_total]

# Сохранение настроек при изменении
def update_settings(difficulty, types):
    cur.execute('''UPDATE Settings
                    SET difficulty = ?,
                        type1 = ?,
                        type2 = ?''', (difficulty, str(types[0]), str(types[1])))
    con.commit()

# Очистка статистики
def delete_all_stats():
    cur.execute('''DELETE from Tasks''')
    con.commit()

def delete_skipped_stats():
    cur.execute('''DELETE from Tasks WHERE status is null''')
    con.commit()

def insert_task(question, answer):
    cur.execute('''INSERT INTO Tasks(question, answer) VALUES(?, ?)''', (question, answer))
    con.commit()
    return cur.lastrowid

def update_task_status(id, status):
    cur.execute('''UPDATE Tasks SET status=? WHERE id=?''', (status, id))
    con.commit()