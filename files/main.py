import sys
import os
from tkinter import *
from math import factorial, log


if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    resource_path = sys._MEIPASS
else:
    resource_path = os.path.dirname(os.path.abspath(__file__))


root = Tk()
root.title('калькулятор')
root.geometry('330x550')
root.resizable(width=False, height=False)
icon_path = os.path.join(resource_path, "icon.ico")
root.iconbitmap(icon_path)


sign = None
number1 = None
number2 = None
hide_expression = None
expression_for_people = ''
expression_for_people_upwars = ''
signs_list = [' + ', ' - ', ' x ', ' % ', ' ÷ ', '! ', 'In', '√', '² ']


def update_display(value):
    global expression_for_people
    global hide_expression
    global sign
    global number1
    global number2
    global expression_for_people_upwars
    if number1 is None:
        hide_expression = expression_for_people
    if number1 is not None:
        if value != ' = ':
            hide_expression += str(value)
        if sign is None:
            if value not in signs_list:
                number1 += str(value)

    if value in signs_list:
        if expression_for_people != '' or value == 'In' or value == '√':
            sign = value
            expression_for_people_upwars = ''
            if number1 is None:
                number1 = hide_expression
            hide_expression = ''
        else:
            value = '-'
    if value == ' = ':
        number2 = hide_expression
        finally_expression = None
        if sign == ' + ':
            finally_expression = float(number1) + float(number2)
            if finally_expression.is_integer():
                finally_expression = int(finally_expression)
        elif sign == ' - ':
            finally_expression = float(number1) - float(number2)
            if finally_expression.is_integer():
                finally_expression = int(finally_expression)
        elif sign == ' x ':
            finally_expression = float(number1) * float(number2)
            if finally_expression.is_integer():
                finally_expression = int(finally_expression)
        elif sign == ' ÷ ':
            finally_expression = float(number1) / float(number2)
            if finally_expression.is_integer():
                finally_expression = int(finally_expression)
        elif sign == ' % ':
            finally_expression = float(number1) % float(number2)
            if finally_expression.is_integer():
                finally_expression = int(finally_expression)
        elif sign == '² ':
            finally_expression = float(number1) ** 2
            if finally_expression.is_integer():
                finally_expression = int(finally_expression)
        elif sign == '! ':
            if number1.isdigit():
                finally_expression = factorial(int(number1))
        elif sign == '√':
            if number1 == '' and number2 != '':
                finally_expression = float(number2) ** 0.5
            elif number2 == '' and number1 != '':
                finally_expression = float(number1) ** 0.5
            elif number1 != '' and number2 != '':
                finally_expression = float(number1) * (float(number2) ** 0.5)
            if finally_expression.is_integer():
                finally_expression = int(finally_expression)
        elif sign == 'In':
            if number1 == '' and number2 != '':
                finally_expression = log(float(number2))
            elif number2 == '' and number1 != '':
                finally_expression = log(float(number1))
            if finally_expression.is_integer():
                finally_expression = int(finally_expression)
        expression_for_people_upwars = expression_for_people + " = "
        expression_for_people = str(finally_expression)
        label_main.config(text=expression_for_people)
        label_upwards.config(text=expression_for_people_upwars)

        hide_expression = ''
        sign = None
        number2 = None
        number1 = str(finally_expression)
        return
    expression_for_people += str(value)
    label_main.config(text=expression_for_people)
    label_upwards.config(text=expression_for_people_upwars)


def button_plus(event=None):
    if event is None or event.state == 0x1 or event.state & 0x1:
        update_display(' + ')


def button_minus(event=None):
    update_display(' - ')


def button_x():
    update_display(' x ')


def button_divide():
    update_display(' ÷ ')


def button_factorial():
    update_display('! ')


def button_log():
    update_display('In')


def button_root():
    update_display('√')


def button_point(event=None):
    update_display('.')


def button_pow2():
    update_display('² ')


def button_divide_remainder():
    update_display(' % ')


def button_0(event=None):
    update_display(0)


def button_1(event=None):
    update_display(1)


def button_2(event=None):
    update_display(2)


def button_3(event=None):
    update_display(3)


def button_4(event=None):
    update_display(4)


def button_5(event=None):
    update_display(5)


def button_6(event=None):
    update_display(6)


def button_7(event=None):
    update_display(7)


def button_8(event=None):
    update_display(8)


def button_9(event=None):
    update_display(9)


def button_equals(event=None):
    update_display(' = ')


def button_c():
    global expression_for_people
    global expression_for_people_upwars
    global sign
    global number1
    global number2
    global hide_expression
    expression_for_people = ''
    sign = None
    number1 = None
    number2 = None
    expression_for_people_upwars = ''
    hide_expression = None
    label_main.config(text='')
    label_upwards.config(text='')


def button_delete(event=None):
    global expression_for_people
    global sign
    global hide_expression
    global number1
    if expression_for_people[-3:] in signs_list:
        sign = None
        expression_for_people = expression_for_people[:-2]
    elif expression_for_people[-2:] in signs_list:
        sign = None
        expression_for_people = expression_for_people[:-1]
    elif expression_for_people[-1:].isdigit():
        if sign is not None:
            hide_expression = hide_expression[:-1]
        elif sign is None:
            if number1 is None:
                hide_expression = hide_expression[:-1]
            elif number1 is not None:
                number1 = number1[:-1]
    expression_for_people = expression_for_people[:-1]
    label_main.config(text=expression_for_people)
    if expression_for_people == '':
        button_c()


canvas = Canvas(root, height=550, width=330, bg='#101721')
canvas.pack()

button = Button(root, text='+', command=button_plus, width=5, height=2, bg='white',
                activebackground='blue', activeforeground='white')
