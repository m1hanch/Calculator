from tkinter import * #170x75  height= pix*17  width = pix*7.9313
import math

SMALL_LABEL_FONT=('Arial',16)
LARGE_LABEL_FONT=('Arial',40,'bold')
LABEL_COLOR='black' #25265E
LIGHT_BLUE='#91c1e7' #for = button
NOT_DIGITS_COLOR='#e6e6e6' #f7f7f7
DIGITS_BUTTON_COLOR='#fdfdfd'
HOVER_COLOR='#dcdcdc'
class Calculator:
    def __init__(self):
        self.calc = Tk()
        self.calc.geometry("700x700")
        #self.calc.resizable(0,0)
        self.calc.title("Мій Калькулятор")
        self.total_value=''
        self.current_value=''
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        self.digits={
            7: (2, 1), 8: (2, 2), 9: (2, 3),
            4: (3, 1), 5: (3, 2), 6: (3, 3),
            1: (4, 1), 2: (4, 2), 3: (4, 3),
            0: (5, 2), '.':(5,3)
        }
        self.operations= {'/':'\u00F7','*':'\u00D7','+':'+','-':'-'}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0,weight=1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x,weight=1)
            self.buttons_frame.columnconfigure(x,weight=1)
        self.create_digits_button()
        self.create_operator_buttons()
        self.create_percent_button()
        self.create_clear_everything_button()
        self.create_clear_button()
        self.create_erase_button()
        self.create_OneDivide_button()
        self.create_Square_button()
        self.create_square_root_button()
        self.create_equals_button()
        self.create_PlusMinus_button()
        self.bind_keys()

    def bind_keys(self):
        self.calc.bind("<Return>",lambda event: self.evaluate())
        for key in self.digits.keys():
            self.calc.bind(str(key),lambda event,digit=key: self.add_to_value(digit))
        for key in self.operations:
            self.calc.bind(str(key),lambda event,operator=key: self.add_to_value(operator))
        self.calc.bind('<BackSpace>',lambda event: self.erase())

    def add_to_value(self,value):
        self.current_value+=str(value)
        self.update_label()
    def create_display_labels(self):
        total_label=Label(self.display_frame, text=self.total_value, anchor='e',bg="#F5F5F5", fg=LABEL_COLOR,font=SMALL_LABEL_FONT)
        total_label.pack(expand=True, fill='both')

        label = Label(self.display_frame, text=self.total_value, anchor='e', bg="#F5F5F5", fg=LABEL_COLOR,font=LARGE_LABEL_FONT)
        label.pack(expand=True, fill="both")
        return total_label,label

    def create_display_frame(self):
        frame=Frame(self.calc, height=75, width=175,bg="#F5F5F5")
        frame.pack(expand=True,fill="both")
        return frame
    def create_buttons_frame(self):
        frame=Frame(self.calc)
        frame.pack(expand=True,fill="both")
        return frame


    #buttons
    def create_digits_button(self):
        def OnButton(button):
            button['bg'] = HOVER_COLOR
        def OffButton(button):
            button['bg'] = DIGITS_BUTTON_COLOR
        for digit,grid_value in self.digits.items():
            button = Button(self.buttons_frame, text=str(digit),bg=DIGITS_BUTTON_COLOR,fg=LABEL_COLOR,font=('Arial',18,'bold'),
                            command=lambda x=digit : self.add_to_value(x),relief='groove')
            button.grid(row=grid_value[0],column=grid_value[1],sticky=NSEW)
            button.bind('<Enter>', lambda event, btn=button: OnButton(btn))
            button.bind('<Leave>', lambda event, btn=button: OffButton(btn))

    def append_operator(self,operator):
        self.current_value+=operator
        self.total_value+=self.current_value
        self.current_value=''
        self.update_label()
        self.update_total_label()

    def create_operator_buttons(self):
        i=1

        def OnButton(button):
            button['bg'] = HOVER_COLOR
        def OffButton(button):
            button['bg'] = NOT_DIGITS_COLOR
        for operator,symbol in self.operations.items():
            button = Button(self.buttons_frame,text=symbol,font=('Arial',20),bg=NOT_DIGITS_COLOR,fg=LABEL_COLOR,
                            command=lambda x=operator: self.append_operator(x),relief='groove')
            button.grid(row=i,column=4,sticky=NSEW)
            i+=1
            button.bind('<Enter>', lambda event, btn=button: OnButton(btn))
            button.bind('<Leave>', lambda event, btn=button: OffButton(btn))

    def clear_everything(self):
        self.total_value=''
        self.current_value=''
        self.update_label()
        self.update_total_label()
    def create_clear_everything_button(self):
        button = Button(self.buttons_frame,text="CE",font=('Arial',20),bg=NOT_DIGITS_COLOR,fg=LABEL_COLOR,
                        command=self.clear_everything,relief='groove')
        button.grid(row=0,column=2,sticky=NSEW)
        def OnButton(e):
            button['bg'] = HOVER_COLOR
        def OffButton(e):
            button['bg']=NOT_DIGITS_COLOR
        button.bind('<Enter>', OnButton)
        button.bind('<Leave>', OffButton)

    def clear_current(self):
        self.current_value=''
        self.update_label()
    def create_clear_button(self):
        button = Button(self.buttons_frame,text="C",font=('Arial',20),bg=NOT_DIGITS_COLOR,fg=LABEL_COLOR,
                        command=self.clear_current,relief='groove')
        button.grid(row=0,column=3,sticky=NSEW)
        def OnButton(e):
            button['bg'] = HOVER_COLOR
        def OffButton(e):
            button['bg']=NOT_DIGITS_COLOR
        button.bind('<Enter>', OnButton)
        button.bind('<Leave>', OffButton)

    def erase(self):
        try:
            self.current_value=self.current_value[0:len(self.current_value)-1]
        except ValueError:
            self.current_value='Натисніть СЕ'
        self.update_label()
    def create_erase_button(self):
        button = Button(self.buttons_frame, text="\u232B", font=('Arial', 20), bg=NOT_DIGITS_COLOR, fg=LABEL_COLOR,
                        command=self.erase,relief='groove')
        button.grid(row=0, column=4, columnspan=1, sticky=NSEW)
        def OnButton(e):
            button['bg'] = HOVER_COLOR
        def OffButton(e):
            button['bg']=NOT_DIGITS_COLOR
        button.bind('<Enter>', OnButton)
        button.bind('<Leave>', OffButton)

    def OneDivide(self):
        try:
            self.current_value=str(1/float(self.current_value))
        except ValueError:
            self.current_value='Натисніть СЕ'
        self.update_label()
    def create_OneDivide_button(self):
        button = Button(self.buttons_frame, text="1/x", font=('Arial', 20), bg=NOT_DIGITS_COLOR, fg=LABEL_COLOR,
                        command=self.OneDivide,relief='groove')
        button.grid(row=1, column=1, sticky=NSEW)
        def OnButton(e):
            button['bg'] = HOVER_COLOR
        def OffButton(e):
            button['bg']=NOT_DIGITS_COLOR
        button.bind('<Enter>', OnButton)
        button.bind('<Leave>', OffButton)

    def square(self):
        try:
            self.current_value=str(float(pow(float(self.current_value),2)))
        except ValueError:
            self.current_value='Натисніть СЕ'
        self.update_label()
    def create_Square_button(self):
        button = Button(self.buttons_frame, text="x\u00b2", font=('Arial', 20), bg=NOT_DIGITS_COLOR, fg=LABEL_COLOR,
                        command=self.square,relief='groove')
        button.grid(row=1, column=2, sticky=NSEW)
        def OnButton(e):
            button['bg'] = HOVER_COLOR
        def OffButton(e):
            button['bg']=NOT_DIGITS_COLOR
        button.bind('<Enter>', OnButton)
        button.bind('<Leave>', OffButton)
    def Square_root(self):
        try:
            self.current_value = str(math.sqrt(float(self.current_value)))
        except ValueError:
            self.current_value='Натисніть СЕ'
        self.update_label()
    def create_square_root_button(self):
        button = Button(self.buttons_frame, text="√x", font=('Arial', 20), bg=NOT_DIGITS_COLOR, fg=LABEL_COLOR,
                        command= self.Square_root,relief='groove')
        button.grid(row=1, column=3, sticky=NSEW)
        def OnButton(e):
            button['bg'] = HOVER_COLOR
        def OffButton(e):
            button['bg']=NOT_DIGITS_COLOR
        button.bind('<Enter>', OnButton)
        button.bind('<Leave>', OffButton)

    def percent(self):
        try:
            for i in range(len(self.total_value)):
                if self.total_value[i]==('-' or '+' or '/' or '*'):
                    index=i
            full_val=self.total_value[0:i]
            percent_val=self.current_value[:len(self.current_value)]
            self.current_value=str((float(percent_val)*float(full_val)/100))
        except ValueError:
            self.current_value='Натисніть СЕ'
        self.update_label()
    def create_percent_button(self):
        button = Button(self.buttons_frame, text="%", font=('Arial', 20), bg=NOT_DIGITS_COLOR, fg=LABEL_COLOR,
                        command=self.percent,relief='groove')
        button.grid(row=0, column=1, sticky=NSEW)
        def OnButton(e):
            button['bg'] = HOVER_COLOR
        def OffButton(e):
            button['bg']=NOT_DIGITS_COLOR
        button.bind('<Enter>', OnButton)
        button.bind('<Leave>', OffButton)

    def evaluate(self):

        self.total_value+=self.current_value+'='
        self.update_total_label()
        try:
            self.current_value=str(eval(self.total_value[0:len(self.total_value)-1]))
            self.total_value=''
        except ZeroDivisionError:
            self.current_value='НЕ МОЖНА ДІЛИТИ НА 0!'
        except SyntaxError:
            self.current_value='Натисність СЕ'
        finally:
            self.update_label()


    def create_equals_button(self):
        button = Button(self.buttons_frame,text="=",font=('Arial',20),bg=LIGHT_BLUE,fg=LABEL_COLOR,
                        command=self.evaluate,relief='groove')
        button.grid(row=5,column=4,sticky=NSEW)
        def OnButton(e):
            button['bg'] = HOVER_COLOR
        def OffButton(e):
            button['bg']=LIGHT_BLUE
        button.bind('<Enter>', OnButton)
        button.bind('<Leave>', OffButton)

    def PlusMinus(self):
        try:
            self.current_value=str(int(self.current_value)*(-1))
        except ValueError:
            self.current_value='Натисніть СЕ'
        self.update_label()
    def create_PlusMinus_button(self):

        button=Button(self.buttons_frame,font=('Arial',20),text='\u00B1',fg=LABEL_COLOR,bg=DIGITS_BUTTON_COLOR,
                      command=self.PlusMinus,relief='groove')
        button.grid(row=5,column=1,sticky=NSEW)
        def OnButton(e):
            button['bg'] = HOVER_COLOR
        def OffButton(e):
            button['bg']=DIGITS_BUTTON_COLOR
        button.bind('<Enter>', OnButton)
        button.bind('<Leave>', OffButton)


    #functionality
    def update_total_label(self):
        self.total_label.config(text=self.total_value)
    def update_label(self):
        self.label.config(text=self.current_value)
    def run(self):

        self.calc.mainloop()


calc=Calculator()
calc.run()







