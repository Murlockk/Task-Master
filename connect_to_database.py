import sqlite3 as sql

con = sql.connect('Task_master.db')
cur = con.cursor()


def create_database():
    '''
    Функция создания базы данных
    :return:
    '''

    cur.execute('PRAGMA foreign_key = ON')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    post VARCHAR(100),
    mail VARCHAR(50),
    password VARCHAR(30)
    )''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    description TEXT,
    status INTEGER,
    create_date_time DATETIME,
    deadline_date_time DATETIME
    )''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Project_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project INTEGER,
    user INTEGER,
    FOREIGN KEY (project) REFERENCES Projects (id) ON DELETE CASCADE,
    FOREIGN KEY (user) REFERENCES Users (id) ON DELETE CASCADE
    )''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS  Tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    main_task INTEGER,
    description TEXT,
    status INTEGER,
    create_date_time DATETIME,
    deadline_date_time DATETIME
    )''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Task_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user INTEGER,
    task INTEGER,
    FOREIGN KEY (user) REFERENCES Users (id),
    FOREIGN KEY (task) REFERENCES Tasks (id)
    )''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Project_tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project INTEGER,
    task INTEGER,
    FOREIGN KEY (project) REFERENCES Projects (id),
    FOREIGN KEY (task) REFERENCES Tasks (id)
    )''')

    print('done')

def login_in_account(login:str, password:str):
    '''
    Функция поиска пользователя по логину и паролю
    :param login: email
    :param password: password
    :return: Flase - если пользователя с такими параметрами нет / id - номер пользователя если таковой существует
    '''
    cur.execute(f'SELECT id FROM Users WHERE mail = "{login}" AND password = "{password}"')
    answer = cur.fetchall()
    if answer:
        # print(answer[0][0])
        return answer[0][0]
    else:
        return False


def create_account(name:str, post:str, mail:str, password:str):
    cur.execute('''
    INSERT INTO Users (name, post, mail, password) VALUES (?,?,?,?)
    ''', (name, post, mail, password))
    con.commit()


def registration_valid(email:str):
    '''
    валидация при регистрации нового пользователя
    :param email: почта нового пользователя
    :return: False - если пользователь с такой почтой уже существует / True - если пользователя с такой почтой не существует
    '''
    cur.execute(f'SELECT id FROM Users WHERE mail = "{email}"')
    answer = cur.fetchall()
    if answer:
        return False
    else:
        return True

def select_user_name(user_id):
    cur.execute(f'SELECT name FROM Users WHERE id = "{user_id}"')
    answer = cur.fetchall()
    return answer[0][0]

def select_users_projects(user_id):
    cur.execute(f'''SELECT Projects.id, name, description, status FROM Projects 
    JOIN Project_users ON Projects.id = project_users.project
    WHERE Project_users.user = "{user_id}"''')
    answer = cur.fetchall()
    ids = []

    for i in range(len(answer)):
        ids.append(answer[i][0])

    return answer, ids

def delete_task(id):
    cur.execute(f'''DELETE FROM Tasks WHERE id = "{id}"''')
    print('done')
    con.commit()


def select_project_tasks(project_id):
    cur.execute(f'''SELECT Tasks.id, name, description, status FROM Tasks
    JOIN Project_tasks ON Project_tasks.task = Tasks.id
    WHERE Project_tasks.project = "{project_id}"''')
    answer = cur.fetchall()
    return answer


def update_task(id):
    # функция обращения к базе данных
    pass
