from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import csv

class Loan:
    def __init__(self, master):
        # tkinter tk use as master
        self.master = master
        # To open application widget
        self.master.geometry('1000x1000')
        self.master.title('Public Bank')
        # Menu option use to make new page and Exit
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)
        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.filemenu.add_command(label='New', command=self.open_new_page)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=self.master.quit)
        # Photoimage use to insert a image in application
        self.image = PhotoImage(file='Bank.png')
        self.image = self.image.subsample(6)

        # label use for text and place use for where the text want to be position
        self.label = Label(self.master, image=self.image)
        self.label.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.label0 = Label(self.master, text='GOLD LOAN CALCULATOR', font=("Arial Bold", 15))
        self.label0.place(relx=0.5, rely=0.8, anchor=CENTER)

        self.label1 = Label(self.master, text='INTEREST CALCULATOR', font=("Arial Bold", 15))
        self.label1.place(relx=0.5, rely=0.65, anchor=CENTER)

        self.label4 = Label(self.master, text='ACCOUNT DETAILS', font=("Arial Bold", 15))
        self.label4.place(relx=0.5, rely=0.55, anchor=CENTER)

        # Button use for generate a function
        self.L1 = Button(self.master, text='Simple Interest',width = 20, command=self.calculate_simple_interest)
        self.L1.place(relx=0.5, rely=0.70, anchor=CENTER)
        self.L2 = Button(self.master, text='Compound Interest',width = 20, command=self.calculate_compound_interest)
        self.L2.place(relx=0.5, rely=0.75, anchor=CENTER)
        self.L3 = Button(self.master, text='Account Details',width = 20, command=self.get_account_details)
        self.L3.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.L0 = Button(self.master, text='Gold Weigth',width = 20, command=self.get_gold_loan)
        self.L0.place(relx=0.5, rely=0.85, anchor=CENTER)
        self.L5 = Button(self.master, text='Loan Amount',width = 20, command=self.get_gold_Amount_loan)
        self.L5.place(relx=0.5, rely=0.9, anchor=CENTER)

    def calculate_simple_interest(self):
        self.master.title('Loan calculator')

        # Canvas use to make a background color
        self.canvas = Canvas(self.master, width=2000, height=2000)
        self.canvas.pack()

        self.overlay_color = "white"
        self.canvas.create_rectangle(0, 0, 2000, 2000, fill=self.overlay_color, outline="")

        self.text = Label(self.master, text='SIMPLE INTEREST', font=("Arial Bold", 30))
        self.text.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.l1 = Label(self.master, text="Principle amount:", background='white', font=("Arial Bold", 15))
        self.l2 = Label(self.master, text="Rate of Interest:", background='white', font=("Arial Bold", 15))
        self.l3 = Label(self.master, text="Duration:", background='white', font=("Arial Bold", 15))

        self.l1.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.l2.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.l3.place(relx=0.4, rely=0.6, anchor=CENTER)

        self.e1 = Entry(self.master)
        self.e2 = Entry(self.master)
        self.e3 = Entry(self.master)

        self.e1.place(relx=0.6, rely=0.4, anchor=CENTER)
        self.e2.place(relx=0.6, rely=0.5, anchor=CENTER)
        self.e3.place(relx=0.6, rely=0.6, anchor=CENTER)

        self.l4 = Label(self.master, text='Simple Interest amount is:', font=("Arial Bold", 20))
        self.l4.place(relx=0.4, rely=0.7, anchor=CENTER)

        # self.b1 button used for called the calculate simple interest
        self.b1 = Button(self.master, text='Submit', command=self.calculate_simple_interest_submit)
        self.b1.place(relx=0.6, rely=0.8, anchor=CENTER)

    def calculate_simple_interest_submit(self):
        # The program of simple interest
        principle = int(self.e1.get())
        rate = int(self.e2.get())
        duration = int(self.e3.get())
        simple_interest = (principle * rate * duration) / 100
        # Config used to format the simple_interest into simple interest amount text
        self.l4.config(text=f"Simple Interest amount is: {simple_interest}")

    def calculate_compound_interest(self):
        self.master.title('Loan calculator')

        self.canvas = Canvas(self.master, width=2000, height=2000)
        self.canvas.pack()

        self.overlay_color = "white"
        self.canvas.create_rectangle(0, 0, 2000, 2000, fill=self.overlay_color, outline="")

        self.text = Label(self.master, text='COMPOUND INTEREST', font=("Arial Bold", 30))
        self.text.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.c1 = Label(self.master, text="Principle amount:")
        self.c2 = Label(self.master, text="Rate of Interest:")
        self.c3 = Label(self.master, text="Duration:")

        self.c1.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.c2.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.c3.place(relx=0.4, rely=0.6, anchor=CENTER)

        self.f1 = Entry(self.master)
        self.f2 = Entry(self.master)
        self.f3 = Entry(self.master)

        self.f1.place(relx=0.6, rely=0.4, anchor=CENTER)
        self.f2.place(relx=0.6, rely=0.5, anchor=CENTER)
        self.f3.place(relx=0.6, rely=0.6, anchor=CENTER)

        self.l4 = Label(self.master, text='Compound Interest amount is:', font=("Arial Bold", 20))
        self.l4.place(relx=0.4, rely=0.7, anchor=CENTER)

        self.b1 = Button(self.master, text='Submit', command=self.calculate_compound_interest_submit)
        self.b1.place(relx=0.6, rely=0.8, anchor=CENTER)

    def calculate_compound_interest_submit(self):
        principle = int(self.f1.get())
        rate = int(self.f2.get())
        duration = int(self.f3.get())
        compound_interest = int(principle * (1 + (rate / 100)) ** duration)
        self.l4.config(text=f"Compound Interest amount is: {compound_interest}")

    def get_account_details(self):

        # Frame used for forget the before function 
        self.newframe =Frame(self.master)
        self.newframe.pack()
        
        self.canvas = Canvas(self.newframe, width=2000, height=2000)
        self.canvas.pack()

        self.overlay_color = "white"
        self.canvas.create_rectangle(0, 0, 2000, 2000, fill=self.overlay_color, outline="")
        
        self.c1 = Label(self.newframe, text="Account Number:", font=('Arial Bold',20))
        self.c1.place(relx=0.4, rely=0.4, anchor=CENTER)

        self.c2 = Label(self.newframe, text="Enter the pin:", font=('Arial Bold',20))
        self.c2.place(relx=0.4, rely=0.5, anchor=CENTER)

        self.f1 = Entry(self.newframe)
        self.f1.place(relx=0.6, rely=0.4, anchor=CENTER)

        self.f2 = Entry(self.newframe)
        self.f2.place(relx=0.6, rely=0.5, anchor=CENTER)

        self.b1 = Button(self.newframe, text='Submit', command=self.retrieve_account_details)
        self.b1.place(relx=0.6, rely=0.6, anchor=CENTER)

    def retrieve_account_details(self):
        self.canvas = Canvas(self.master, width=2000, height=2000)
        self.canvas.pack()

        self.overlay_color = "white"
        self.canvas.create_rectangle(0, 0, 2000, 2000, fill=self.overlay_color, outline="")
        account_number = (self.f1.get())
        length = len(account_number)
        if 7 == length:
            account_number=account_number
        else:
            messagebox.showerror('showerror','Account number is wrong')
        pin_number = (self.f2.get())
        Length1 = len(pin_number)
        if 4 == Length1:
            pin_number = pin_number
        else:
            messagebox.showerror('showerror','Pin number is wrong')
        # Bank.csv open the csv file
        with open('Bank.csv', 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                if int(row[0]) == int(account_number) and int(row[4]) == int(pin_number):
                    self.display_account_details(row)
                    break
            
    def display_account_details(self, account):

        # if every input will be correct the Account details will show in new page
        self.canvas = Canvas(self.master, width=2000, height=2000)
        self.canvas.pack()

        self.overlay_color = "white"
        self.canvas.create_rectangle(0, 0, 2000, 2000, fill=self.overlay_color, outline="")

        self.text = Label(self.master, text='ACCOUNT DETAILS', font=("Arial Bold", 30))
        self.text.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.l1 = Label(self.master, text=f"Account Number: {account[0]}", font=("Arial Bold", 15))
        self.l2 = Label(self.master, text=f"Account Holder Name: {account[1]}", font=("Arial Bold", 15))
        self.l3 = Label(self.master, text=f"Account Holder Phone Number: {account[2]}", font=("Arial Bold", 15))
        self.l4 = Label(self.master, text=f"Balance Amount:  {account[3]}", font=("Arial Bold", 15))

        self.l1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.l2.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.l3.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.l4.place(relx=0.5, rely=0.8, anchor=CENTER)

        self.newframe.pack_forget()

    def get_gold_loan(self):

        self.canvas = Canvas(self.master, width=2000, height=2000)
        self.canvas.pack()

        self.overlay_color = "white"
        self.canvas.create_rectangle(0, 0, 2000, 2000, fill=self.overlay_color, outline="")

        self.master.title('Gold Loan')

        self.Title = Label(self.master,text='Gold Loan', font=("Arial Bold",20))
        self.Title.place(relx=0.5,rely=0.3,anchor=CENTER)

        self.gram = Label(self.master,text='Grams:', font=("Arial Bold", 15))
        self.gram.place(relx=0.4,rely=0.5,anchor=CENTER)

        self.interest = Label(self.master,text='Interest:', font=("Arial Bold", 15))
        self.interest.place(relx=0.4,rely=0.55,anchor=CENTER)

        self.Duration= Label(self.master,text='Months:', font=("Arial Bold", 15))
        self.Duration.place(relx=0.4,rely=0.6,anchor=CENTER)

        self.gr = Entry(self.master)
        self.gr.place(relx=0.55,rely=0.5,anchor=CENTER)

        self.int = Entry(self.master)
        self.int.place(relx=0.55,rely=0.55,anchor=CENTER)

        self.Dur = Entry(self.master)
        self.Dur.place(relx=0.55,rely=0.6,anchor=CENTER)

        self.rinciple = Label(text='The Gold Amount:',font =('Arial Bold', 20))
        self.rinciple.place(relx=0.4,rely=0.7,anchor=CENTER)

        self.Gold = Button(self.master,text='Sumbit', command= self.principle_gold_loan)
        self.Gold.place(relx=0.6,rely=0.75,anchor=CENTER)

    def principle_gold_loan(self):
        # The Goldrate.csv was used for 
        with open('Goldrate.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for i in csv_reader:
                Gold_rate = int(i[1])
        gr = int(self.gr.get())
        interest = int(self.int.get())
        Dur = int(self.Dur.get())
        Principle = (Gold_rate*gr)
        Loan_amount = (Principle*interest*(1+interest)**Dur/(1+interest)**(Dur-1))

        self.rinciple.config(text=f'The Gold Loan: {Loan_amount}')

    def get_gold_Amount_loan(self):

        self.canvas = Canvas(self.master, width=2000, height=2000)
        self.canvas.pack()

        self.overlay_color = "white"
        self.canvas.create_rectangle(0, 0, 2000, 2000, fill=self.overlay_color, outline="")

        self.master.title('Gold Loan')

        self.Title = Label(self.master,text='GOLD LOAN', font=("Arial Bold",20))
        self.Title.place(relx=0.5,rely=0.3,anchor=CENTER)

        self.gram = Label(self.master,text='Amount:', font=("Arial Bold", 15))
        self.gram.place(relx=0.4,rely=0.5,anchor=CENTER)

        self.gr1 = Entry(self.master)
        self.gr1.place(relx=0.55,rely=0.5,anchor=CENTER)

        self.rinciple = Label(text='The Gold gram for this amount:',font =('Arial Bold', 20))
        self.rinciple.place(relx=0.4,rely=0.7,anchor=CENTER)

        self.Gold = Button(self.master,text='Sumbit', command= self.principle_of_gold_loan)
        self.Gold.place(relx=0.6,rely=0.75,anchor=CENTER)

    def principle_of_gold_loan(self):
        
        with open('Goldrate.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for i in csv_reader:
                Gold_rate = int(i[1])
        gr = int(self.gr1.get())
        Rate = (gr/Gold_rate)

        self.rinciple.config(text=f'The Gold gram for this amount: {Rate}')        

    def open_new_page(self):
        # Top level using for program run from top
        new_page = Toplevel(self.master)
        loan_app = Loan(new_page)

# Main fun used for create the application page and function the class
def main():
    master = Tk()
    loan_app = Loan(master)
    master.mainloop()

main()