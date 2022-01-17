import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sq
import tkinter.constants as const
import random as rd

user1=None


username=""
password=""
playerview=[]
usedque=[]

data = sq.connect('maindata.db')
score1=0
wrong=0
score=0
count=0
q=[]


#Κλαση που χρησιμοποιειται σε συνδυασμο με την κλαση Users για την δημιουργια ενος αντικειμενου που αναπαριστα τον ενεργο χρηστη το
def auser(username,password):
        cursor=data.cursor()
        auser="SELECT * FROM Users WHERE username='"+ username + "'" + "AND password='" + password + "'"
        auser1=cursor.execute(auser).fetchall()
        
        return Users(auser1[0][0],auser1[0][1],auser1[0][2],auser1[0][3])



class Users:
    def __init__(self,id,username,password,highscore):
        self.id=id
        self.username=username
        self.password=password
        self.highscore=highscore
    def __str__(self):
        return 'fghfghfghgf'+ self.username + self.password

class Login():
    
    
    def btn_clicked(self):
        global username
        global password
        global user1
        username=self.entry1.get()
        password=self.entry0.get()
        if username=="":
            pass
        else:
                data1=(username,password)
                cursor=data.cursor()
                #cursor.execute('''CREATE TABLE Users ( username text, password text)''')
                userlist="SELECT * FROM Users WHERE username='"+ username + "'"
                
                count=cursor.execute(userlist).fetchall()
                if len(count)==0:
                    insert="INSERT INTO Users(username,password) VALUES(?,?)"
                    entry=data.execute(insert,data1)
                    data.commit()
                    messagebox.showinfo("Επιτυχια","Επιτυχης Εγγραφη")
                    user1=auser(username,password)
                    self.canvas.delete('all')
                    MainWindow=MainWin(root)
                    
                else:
                    passwords="SELECT password FROM Users WHERE username='"+ username + "'"
                    count1=cursor.execute(passwords).fetchall()
                    
                    if count1[0][0]==str(password):
                        messagebox.showinfo("Επιτυχια","Επιτυχης Συνδεση")
                        
                        user1=auser(username,password)
                        self.canvas.delete('all')
                        MainWindow=MainWin(root)
                    
                    

                    else:
                        messagebox.showinfo("Απιτυχια","Αποτυχημενη Εγγραφη")
                
        
        
        
                
                
                
        
        data.commit()
        
    
    def __init__(self,root):
        root.title("Εισοδος λογαριασμου")
        root.resizable(False,False)
        root.geometry("1280x720")
        
        self.canvas = tk.Canvas( root ,bg="#3E4243", height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")

        self.canvas.place(x = 0, y = 0)
        
        self.entry0_img = tk.PhotoImage(file = f"img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(640.0, 431.5,image = self.entry0_img)
        self.entry0 = tk.Entry(bd = 0,bg = "#FFC700",highlightthickness = 0,font = ("LexendDeca-Regular", 16))
        self.entry0['show']='*'
        self.entry0.place(x = 500.0, y = 409,width = 280.0,height = 43)
        self.entry1_img = tk.PhotoImage(file = "img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(640.0, 354.5,image = self.entry1_img)
        self.entry1 =tk.Entry(bd = 0,bg = "#FFC700",highlightthickness = 0,font = ("LexendDeca-Regular", 16))
        self.entry1.place(x = 500.0, y = 332,width = 280.0,height = 43)
        
        b0 = tk.Button(self.canvas,text="Εισοδος",bg = "#FFC700",borderwidth = 0,highlightthickness = 0,command = self.btn_clicked,relief = "flat",font = ("LexendDeca-Regular", 16),fg="#ffffff")
        b0.place(x = 490, y = 585,width = 300,height = 45)
         
        
       
        self.canvas.create_text(420, 355.0,text = "Ονομα χρηστη",fill = "#ffffff",font = ("LexendDeca-Regular", 16))
        self.canvas.create_text(420, 432.0,text = "Κωδικος",fill = "#ffffff",font = ("LexendDeca-Regular", 16))
        self.canvas.create_text(640,157,text="Quiz Ομαδας 23",fill="#FFC700",font=("LexendDeca-Regular", 24))
        self.backgroundimg = tk.PhotoImage(file = "background.png")
        background = self.canvas.create_image(640,350,image=self.backgroundimg)

class MainWin():
    global playerview

    def Players(self):
        
        cursor = data.cursor()
        Players=cursor.execute("SELECT * FROM Users").fetchall()
        
        
        for r in Players:
            p=Users(r[0],r[1],r[2],r[3])
            
            playerview.append(p)
        
        View()
            


    def __init__(self,master):
        self.master=master
        options1=["Ανοιχτου τυπου ερωτησεις","Πολλαπλης επιλογης"]
        self.clicked1=tk.StringVar()
        self.clicked1.set(options1[0])
        self.master.title("Επιλογες")
        self.master.resizable(False,False)
        self.master.geometry("1280x720")
        self.master.configure(bg = "#3e4243")
        self.canvas = tk.Canvas(self.master,bg = "#3e4243",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
        self.canvas.place(x = 0, y = 0) 
        self.background_img1 = tk.PhotoImage(file = "background1.png")
        label1 = tk.Label(self.master,bg="#3e4243", image=self.background_img1)
        label1.place(x = 0, y = 0)
        b01 = tk.Button(self.master,bg="#FFC700",text="Εξοδος",fg="black",font = ("LexendDeca-Regular", 16),borderwidth = 0,highlightthickness = 0,width = 140,height = 45,command = self.close,relief = "flat")
        b01.place(x = 57, y = 642,width = 140,height = 45)
        
        b11 = tk.Button(self.master,bg="#FFC700",text="Παικτες",fg="black",font = ("LexendDeca-Regular", 16),borderwidth = 0,highlightthickness = 0,width = 300,height = 75,command = self.Players,relief = "flat")
        b11.place(x = 490, y = 534,width = 300,height = 75)
        
        b21 = tk.Button(self.master,bg="#FFC700",text="Ξεκινα",borderwidth = 0,fg="black",font = ("LexendDeca-Regular", 16),highlightthickness = 0,width = 300,height = 75,command = self.Play,relief = "flat")
        b21.place(x = 490, y =383,width = 300,height = 75)
        ttk.Style().configure("TMenubutton", background="#FFC700",font = ("LexendDeca-Regular", 16))
        self.combobox1=ttk.OptionMenu(self.master,self.clicked1,options1[0],*options1).place(x=490,y=232,width=300,height=75)
           
    def close(self):
        self.master.destroy()
    def Play(self):
        self.category=self.clicked1.get()
        if self.category=="Ανοιχτου τυπου ερωτησεις":
            main2(self.master)
        if self.category=="Πολλαπλης επιλογης":
            Menu=PlayMenu(self.master)

        
        
        

   
    
class View():   
    def __init__(self):
        global playerview
        root=tk.Tk()
        
        root.title("Παικτες")
        style=ttk.Style(root)
        style.configure("Treeview",background="#3e4243",foreground="#FFC700",fieldbackground="black",font=("LexendDeca-Regular", 16))
        style.map('Treeview',background=[('selected','#FFC700')])
         
        tree=ttk.Treeview(root)
        tree['columns']=("id","username","highscore")
        tree.column("#0",width=0,anchor=const.CENTER,stretch=False)
        tree.column("id",width=120,anchor=const.W)
        
        tree.column("username",width=120,anchor=const.CENTER)
        
        tree.column("highscore",width=120,anchor=const.CENTER)
        
        tree.heading("#0",text="",anchor=const.CENTER)
        tree.heading("id",text="ID",anchor=const.W)
        tree.heading("username",text="Username",anchor=const.CENTER)
        tree.heading("highscore",text="Highscore",anchor=const.CENTER)
        tree.pack()
        for p in playerview:
            tree.insert(parent='',index='end',text='',values=(p.id,p.username,p.highscore))
        playerview=[]
        
            
        root.mainloop()

    
class PlayMenu():

    def __init__(self,window):
        self.window=window
        window.title("Menu Πολλαπλης επιλογης ")
        window.geometry("1280x720")
        
        self.background_img1 = tk.PhotoImage(file = "background1.png")
        label11 = tk.Label(self.window,bg="#3e4243", image=self.background_img1)
        label11.place(x = 0, y = 0)
        
        options1=["Γεωγραφια","Ιστορια"]
        
        
        self.clicked1=tk.StringVar()
        
        
        self.clicked1.set(options1[0])
        
        
        ttk.Style().configure("TMenubutton", background="#FFC700",font = ("LexendDeca-Regular", 24))
        
        
        
        self.combobox1=ttk.OptionMenu(self.window,self.clicked1,options1[0],*options1).place(relx=0.5,rely=0.3,width=400,height=75,anchor=const.CENTER)
        
        self.b2=tk.Button(self.window,text="Εναρξη",bg="#FFC700",command=self.beginplay,font = ("LexendDeca-Regular", 16)).place(relx=0.5,rely=0.5,width=200,height=45,anchor=const.CENTER)
        
        
    
    def beginplay(self):
        if self.clicked1.get() == 'Γεωγραφια':
            main4(self.window)
        else:
            main3(self.window)

        
#------------------------------------------------------------------------------------------------------------------------------------------#


    
class MyQuiz2():
    count=0
    def questionm(self):
        global usedque
        while True:
            
            randomq1='SELECT que FROM Que'
            cur = data.cursor()
            randomq2=cur.execute(randomq1).fetchall()
            
            q = rd.choice(randomq2)
            
        
        
            if q[0] in usedque:
                continue
            else:
                
                usedque.append(q[0])
                
                
                break
        return q
    
    def __init__(self,master):
        global score
        global wrong
        global q
        
        
        q=self.questionm()
        



       #GRAPHICS START
        #Create one window
        

        #Add me image to virable
        self.my_image_bg = tk.PhotoImage(file='background1.png')

        #Create canvas
        self.master=master
        self.my_canvas = tk.Canvas(self.master, width=1280, height=720,bg="#3e4243")
        self.my_canvas.place(relx=0.0, rely=0.0)
        self.quest = tk.StringVar(self.master, name ="str")
        master.setvar(name ="str", value =q[0])

        self.my_canvas.create_image(0, 0, image=self.my_image_bg, anchor="nw")
        #Add Label to Canvas
        self.question=self.my_canvas.create_text(600, 330, text=q[0], font=("LexendDeca-Regular", 16), fill="Black")
        
        #Add Score to Canvas
        self.score_label = self.my_canvas.create_text(70, 15, text=f"Το Score σου είναι: {score}", font=("LexendDeca-Regular", 16))

        #Add Entry
        self.entry1 = tk.Entry(self.master, font="Arial 20", width=18, bg="#FFC700")
        self.entry1_canvas = self.my_canvas.create_window(400, 377, anchor="nw", window=self.entry1)

        #Add button
        self.button_entry1 = tk.Button(self.master,text="Υποβολή", command=self.checkAnswer, font="Arial 15", bg="#FFC700")
        self.button_entry1_canvas = self.my_canvas.create_window(700,375, anchor="nw", window=self.button_entry1)

        # Add Wrongs to Canvas
        self.wrong_label = self.my_canvas.create_text(1095, 15, text=f"Έχεις κάνει {wrong} λανθασμένες απαντήσεις.",font=("LexendDeca-Regular", 16))

        #Add Enter button command
        self.master.bind("<Return>", self.checkAnswer)

        
        
        
        
        
    
    def roundStarts(self):
        global count
        global usedque
        global wrong
        global score
        global user1
        global username
        global password
        
        
        count=count + 1
        
        if count == 5 or wrong ==3:

            finalscoreval=int(score)-int(wrong)

            cursor=data.cursor()
                
            if user1.highscore==None:
                highscore1=0
            else:
                highscore1=user1.highscore

                
                
            finalscore1=int(highscore1) + finalscoreval

            finalscore1str="UPDATE Users SET highscore ='" + str(finalscore1) + "'" + "WHERE username='" + str(user1.username) + "'"
            finalscore1=cursor.execute(finalscore1str)
            data.commit()
            
            score=0
            wrong=0
            count=0
            
            
            
            
            user1=auser(username,password)

            usedque=[]
            self.my_canvas.delete('all')
            main1(self.master)
            
            
    
    def checkAnswer(self, event=0):
        
        global score
        global wrong
        global q
        answer = self.entry1.get()
        
        cur = data.cursor()
        
        answers="SELECT ans FROM Que WHERE que='"+ q[0] + "'"
        answers1=cur.execute(answers).fetchall()
        
        
        answers2 = ''
        for i in answers1[0]:
            answers2 = answers2 + i
        
        
        if answer=='':
            pass
                
                
        elif str(answer) in str(answers2):
            
            messagebox.showinfo("Σωστη!","Σωστη Απαντηση")
            score += 1
            self.entry1.delete(0, 'end')
            self.my_canvas.delete(self.score_label)
            q=self.questionm()
            self.my_canvas.delete(self.question)
            self.question=self.my_canvas.create_text(600, 340, text=q[0], font=("LexendDeca-Regular", 16), fill="Black")
            self.score_label = self.my_canvas.create_text(70, 15, text=f"Το Score σου είναι: {score}",font=("LexendDeca-Regular", 16))
            self.roundStarts()
            
            
            
        else:
            messagebox.showinfo("Λαθος!","Λαθος Απαντηση")
            wrong += 1


            self.entry1.delete(0, 'end')
            self.my_canvas.delete(self.wrong_label)
            
            q=self.questionm()
            self.my_canvas.delete(self.question)
            self.question=self.my_canvas.create_text(600, 340, text=q[0], font=("LexendDeca-Regular", 16), fill="Black")
            self.wrong_label = self.my_canvas.create_text(1095, 15,text=f"Έχεις κάνει {wrong} λανθασμένες απαντήσεις.",font=("LexendDeca-Regular", 16))
            
            self.roundStarts()
    
def main2(master):
    quiz2=MyQuiz2(master)
    #quiz2.show_start()
def main1(master):
    MainWindow=MainWin(master)
def main4(master):
    blah = Feedback(master,0)
    blah.show_start()
def main3(master):
    blah = Feedback(master,1)
    blah.show_start()
    
    
    
        
#----------------------------------------------------------------------------------------------------------------------------------------#        
class Quizzer(object):

    def __init__(self, number):
        self.question_list = []
        self.answer_list = []
        self.question_answer = {}
        self.target_answer = ''
        self.answered_questions = []
        self.number = number

        # connect to the database
        quizz_db = "./country_database.db"
        connection = sq.connect(quizz_db)
        cursor = connection.cursor()

        # create table
        # cursor.execute('''CREATE TABLE geography ( question text, answer text, has_capital real)''')
        # insert row of data
        cursor.execute("INSERT INTO geography VALUES('πρωτεύουσα της Ελλάδας', 'Αθήνα', 1)")
        cursor.execute("INSERT INTO geography VALUES('πρωτεύουσα της Γαλλίας', 'Παρίσι', 1)")
        cursor.execute("INSERT INTO geography VALUES('πρωτεύουσα της Γερμανίας', 'Βερολίνο', 1)")
        cursor.execute("INSERT INTO geography VALUES('πρωτεύουσα της Μεγάλης Βρετανίας', 'Λονδίνο', 1)")
        cursor.execute("INSERT INTO geography VALUES('πρωτεύουσα της Ισπανίας', 'Μαδρίτη', 1)")
        #cursor.executemany("INSERT INTO geography VALUES (? , ?, 1)", self.question_answer)
        # cursor.execute('''CREATE TABLE history ( question text, answer text, has_capital real)''')
        # insert row of data
        cursor.execute("INSERT INTO history VALUES('ημερομηνία της Ναυμαχίας της Σαλαμίνας', '480 π.Χ', 1)")
        cursor.execute("INSERT INTO history VALUES('ημερομηνία της Μάχης του Μαραθώνα', '490 π.Χ', 1)")
        cursor.execute("INSERT INTO history VALUES('ημερομηνία της Μάχης των Πλαταιών', '479 π.Χ', 1)")
        cursor.execute("INSERT INTO history VALUES('ημερομηνία της Ναυμαχίας της Ναυπάκτου', '429 π.Χ', 1)")
        cursor.execute("INSERT INTO history VALUES('ημερομηνία της Μάχης της Χαιρώνειας', '338 π.Χ', 1)")
        # save changes
        #connection.commit()

        # query the database and return all matching values
        if self.number == 0:
            cursor.execute('SELECT question FROM geography WHERE has_capital=1')
        else:
            cursor.execute('SELECT question FROM history WHERE has_capital=1')
        rows = cursor.fetchall()

        # iterate over the rows and put them into a list
        for x in rows:
            x = str(x)
            x = x[2:-3]
            self.question_list.append(x)

        # query the database and return all matching values
        if self.number == 0:
            cursor.execute('SELECT answer FROM geography WHERE has_capital=1')
        else:
            cursor.execute('SELECT answer FROM history WHERE has_capital=1')

        for x in cursor:
            x = str(x)
            x = x[2:-3]  # δευτερος μεχρι 4ος απο τελος
            self.answer_list.append(x)

        # create the dict
        for x in range(len(self.question_list)):
            self.question_answer[self.question_list[x]] = self.answer_list[x]

    def get_question_list(self):
        random_answers = []
        question_answer = self.question_answer
        self.target_question = rd.choice(list(self.question_answer.keys()))
        while self.target_question in self.answered_questions:
            self.target_question = rd.choice(list(self.question_answer.keys()))
            if len(self.answered_questions) == len(self.question_answer):
                self.target_question = "NULL"

        self.answered_questions.append(self.target_question)

        if self.target_question == "NULL":
            random_answers.append("NULL")
        else:
            random_answers.append(self.question_answer[self.target_question])

        x = rd.choice(list(self.question_answer.values()))
        while len(random_answers) < 4:
            x = rd.choice(list(self.question_answer.values()))
            if x in random_answers:
                pass
            else:
                random_answers.append(x)

        rd.shuffle(random_answers)

        question_string = 'Ποια είναι η {}?'.format(self.target_question)

        return question_string, random_answers
    
class Feedback():
    
    def __init__(self,master,number):
        global score
        self.master = master
        self.label_text = None
        self.blah = Quizzer(number)
        score = 0
        self.master.resizable(False, False)
        self.master.geometry("1280x720")
        self.master.configure(bg="#3e4243")
        self.canvas = tk.Canvas(self.master, bg="#3e4243", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.background_img1 = tk.PhotoImage(file="background1.png")
        self.canvas.create_image(0, 0, image=self.background_img1, anchor="nw")

    def show_start(self):
        self.master.title("Quiz")
        self.master.resizable(False, False)
        self.master.geometry("1280x720")
        self.master.configure(bg="#3e4243")
        self.canvas = tk.Canvas(self.master, bg="#3e4243", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.background_img1 = tk.PhotoImage(file="background1.png")
        self.canvas.create_image(0, 0, image=self.background_img1, anchor="nw")
        self.canvas.create_text(600, 100.0, text="Καλησπέρα.\n Αυτό είναι ένα μικρό κουίζ γενικών γνώσεων. ", fill="#ffffff", font=("LexendDeca-Regular", 16))
        button_continue = tk.Button(self.canvas,text="Εισοδος",bg = "#FFC700",borderwidth = 0,highlightthickness = 0,command = self.show_questions,relief = "flat",font = ("LexendDeca-Regular", 16),fg="#ffffff")
        button_continue.place(x=400, y=285, width=300, height=45)
        button_quit = tk.Button(self.canvas,text="Εξoδος",bg = "#FFC700",borderwidth = 0,highlightthickness = 0,command = self.master.destroy,relief = "flat",font = ("LexendDeca-Regular", 16),fg="#ffffff")
        button_quit.place(x=400, y=385, width=300, height=45)
    def show_questions(self):
        global score1
        # Set the questions up.
        whatis = self.blah.get_question_list()
        # check country here
        question_text = whatis[0]
        button_a_text = whatis[1][0]
        button_b_text = whatis[1][1]
        button_c_text = whatis[1][2]
        button_d_text = whatis[1][3]
        self.master.title("Ερωτησεις")
        self.master.resizable(False, False)
        self.master.geometry("1280x720")
        self.master.configure(bg="#3e4243")
        self.canvas = tk.Canvas(self.master, bg="#3e4243", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.background_img1 = tk.PhotoImage(file="background1.png")
        self.canvas.create_image(0, 0, image=self.background_img1, anchor="nw")
        self.canvas.create_text(100, 100.0,text='Score:{}'.format(score1), fill="#ffffff", font=("LexendDeca-Regular", 16))
        self.canvas.create_text(600, 100.0,text=question_text,fill="#ffffff", font=("LexendDeca-Regular", 16))

        if question_text == 'Ποια είναι η {}?'.format("NULL"):
            self.showend()
            return

        button_a = tk.Button(self.canvas, text=button_a_text, bg="#FFC700", borderwidth=0, highlightthickness=0,
                                    command=lambda : self.check_win(button_a_text), relief="flat", font=("LexendDeca-Regular", 16),
                                    fg="#ffffff")
        button_a.place(x=500, y=185, width=300, height=45)
        button_b= tk.Button(self.canvas, text=button_b_text, bg="#FFC700", borderwidth=0, highlightthickness=0,
                                    command=lambda :self.check_win(button_b_text), relief="flat", font=("LexendDeca-Regular", 16),
                                    fg="#ffffff")
        button_b.place(x=500, y=285, width=300, height=45)
        button_c= tk.Button(self.canvas, text=button_c_text, bg="#FFC700", borderwidth=0, highlightthickness=0,
                                    command=lambda :self.check_win(button_c_text), relief="flat", font=("LexendDeca-Regular", 16),
                                    fg="#ffffff")
        button_c.place(x=500, y=385, width=300, height=45)
        button_d= tk.Button(self.canvas, text=button_d_text, bg="#FFC700", borderwidth=0, highlightthickness=0,
                                    command=lambda :self.check_win(button_d_text), relief="flat", font=("LexendDeca-Regular", 16),
                                    fg="#ffffff")
        button_d.place(x=500, y=485, width=300, height=45)
        #time.sleep(5)

    def check_win(self, value):
        if value == self.blah.question_answer[self.blah.target_question]:
            self.show_win()
        else:
            self.show_lose()

    def show_win(self):
        global score
        global wrong
        global score1
        score += 1
        score1=score - wrong
        
        self.master.title("Σωστο")
        self.canvas = tk.Canvas(self.master, bg="#3e4243", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.canvas.create_image(0, 0, image=self.background_img1, anchor="nw")
        self.canvas.create_text(100, 100.0,text='Score:{}'.format(score1), fill="#ffffff", font=("LexendDeca-Regular", 16))
        self.canvas.create_text(600, 100.0,text='Σωστή απάντηση!\n Η {} είναι {}!\n θες να συνεχίσεις;'.format(self.blah.target_question,
                                                                                           self.blah.question_answer[
                                                                                               self.blah.target_question]),fill="#ffffff", font=("LexendDeca-Regular", 16))

        button_continue = tk.Button(self.canvas, text="Συνέχεια", bg="#FFC700", borderwidth=0, highlightthickness=0,
                                    command=self.show_questions, relief="flat", font=("LexendDeca-Regular", 16),
                                    fg="#ffffff")
        button_continue.place(x=500, y=185, width=300, height=45)
        button_quit = tk.Button(self.canvas, text="Εξοδος", bg="#FFC700", borderwidth=0, highlightthickness=0,
                                command=self.master.destroy, relief="flat", font=("LexendDeca-Regular", 16),
                                fg="#ffffff")
        button_quit.place(x=500, y=285, width=300, height=45)

    def show_lose(self):
        global wrong
        global score
        global score1
        wrong=wrong + 1
        score1=score - wrong
        self.master.title("Λαθος")
        
        self.canvas = tk.Canvas(self.master, bg="#3e4243", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.canvas.create_image(0, 0, image=self.background_img1, anchor="nw")
        self.canvas.create_text(100, 100.0,text='Score:{}'.format(score1), fill="#ffffff", font=("LexendDeca-Regular", 16))
        self.canvas.create_text(600, 100.0,
                                text='Λάθος.\n Η {} είναι {}!\n Θες να συνεχίσεις;'.format(
                                    self.blah.target_question,
                                    self.blah.question_answer[
                                        self.blah.target_question]), fill="#ffffff", font=("LexendDeca-Regular", 16))

        button_continue = tk.Button(self.canvas, text="Συνέχεια", bg="#FFC700", borderwidth=0, highlightthickness=0,
                                    command=self.show_questions, relief="flat", font=("LexendDeca-Regular", 16),
                                    fg="#ffffff")
        button_continue.place(x=500, y=185, width=300, height=45)
        button_quit = tk.Button(self.canvas, text="Έξοδος", bg="#FFC700", borderwidth=0, highlightthickness=0,
                                command=self.master.destroy, relief="flat", font=("LexendDeca-Regular", 16),
                                fg="#ffffff")
        button_quit.place(x=500, y=285, width=300, height=45)

    def showend(self):
        global score
        global wrong
        self.master.title("Τέλος")
        self.finalscore=score - wrong
        self.canvas = tk.Canvas(self.master, bg="#3e4243", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.canvas.create_image(0, 0, image=self.background_img1, anchor="nw")
        self.canvas.create_text(600, 100.0,
                                text='Το score σου είναι {}!'.format(self.finalscore), fill="#ffffff", font=("LexendDeca-Regular", 16))

        button_quit = tk.Button(self.canvas, text="Τέλος", bg="#FFC700", borderwidth=0, highlightthickness=0,
                                command=self.end, relief="flat", font=("LexendDeca-Regular", 16),
                                fg="#ffffff")
        button_quit.place(x=500, y=185, width=300, height=45)

    def end(self):
        global user1
        global score
        global wrong
        
        finalscoreval=int(score)-int(wrong)

        cursor=data.cursor()
                
        if user1.highscore==None:
            highscore1=0
        else:
            highscore1=user1.highscore 
        
        finalscore1=int(highscore1) + finalscoreval

        finalscore1str="UPDATE Users SET highscore ='" + str(finalscore1) + "'" + "WHERE username='" + str(user1.username) + "'"
        finalscore1=cursor.execute(finalscore1str)
        data.commit()
        score=0
        wrong=0
        
            
            
            
            
        user1=auser(username,password)
            
        
        
        main1(self.master)
            
root=tk.Tk()
Login=Login(root)
  
root.mainloop()         
        

            
            
            
        
        
            
        
            
        
        
            
        
             
            
            

    
        

        
    
  
      

            
            
            
            
        
            

        
        
        
        
        
        
        
            
        
        


    
        

        

        
        
    


