import sqlite3
import random
from tkinter import *
from tkinter import ttk

class Quizzer(object):

    def __init__(self, number):
        self.question_list = []
        self.answer_list = []
        self.question_answer = {}
        self.target_answer = ''
        self.answered_questions= []
        self.number = number
        # set up the country and capital dict
        # country_list = []
        # capital_list = []
        # country_capital = {}
        # target_country = ''
        # question_list = []

        

        # connect to the database
        quizz_db="./country_database.db"
        connection=sqlite3.connect(quizz_db)
        cursor=connection.cursor()

        #create table
        #cursor.execute('''CREATE TABLE geography ( question text, answer text, has_capital real)''')
        #insert row of data
        cursor.execute("INSERT INTO geography VALUES('GR', 'ATH', 1)")
        cursor.execute("INSERT INTO geography VALUES('FR', 'PA', 1)")
        cursor.execute("INSERT INTO geography VALUES('GE', 'BE', 1)")
        cursor.execute("INSERT INTO geography VALUES('UK', 'LO', 1)")
        cursor.executemany("INSERT INTO geography VALUES (? , ?, 1)", self.question_answer)
        #cursor.execute('''CREATE TABLE history ( question text, answer text, has_capital real)''')
        #insert row of data
        cursor.execute("INSERT INTO history VALUES('h1', 'ATH', 1)")
        cursor.execute("INSERT INTO history VALUES('h2', 'PA', 1)")
        cursor.execute("INSERT INTO history VALUES('h3', 'BE', 1)")
        cursor.execute("INSERT INTO history VALUES('h4', 'LO', 1)")
        #save changes
        #connection.commit()

        # query the database and return all matching values
        if self.number == 0:
            cursor.execute('SELECT question FROM geography WHERE has_capital=1')
        else:
            cursor.execute('SELECT question FROM history WHERE has_capital=1')
        rows=cursor.fetchall()

        # iterate over the rows and put them into a list
        for x in rows:
            x = str(x)
            x = x[2:-3]
            self.question_list.append(x)

        # query the database and return all matching values
        if self.number == 0:
            cursor.execute('SELECT answer FROM qeography WHERE has_capital=1')
        else:
            cursor.execute('SELECT answer FROM history WHERE has_capital=1')

        for x in cursor:
            x = str(x)
            x = x[2:-3] #δευτερος μεχρι 4ος τελος
            #print(x)
            self.answer_list.append(x)

        # create the dict
        for x in range(len(self.question_list)):
            self.question_answer[self.question_list[x]] = self.answer_list[x]


    def get_question_list(self):
        random_answers = []
        question_answer = self.question_answer
        self.target_question = random.choice(list(self.question_answer.keys()))
        while self.target_question in self.answered_questions:
            self.target_question = random.choice(list(self.question_answer.keys()))
            if len(self.answered_questions) == len(self.question_answer):
                self.target_question = "NULL"
                
        self.answered_questions.append(self.target_question)
        
        if self.target_question == "NULL":
            random_answers.append("NULL")
        else:
            random_answers.append(self.question_answer[self.target_question])

        x = random.choice(list(self.question_answer.values()))
        # print(len(question_list))
        while len(random_answers) < 4:
            x = random.choice(list(self.question_answer.values()))
            if x in random_answers:
                pass
            else:
                random_answers.append(x)

        random.shuffle(random_answers)

        question_string = 'What is the capital of {}?'.format(self.target_question)

        return question_string, random_answers

        # print('What is the capital of {}?'.format(self.target_country))
        # print( 'A. {} \nB. {} \nC. {} \nD. {} \n'.format(
        # question_list[0], question_list[1], question_list[2], question_list[3]) )
        
        # i think maybe the gui class should be responsible for the text.
        # def get_label():
        #     label = ttk.Label(root, text = 
        #     target_string)
        #     label.config(justify = CENTER)
        #     # label.config(font = ('Calibri', 18, 'bold'))

        #     label.grid(row = 0, column = 1, columnspan = 4)
        #     label.grid(row=0, column=1, padx=20, pady=20)


    # def get_result(self, value):
    #     if value == self.country_capital[self.target_country]:
    #         return True
    #     else:
    #         return False


def main():


    blah = Quizzer(1)
    blah.get_question_list()

    meh = Quizzer(1)
    # print(meh.get_question_list())

    # print(blah.target_country)
    # print(blah.get_question_list())
    # blah.get_question_list()

    whatis = blah.get_question_list()
    # print(whatis)
    # print('target country: {}\n'.format(whatis[0]))
    
    # print(whatis[0])

    # print(whatis[1][0])
    # print(whatis[1][1])
    # print(whatis[1][2])
    # print(whatis[1][3])





    

if __name__ == '__main__':
    main()
