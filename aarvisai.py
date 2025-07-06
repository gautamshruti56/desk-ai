from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import random
import wikipedia
import openai

def Aarvis():
    try:
        apikey = 'AIzaSyClvZ-UntdAi3ndOzg7lTvJp9jj_uyBzl8'
        def ai(prompt):
            openai.api_key = apikey
            text = f'OpenAI response for prompt: {prompt} \n *************************\n\n'
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            text += response["choices"][0]['text']
            if not os.path.exists("Openai"):
                os.mkdir("Openai")
            with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
                f.write(text)

        chatstr = ''

        def chat(query):
            global chatstr
            openai.api_key = apikey
            chatstr += f"User: {query}\n Aarvis: "
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=chatstr,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            speak(response["choices"][0]["text"])
            chatstr += f"{response['choices'][0]['text']}\n"
            return response["choices"][0]['text']

        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

        def speak(text):
            engine.say(text)
            engine.runAndWait()

        def wishme():
            hour = int(datetime.datetime.now().hour)

            if hour >= 0 and hour < 12:
                speak("good morning")

            elif hour >= 12 and hour < 18:
                speak("good Afternoon")

            else:
                speak("good evening")

            speak("I am Aarvis AI how may i help you")

        def takecommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                r.pause_threshold = 1
                audio = r.listen(source)

            try:
                print("recognizing..")
                query = r.recognize_google(audio, language='en-in')
                print(f"User said:  {query}\n")
                speak(f"{query}\n")

            except Exception as e:
                print(e)
                print("Say that again please...")
                return "None"
            return query

        def talkcommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                r.pause_threshold = 1
                audio = r.listen(source)

            try:
                print("recognizing..")
                query = r.recognize_google(audio, language='hi-in')
                print(f"User said:  {query}\n")
                speak(f"{query}/n")

            except Exception as e:
                print(e)
                print("Say that again please...")
                return "None"
            return query

        if __name__ == "__main__":

            chatstr = ''
            wishme()

            while True:
                query = takecommand().lower()
                try:

                    if 'wikipedia' in query:
                        speak('Searching wikipedia...')
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        speak("According to wikipedia")
                        print(results)
                        speak(results)

                    elif 'open youtube' in query:
                        webbrowser.open("youtube.com")

                    elif 'open google' in query:
                        webbrowser.open("goggle.com")

                    elif 'open instagram' in query:
                        webbrowser.open("instagram.com")

                    elif 'open whatsapp' in query:
                        webbrowser.open("whatsapp.com")

                    elif 'open python compiler' in query:
                        webbrowser.open("programiz.com")

                    elif 'open facebook' in query:
                        webbrowser.open("facebook.com")

                    elif 'open Ai' in query:
                        webbrowser.open("chatgpt.com")

                    elif 'open pintrest' in query:
                        webbrowser.open("pintrest.com")

                    elif 'tell me about' in query:
                        ai(prompt=query)

                    elif 'open wattpad' in query:
                        webbrowser.open("wattpad.com")

                    elif 'open twitter' in query:
                        webbrowser.open("twitter.com")

                    elif 'open attackoverflow' in query:
                        webbrowser.open("attackoverflow.com")

                    elif 'open google photos' in query:
                        webbrowser.open("googlephotos.com")

                    elif 'open google map' in query:
                        webbrowser.open("googlemap.com")

                    elif 'play music' in query:
                        music_dir = 'C:\\Users\\AdminMusic\\English songs'
                        songs = os.listdir(music_dir)
                        print(songs)
                        os.startfile(os.path.join(music_dir, songs[random.randint(0, 21)]))

                    elif 'the time' in query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        speak(f"the time is {strTime}")

                    elif 'talk in hindi' in query:
                        query = talkcommand()

                    elif 'quit chat' in query:
                        exit()

                    elif 'aarvis' in query:
                        chatstr = ''

                    else:
                        print("Chatting.......")

                except Exception as e:
                    print(e)

    except Exception as e:
        print(e)