button.place(x=10, y=400)
button2 = Button(root, text='-', command=button_minus, width=5, height=2, bg='white',
                 activebackground='blue', activeforeground='white')
button2.place(x=62, y=400)
button3 = Button(root, text='x', command=button_x, width=5, height=2, bg='white',
                 activebackground='blue', activeforeground='white')
button3.place(x=114, y=400)
button4 = Button(root, text='÷', command=button_divide, width=5, height=2, bg='white',
                 activebackground='blue', activeforeground='white')
button4.place(x=166, y=400)
button5 = Button(root, text='n!', command=button_factorial, width=5, height=2, bg='white',
                 activebackground='blue', activeforeground='white')
button5.place(x=218, y=400)
button6 = Button(root, text='In', command=button_log, width=5, height=2, bg='white',
                 activebackground='blue', activeforeground='white')
button6.place(x=271, y=400)
button7 = Button(root, text='√', command=button_root, width=5, height=2, bg='white',
                 activebackground='blue', activeforeground='white')
button7.place(x=114, y=449)
button8 = Button(root, text='.', command=button_point, width=5, height=2, font=('Arial', 9, 'bold'), bg='white',
                 activebackground='blue', activeforeground='white')
button8.place(x=62, y=449)
button9 = Button(root, text='n²', command=button_pow2, width=5, height=2, bg='white',
                 activebackground='blue', activeforeground='white')
button9.place(x=166, y=449)
button10 = Button(root, text='%', command=button_divide_remainder, width=5, height=2, bg='white',
                  activebackground='blue', activeforeground='white')
button10.place(x=218, y=449)


label1 = Label(root)
label1.place(relwidth=50, relheight=0.1)
label2 = Label(root, text='_________________________', font='Arial 17')
label2.place(y=50)
label3 = Label(root, text="выполнить операцию ↓")
label3.place(y=7, x=98)


button11 = Button(root, text='0', command=button_0, width=5, height=2, bg='blue',
                  activebackground='white', activeforeground='black', foreground='white')
button11.place(x=62, y=351)
button12 = Button(root, text='1', command=button_1, width=5, height=2, bg='blue',
                  activebackground='white', activeforeground='black', foreground='white')
button12.place(x=114, y=351)
button13 = Button(root, text='2', command=button_2, width=5, height=2, bg='blue',
                  activebackground='white', activeforeground='black', foreground='white')
button13.place(x=166, y=351)
button14 = Button(root, text='3', command=button_3, width=5, height=2, bg='blue',
                  activebackground='white', activeforeground='black', foreground='white')
button14.place(x=218, y=351)
button15 = Button(root, text='4', command=button_4, width=5, height=2, bg='blue',
                  activebackground='white', activeforeground='black', foreground='white')
button15.place(x=62, y=302)
button16 = Button(root, text='5', command=button_5, width=5, height=2, bg='blue',
                  activebackground='white', activeforeground='black', foreground='white')
button16.place(x=114, y=302)
button17 = Button(root, text='6', command=button_6, width=5, height=2, bg='blue',
                  activebackground='white', activeforeground='black', foreground='white')
button17.place(x=166, y=302)
button18 = Button(root, text='7', command=button_7, width=5, height=2, bg='blue',
                  activebackground='white', activeforeground='black', foreground='white')
button18.place(x=218, y=302)
button19 = Button(root, text='8', command=button_8, width=5, height=2, bg='blue',
                  activebackground='white', activeforeground='black', foreground='white')
button19.place(x=114, y=253)
button20 = Button(root, text='9', command=button_9, width=5, height=2, bg='blue',
                  activebackground='white', activeforeground='black', foreground='white')
button20.place(x=166, y=253)


button21 = Button(root, text='C', command=button_c, width=5, height=2, bg='#5ae0a4',
                  activebackground='white', activeforeground='black', foreground='black')
button21.place(x=62, y=204)
button22 = Button(root, text='⌫', command=button_delete, width=5, height=2, bg='#5ae0a4',
                  activebackground='white', activeforeground='black', foreground='black')
button22.place(x=218, y=204)


canvas.create_line(62, 395, 263, 395, fill="purple", width=3)
canvas.create_line(114, 296.6, 211, 296.6, fill="red", width=3)
canvas.create_line(114, 296.6, 97, 280, fill="red", width=3)
canvas.create_line(211, 296.6, 228, 280, fill="red", width=3)

image_path = os.path.join(resource_path, "bg_calcalator-transformed.png")
image = PhotoImage(file=image_path)
button_image = Button(root, image=image, bg='#101721', activebackground='#101721', command=button_equals)
button_image["border"] = "0"
button_image.place(y=100, x=100)

label_main = Label(root, text='', font=('Arial', 15), width=29, anchor='e')
label_main.place(y=48.4, x=1)
label_upwards = Label(root, text='', font=('Arial', 11), width=29, anchor='e', fg='#9ba89e')
label_upwards.place(y=25, x=65)
root.bind("<Key-0>", button_0)
root.bind("<Key-1>", button_1)
root.bind("<Key-2>", button_2)
root.bind("<Key-3>", button_3)
root.bind("<Key-4>", button_4)
root.bind("<Key-5>", button_5)
root.bind("<Key-6>", button_6)
root.bind("<Key-7>", button_7)
root.bind("<Key-8>", button_8)
root.bind("<Key-9>", button_9)
root.bind("<Return>", button_equals)
root.bind("<equal>", button_equals)
root.bind("<BackSpace>", button_delete)
root.bind("<period>", button_point)
root.bind("<minus>", button_minus)
root.bind("<plus>", button_plus)
root.mainloop()