import csv 
def exam_csv(file_path):
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]
            return data

def user_data(file_path):
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]
            return data
        
def exam(questions):
        score=0
        for question in questions:
            print(question['question'])
            answer = input('Your Answer: ')
            if answer == question['answer']:
               score+=1
        return score

users = user_data('/home/soham/ilearn-task/python/task-6/userdata.csv')
questions =  exam_csv('/home/soham/ilearn-task/python/task-6/exam.csv')

if questions and users:
    print("Welcome to the Exam!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username != "" and password != "":     
        username_data = (username for row in users if row['username'] == username)
        password_data = (password for row in users if row['password'] == password)
        if username_data and password_data:
            print(f"Hello, {username}!")
            counduct_exam = exam(questions)
            print(f'You scored {counduct_exam}/{len(questions)} points.')
        else:
            print("Invalid Input")
    else:
         print("please enter a both fields")