def signuppage():


    def login_page():
        signup_window.destroy()
        checking()

    def clear():
        emailEntry.delete(0, END)
        userEntry.delete(0, END)
        passwordEntry.delete(0, END)
        confirmpasswordEntry.delete(0, END)
        check.set(0)

    def connect_database():
        if emailEntry.get() == '' or userEntry.get() == '' or passwordEntry.get() == '' or confirmpasswordEntry.get() == '':
            messagebox.showerror('Error', 'All fields are required')
        elif passwordEntry.get() != confirmpasswordEntry.get():
            messagebox.showerror('Error', 'Password Mismatched')
        elif check.get() == 0:
            messagebox.showerror('Error', 'Please Accept terms and conditions')
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='1234')
                mycursor = con.cursor()
            except:
                messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')

                return

            try:
                query = 'create database if not exists userdata_interface'
                mycursor.execute(query)
                query = 'use userdata_interface'
                mycursor.execute(query)
                query = 'create table if not exists userdata(email varchar(30),username varchar(30) not null primary key,password varchar(10))'
                mycursor.execute(query)

            except:
                mycursor.execute('use userdata_interface')

            query = 'select * from userdata where username = %s'
            mycursor.execute(query, (userEntry.get()))
            row = mycursor.fetchone()
            query = 'select * from userdata where username = %s'
            mycursor.execute(query, (emailEntry.get()))
            row2 = mycursor.fetchone()
            if row != None and row2 != None:
                messagebox.showerror('Error', 'Email and User name already exists')
            elif row2 != None:
                messagebox.showerror('Error', 'Email already exists')

            elif row != None:
                messagebox.showerror('Error', 'Username already exists')

            else:

                query = 'insert into userdata(username,email,password)values(%s,%s,%s)'
                mycursor.execute(query, (userEntry.get(), emailEntry.get(), passwordEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Registration is successful')
                clear()
                signup_window.destroy()
                checking()

    signup_window = Tk()
    signup_window.title('Signup Page')
    signup_window.resizable(False, False)

    background = ImageTk.PhotoImage(file='image2.jpg')

    bgLabel = Label(signup_window, image=background)
    bgLabel.grid()

    frame = Frame(signup_window, bg='white')
    frame.place(x=610, y=50)

    heading = Label(frame, text='CREATE AN ACCOUNT', font=('Elephant', 20)
                    , bg='white', fg='black')
    heading.grid(row=0, column=0, padx=10, pady=10)

    emailLabel = Label(frame, text='Email', font=('Microsoft Yahei UI Light', 12, 'bold'), bg='white', fg='black')
    emailLabel.grid(row=1, column=0, sticky='w', padx=25)

    emailEntry = Entry(frame, width=35, font=('Microsoft Yahei UI Light', 12, 'bold'), bg='grey', fg='white')
    emailEntry.grid(row=2, column=0, sticky='w', padx=25)

    userLabel = Label(frame, text='Username', font=('Microsoft Yahei UI Light', 12, 'bold'), bg='white', fg='black')
    userLabel.grid(row=3, column=0, sticky='w', padx=25)

    userEntry = Entry(frame, width=35, font=('Microsoft Yahei UI Light', 12, 'bold'), bg='grey', fg='white')
    userEntry.grid(row=4, column=0, sticky='w', padx=25)

    passwordLabel = Label(frame, text='Password', font=('Microsoft Yahei UI Light', 12, 'bold'), bg='white', fg='black')
    passwordLabel.grid(row=5, column=0, sticky='w', padx=25)

    passwordEntry = Entry(frame, width=35, font=('Microsoft Yahei UI Light', 12, 'bold'), bg='grey', fg='white')
    passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

    confirmpasswordLabel = Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light', 12, 'bold'),
                                 bg='white', fg='black')
    confirmpasswordLabel.grid(row=7, column=0, sticky='w', padx=25)

    confirmpasswordEntry = Entry(frame, width=35, font=('Microsoft Yahei UI Light', 12, 'bold'), bg='grey', fg='white')
    confirmpasswordEntry.grid(row=8, column=0, sticky='w', padx=25)

    check = IntVar()
    termandcondition = Checkbutton(frame, text='I agree to the Terms and conditions',
                                   font=('Microsoft Yahei UI Light', 10, 'bold'), cursor='hand2', variable=check)
    termandcondition.grid(row=9, column=0, pady=10, padx=15)

    signupbutton = Button(frame, text="Signup", font=('Open Sans', 16, 'bold')
                          , bd=0, fg='black', width=17, activebackground='red', activeforeground='white',
                          cursor='hand2', command=connect_database)
    signupbutton.grid(row=10, column=0, pady=10)

    alreadyaccountLabel = Button(frame, text='Have an account?', font=('Open sans', 12, 'bold'), bg='white', bd=0,
                                 fg='black', cursor='hand2')
    alreadyaccountLabel.grid(row=11, column=0, sticky='w', padx=25, pady=10)

    loginbutton = Button(frame, text="Login", font=('Open Sans', 12, 'bold underline'), bg='white'
                         , bd=0, fg='blue', activebackground='grey', activeforeground='blue', cursor='hand2',
                         command=login_page)
    loginbutton.place(x=240, y=385)

    signup_window.mainloop()


def checking():
    def forget_pass():
        def change_password():
            if user_Entry.get == '' or newpass_Entry.get() == '' or confirmpass_Entry.get() == '':
                messagebox.showerror('Error', 'All fields are required', parent=window)
            elif newpass_Entry.get() != confirmpass_Entry.get():
                messagebox.showerror('Error', 'New pass and confirm pass mismatch', parent=window)
            else:
                con = pymysql.connect(host='localhost', user='root', password='1234', database='userdata_interface')
                mycursor = con.cursor()
                query = 'select * from userdata where username = %s'
                mycursor.execute(query, (user_Entry.get()))
                row = mycursor.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Username incorrect!')
                else:
                    query = 'update userdata set password = %s where username = %s'
                    mycursor.execute(query, (newpass_Entry.get(), user_Entry.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo('Success', 'Password is reset, please login with new password', parent=window)
                    window.destroy()

        def on_enter_(event):
            if user_Entry.get() == 'Username':
                user_Entry.delete(0, END)

        def newpass_enter_(event):
            if newpass_Entry.get() == 'New Password':
                newpass_Entry.delete(0, END)

        def confirmpass_enter(event):
            if confirmpass_Entry.get() == 'Confirm Password':
                confirmpass_Entry.delete(0, END)

        window = Toplevel()
        window.title('Change Password')

        bgImage = ImageTk.PhotoImage(file='Imagee1.jpg')

        bgLabel = Label(window, image=bgImage)
        bgLabel.grid(row=0, column=0)

        heading = Label(window, text='RESET PASSWORD', font=('Elephant', 20, 'bold'), bd=0)
        heading.place(x=660, y=80)

        user_Entry = Entry(window, width=35, font=('bold'), fg='black')
        user_Entry.place(x=660, y=150)
        user_Entry.insert(0, 'Username')
        user_Entry.bind('<FocusIn>', on_enter_)

        newpass_Entry = Entry(window, width=35, font=('bold'), fg='black')
        newpass_Entry.place(x=660, y=190)
        newpass_Entry.insert(0, 'New Password')
        newpass_Entry.bind('<FocusIn>', newpass_enter_)

        confirmpass_Entry = Entry(window, width=35, font=('bold'), fg='black')
        confirmpass_Entry.place(x=660, y=230)
        confirmpass_Entry.insert(0, 'Confirm Password')
        confirmpass_Entry.bind('<FocusIn>', confirmpass_enter)

        submitbutton = Button(window, text='Submit', font=('Open Sans', 16, 'bold'), fg='white', bg='red',
                              activebackground='red', cursor='hand2', bd=0, width=20, command=change_password)
        submitbutton.place(x=685, y=360)

        window.mainloop()

    def clear():

        usernameEntry.delete(0, END)
        passwordEntry.delete(0, END)

    def signup_page():
        loginwindow.destroy()
        signuppage()

    def user_login():
        if usernameEntry.get() == '' or passwordEntry.get() == '':
            messagebox.showerror('Error', 'All fields are required')
            return
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='1234')
                mycursor = con.cursor()
            except:
                messagebox.showerror('Error', 'Connection did not established')
                return
        query = 'use userdata_interface'
        mycursor.execute(query)
        query = 'select * from userdata where username =%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Welcome', 'Login Successful')
            clear()
            loginwindow.destroy()
            Aarvis()

    def on_enter(event):
        if usernameEntry.get() == 'Username':
            usernameEntry.delete(0, END)

    def password_enter(event):
        if passwordEntry.get() == 'Password':
            passwordEntry.delete(0, END)

    def hide():
        openeye.config(file='closeeye.png')
        passwordEntry.config(show='*')
        eyeButton.config(command=show)

    def show():
        openeye.config(file='openeye.png')
        passwordEntry.config(show='')
        eyeButton.config(command=hide)

    loginwindow = Tk()
    loginwindow.resizable(0, 0)
    loginwindow.title('loginpage')

    bgImage = ImageTk.PhotoImage(file='Imagee1.jpg')

    bgLabel = Label(loginwindow, image=bgImage)
    bgLabel.grid(row=0, column=0)

    heading = Label(loginwindow, text='USER LOGIN', font=('Elephant', 20, 'bold'), bd=0)
    heading.place(x=700, y=80)

    usernameEntry = Entry(loginwindow, width=35, font=('bold'), fg='black')
    usernameEntry.place(x=660, y=150)
    usernameEntry.insert(0, 'Username')
    usernameEntry.bind('<FocusIn>', on_enter)

    passwordEntry = Entry(loginwindow, width=35, font=('bold'), fg='black')
    passwordEntry.place(x=660, y=190)
    passwordEntry.insert(0, 'Password')
    passwordEntry.bind('<FocusIn>', password_enter)

    openeye = PhotoImage(file='openeye.png')
    eyeButton = Button(loginwindow, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',
                       command=hide)
    eyeButton.place(x=953, y=193)

    forgetButton = Button(loginwindow, text='Forgot Password?', bd=0, bg='white', activebackground='white',
                          cursor='hand2', font=('', 8, 'bold'), fg='black', activeforeground='red', command=forget_pass)
    forgetButton.place(x=870, y=214)

    loginbutton = Button(loginwindow, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='red',
                         activebackground='red', cursor='hand2', bd=0, width=20, command=user_login)
    loginbutton.place(x=685, y=360)

    signuplabel = Label(loginwindow, text='Dont have an account?', font=('', 9, 'bold'), bd=0, )
    signuplabel.place(x=670, y=450)

    newaccountbutton = Button(loginwindow, text='Create new account', font=('Open Sans', 9, 'underline', 'bold'),
                              fg='blue', activeforeground='blue', activebackground='white', cursor='hand2', bd=0,
                              command=signup_page)
    newaccountbutton.place(x=810, y=450)

    loginwindow.mainloop()


def login_page():
    signup_window.destroy()
    checking()


def clear():
    emailEntry.delete(0,END)
    userEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmpasswordEntry.delete(0,END)
    check.set(0)


def connect_database():
    if emailEntry.get() == '' or userEntry.get() == '' or passwordEntry.get() == '' or confirmpasswordEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif passwordEntry.get()!= confirmpasswordEntry.get():
        messagebox.showerror('Error', 'Password Mismatched')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please Accept terms and conditions')
    else:
        try:
             con= pymysql.connect(host='localhost', user='root',password='1234')
             mycursor= con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            
            return

        try:
            query='create database if not exists userdata_interface'
            mycursor.execute(query)
            query= 'use userdata_interface'
            mycursor.execute(query)
            query= 'create table if not exists userdata(email varchar(30),username varchar(30) not null primary key,password varchar(10))'
            mycursor.execute(query)

        except:
            mycursor.execute('use userdata_interface')

        query='select * from userdata where username = %s'
        mycursor.execute(query,(userEntry.get()))
        row = mycursor.fetchone()
        query='select * from userdata where username = %s'
        mycursor.execute(query, (emailEntry.get()))
        row2 = mycursor.fetchone()
        if row != None and row2 != None:
            messagebox.showerror('Error','Email and User name already exists')
        elif row2 != None:
            messagebox.showerror('Error','Email already exists')

        elif row != None:
            messagebox.showerror('Error','Username already exists')

        else:

            query= 'insert into userdata(username,email,password)values(%s,%s,%s)'
            mycursor.execute(query,(userEntry.get(),emailEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is successful')
            clear()
            signup_window.destroy()
            checking()

signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)

background=ImageTk.PhotoImage(file='image2.jpg')

bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=610,y=50)

heading = Label(frame,text = 'CREATE AN ACCOUNT',font=('Elephant',20)
                ,bg='white',fg='black')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('Microsoft Yahei UI Light',12,'bold'),bg='white',fg='black')
