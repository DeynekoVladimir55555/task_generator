from flask import Flask, request, redirect, render_template, send_from_directory
import os
import DataBaseFile
import GenerationFile
import TranslateFunctions

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html')

@app.route('/training', methods=['GET', 'POST'])
def training():
    if request.method == 'GET':
        difficulty, types_str = DataBaseFile.load_settings()
        types = []
        if types_str[0] == 'True':
            types.append(1)
        if types_str[1] == 'True':
            types.append(2)
        task = GenerationFile.print_question(difficulty, types)
        task_id = DataBaseFile.insert_task(task[0], task[1])

        print(task)

        return render_template('training.html', question=task[0], task_id=task_id)
    elif request.method == 'POST':
        action = request.form.get('action')
        task_id = request.form.get('task_id')

        if action == 'skip':
            return redirect('/training')
        elif action == 'check':
            test = DataBaseFile.find(f'''SELECT answer, status FROM Tasks WHERE id={task_id}''')
            if test[0][1] == 1:
                return redirect('/')
            else:
                answer = request.form.get('answer')
                if answer == test[0][0]:
                    DataBaseFile.update_task_status(task_id, 1)
                else:
                    DataBaseFile.update_task_status(task_id, 0)
                return redirect(f'/result/{task_id}')
        else:
            return redirect('/')

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'GET':
        difficulty, types = TranslateFunctions.translate_to_ui(*DataBaseFile.load_settings())
        if 'on' not in types:
            types = ['on', 'on']
            DataBaseFile.update_settings(*TranslateFunctions.translate_to_db(difficulty, types))
        return render_template('settings.html', difficulty=difficulty, types=types)
    elif request.method == 'POST':
        difficulty = request.form.get('difficulty')
        types = [request.form.get('type_1'), request.form.get('type_2')]
        DataBaseFile.update_settings(*TranslateFunctions.translate_to_db(difficulty, types))
        return redirect('/settings')

@app.route('/stats', methods=['GET', 'POST'])
def stats():
    if request.method == 'GET':
        totals = DataBaseFile.load_statistics()
        return render_template('stats.html', success_total=totals[0], fail_total=totals[1], skip_total=totals[2])
    elif request.method == 'POST':
        mode = request.form.get('mode')
        if mode == 'clear_all':
            DataBaseFile.delete_all_stats()
        elif mode == 'clear_skipped_only':
            DataBaseFile.delete_skipped_stats()
        return redirect('/stats')

@app.route('/about', methods=['GET'])
def about():
    if request.method == 'GET':
        return render_template('about.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'), 'favicon.ico')

@app.route('/result/<task_id>', methods=['GET'])
def result(task_id):
    if request.method == 'GET':
        status = 'fail'
        test = DataBaseFile.find(f'''SELECT status FROM Tasks WHERE id={task_id}''')
        if test[0][0] == 1:
            status = 'success'
        return render_template('result.html', task_id=task_id, result=status)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