emailLabel.grid(row=1,column=0,sticky='w',padx=25)

emailEntry=Entry(frame,width=35,font=('Microsoft Yahei UI Light',12,'bold'),bg='grey',fg='white')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

userLabel=Label(frame,text='Username',font=('Microsoft Yahei UI Light',12,'bold'),bg='white',fg='black')
userLabel.grid(row=3,column=0,sticky='w',padx=25)

userEntry=Entry(frame,width=35,font=('Microsoft Yahei UI Light',12,'bold'),bg='grey',fg='white')
userEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light',12,'bold'),bg='white',fg='black')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25)

passwordEntry=Entry(frame,width=35,font=('Microsoft Yahei UI Light',12,'bold'),bg='grey',fg='white')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmpasswordLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',12,'bold'),bg='white',fg='black')
confirmpasswordLabel.grid(row=7,column=0,sticky='w',padx=25)

confirmpasswordEntry=Entry(frame,width=35,font=('Microsoft Yahei UI Light',12,'bold'),bg='grey',fg='white')
confirmpasswordEntry.grid(row=8,column=0,sticky='w',padx=25)


check=IntVar()
termandcondition=Checkbutton(frame,text='I agree to the Terms and conditions',
                             font=('Microsoft Yahei UI Light',10,'bold'),cursor='hand2',variable=check )
termandcondition.grid(row=9,column=0,pady=10,padx=15)

signupbutton=Button(frame,text="Signup",font=('Open Sans',16,'bold')
                    ,bd=0,fg='black',width=17,activebackground='red',activeforeground='white',cursor='hand2',command=connect_database)
signupbutton.grid(row=10,column=0,pady=10) 

alreadyaccountLabel=Button(frame,text='Have an account?',font=('Open sans',12,'bold'),bg='white',bd=0,fg='black',cursor='hand2')
alreadyaccountLabel.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginbutton=Button(frame,text="Login",font=('Open Sans',12,'bold underline'),bg='white'
                    ,bd=0,fg='blue',activebackground='grey',activeforeground='blue',cursor='hand2',command=login_page)
loginbutton.place(x=240,y=385) 

signup_window.mainloop()