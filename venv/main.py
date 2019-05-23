from tkinter import *


class Point:
    def __init__(self):
        self.state = False

def create(numel,steps):
    tab = [[Point() for j in range(numel)] for i in range(steps)]
    if numel>100:
        tab[0][50].state = True
    else:
        tab[0][int(numel/2)].state = True
    return tab

def selected():
    numel = int(entry.get())
    steps = int(entry2.get())
    tab = create(numel, steps)
    x = my_var.get()
    if x==30:
        thirty(tab,numel,steps)
    elif x==60:
        sixty(tab,numel,steps)
    elif x==90:
        ninety(tab,numel,steps)
    elif x==120:
        onetwenty(tab,numel,steps)
    elif x==225:
        twotwofive(tab,numel,steps)
    else:
        print("stuff")
        pass

    #print('\n')
    #print(x)
    can.delete(ALL)
    for i in range (0,steps):
        row = ''
        for j in range (0,numel):
            if tab[i][j].state == False:
                #row+=' 0 '
                #can.create_rectangle(4*j,4*i,4*j+4,4*i+4,fill="white")
                can.create_rectangle(5*j,5*i,5*j+5,5*i+5,fill="white")
                #can.create_rectangle(6*j,6*i,6*j+6,6*i+6,fill="white")
            else:
                #row+=' 1 '
                #can.create_rectangle(4*j,4*i,4*j+4,4*i+4,fill="black")
                can.create_rectangle(5*j,5*i,5*j+5,5*i+5,fill="black")
                #can.create_rectangle(6*j,6*i,6*j+6,6*i+6,fill="black")
        #print(row)


def thirty(tab, numel,steps):
    #30
    for i in range (0,steps-1):
        for j in range (0,numel-1):
            if i>1 and j==0:
                if tab[i-1][numel-1].state and not tab[i][j].state and not tab[i][j + 1].state \
                        or not tab[i-1][numel-1].state and tab[i][j].state and tab[i][j + 1].state \
                        or not tab[i-1][numel-1].state and tab[i][j].state and not tab[i][j + 1].state \
                        or not tab[i-1][numel-1].state and not tab[i][j].state and tab[i][j + 1].state:

                    tab[i][j].state=True
                else:
                    tab[i][j].state=False
            if i>1 and j==numel-1:
                if tab[i][j - 1].state and not tab[i][j].state and not tab[i][0].state \
                        or not tab[i][j - 1].state and tab[i][j].state and tab[i][0].state \
                        or not tab[i][j - 1].state and tab[i][j].state and not tab[i][0].state \
                        or not tab[i][j - 1].state and not tab[i][j].state and tab[i][0].state:

                    tab[i+1][j].state=True
                else:
                    tab[i+1][j].state=False


            elif tab[i][j - 1].state and not tab[i][j].state and not tab[i][j + 1].state \
                or not tab[i][j - 1].state and tab[i][j].state and tab[i][j + 1].state \
                or not tab[i][j - 1].state and tab[i][j].state and not tab[i][j + 1].state \
                or not tab[i][j - 1].state and not tab[i][j].state and tab[i][j + 1].state:

                tab[i + 1][j].state = True
            else:
                tab[i + 1][j].state = False
    return tab

def sixty(tab, numel,steps):
    #60
    for i in range (0,steps-1):
        for j in range (0,numel):
            if i>1 and j==0:
                if tab[i-1][numel - 1].state and not tab[i][j].state and tab[i][j + 1].state \
                or tab[i-1][numel - 1].state and not tab[i][j].state and not tab[i][j + 1].state \
                or not tab[i-1][numel - 1].state and tab[i][j].state and tab[i][j + 1].state \
                or not tab[i-1][numel - 1].state and tab[i][j].state and not tab[i][j + 1].state:

                    tab[i+1][j].state=True
                else:
                    tab[i+1][j].state=False

            if i>1 and j==numel-1:
                if tab[i][j - 1].state and not tab[i][j].state and tab[i][0].state \
                or tab[i][j - 1].state and not tab[i][j].state and not tab[i][0].state \
                or not tab[i][j - 1].state and tab[i][j].state and tab[i][0].state \
                or not tab[i][j - 1].state and tab[i][j].state and not tab[i][0].state:

                    tab[i+1][j].state=True
                else:
                    tab[i+1][j].state=False

            elif tab[i][j - 1].state and not tab[i][j].state and tab[i][j + 1].state \
                or tab[i][j - 1].state and not tab[i][j].state and not tab[i][j + 1].state \
                or not tab[i][j - 1].state and tab[i][j].state and tab[i][j + 1].state \
                or not tab[i][j - 1].state and tab[i][j].state and not tab[i][j + 1].state:

                tab[i + 1][j].state = True
            else:
                tab[i + 1][j].state = False
    return tab

def ninety(tab, numel,steps):
    #90
    for i in range (0,steps-1):
        for j in range (0,numel-1):
            if i>1 and j==0:
                if tab[i-1][numel - 1].state and tab[i][j].state and not tab[i][j + 1].state \
                or tab[i-1][numel - 1].state and not tab[i][j].state and not tab[i][j + 1].state \
                or not tab[i-1][numel - 1].state and tab[i][j].state and tab[i][j + 1].state \
                or not tab[i-1][numel - 1].state and not tab[i][j].state and tab[i][j + 1].state:

                    tab[i+1][j].state=True
                else:
                    tab[i+1][j].state=False

            if i>1 and j==numel-1:
                if tab[i][j - 1].state and tab[i][j].state and not tab[i][0].state \
                or tab[i][j - 1].state and not tab[i][j].state and not tab[i][0].state \
                or not tab[i][j - 1].state and tab[i][j].state and tab[i][0].state \
                or not tab[i][j - 1].state and not tab[i][j].state and tab[i][0].state:

                    tab[i+1][j].state=True
                else:
                    tab[i+1][j].state=False

            elif tab[i][j - 1].state and tab[i][j].state and not tab[i][j + 1].state \
                or tab[i][j - 1].state and not tab[i][j].state and not tab[i][j + 1].state \
                or not tab[i][j - 1].state and tab[i][j].state and tab[i][j + 1].state \
                or not tab[i][j - 1].state and not tab[i][j].state and tab[i][j + 1].state:

                tab[i + 1][j].state = True
            else:
                tab[i + 1][j].state = False
    return tab


def onetwenty(tab, numel,steps):
    #120
    for i in range (0,steps-1):
        for j in range (0,numel):
            if i>1 and j==0:
                if tab[i-1][numel - 1].state and tab[i][j].state and not tab[i][j + 1].state \
                or tab[i-1][numel - 1].state and not tab[i][j].state and tab[i][j + 1].state \
                or tab[i-1][numel - 1].state and not tab[i][j].state and not tab[i][j + 1].state \
                or not tab[i-1][numel - 1].state and tab[i][j].state and tab[i][j + 1].state:

                    tab[i+1][j].state=True
                else:
                    tab[i+1][j].state=False

            if i>1 and j==numel-1:
                if tab[i][j - 1].state and tab[i][j].state and not tab[i][0].state \
                or tab[i][j - 1].state and not tab[i][j].state and tab[i][0].state \
                or tab[i][j - 1].state and not tab[i][j].state and not tab[i][0].state \
                or not tab[i][j - 1].state and tab[i][j].state and tab[i][0].state:

                    tab[i+1][j].state=True
                else:
                    tab[i+1][j].state=False

            elif tab[i][j - 1].state and tab[i][j].state and not tab[i][j + 1].state \
                or tab[i][j - 1].state and not tab[i][j].state and tab[i][j + 1].state \
                or tab[i][j - 1].state and not tab[i][j].state and not tab[i][j + 1].state \
                or not tab[i][j - 1].state and tab[i][j].state and tab[i][j + 1].state:

                tab[i + 1][j].state = True
            else:
                tab[i + 1][j].state = False
    return tab

def twotwofive(tab, numel,steps):
    #225
    for i in range (0,steps-1):
        for j in range (0,numel-1):
            if i>1 and j==0:
                if tab[i-1][numel - 1].state and tab[i][j].state and tab[i][j + 1].state \
                or tab[i-1][numel - 1].state and tab[i][j].state and not tab[i][j + 1].state \
                or tab[i-1][numel - 1].state and not tab[i][j].state and tab[i][j + 1].state \
                or not tab[i-1][numel - 1].state and not tab[i][j].state and not tab[i][j + 1].state:

                    tab[i+1][j].state=True
                else:
                    tab[i+1][j].state=False

            if i>1 and j==numel-1:
                if tab[i][j - 1].state and tab[i][j].state and tab[i][0].state \
                or tab[i][j - 1].state and tab[i][j].state and not tab[i][0].state \
                or tab[i][j - 1].state and not tab[i][j].state and tab[i][0].state \
                or not tab[i][j - 1].state and not tab[i][j].state and not tab[i][0].state:

                    tab[i+1][j].state=True
                else:
                    tab[i+1][j].state=False

            elif tab[i][j - 1].state and tab[i][j].state and tab[i][j + 1].state \
                or tab[i][j - 1].state and tab[i][j].state and not tab[i][j + 1].state \
                or tab[i][j - 1].state and not tab[i][j].state and tab[i][j + 1].state \
                or not tab[i][j - 1].state and not tab[i][j].state and not tab[i][j + 1].state:

                tab[i + 1][j].state = True
            else:
                tab[i + 1][j].state = False
    return tab

#var = IntVar()

tab = []

mGui = Tk()
mGui.geometry('600x745+500+30')
mGui.title('Rules')
mGui.resizable(False,False)

my_var = IntVar()
size = StringVar()
WIDTH, HEIGHT = 600, 600

rb1 = Radiobutton(mGui, text='Rule 30', variable=my_var, value=30)
rb2 = Radiobutton(mGui, text='Rule 60', variable=my_var, value=60)
rb3 = Radiobutton(mGui, text='Rule 90', variable=my_var, value=90)
rb4 = Radiobutton(mGui, text='Rule 120', variable=my_var, value=120)
rb5 = Radiobutton(mGui, text='Rule 225', variable=my_var, value=225)

but = Button(mGui,text='Show',command=selected)
but.grid(row=4, sticky='S')

lab_empty = Label(text='\nChoose the rule:\n').grid(row=0, sticky='W', padx=(5,0))

rb1.grid(row=1, sticky='W', padx=(10,0))
rb2.grid(row=2, sticky='W', padx=(10,0))
rb3.grid(row=3, sticky='W', padx=(10,0))
rb4.grid(row=4, sticky='W', padx=(10,0))
rb5.grid(row=5, sticky='W', padx=(10,0))

lab1 = Label(text='Size:').grid(row=6, column=0, sticky='S')
lab2 = Label(text='Steps:').grid(row=6, column=0, sticky='W')
entry = Entry(mGui)
entry2 = Entry(mGui)
entry.insert(END, 20)
entry2.insert(END, 20)
entry.grid(row=7, column=0, sticky='S')
entry2.grid(row=7, column=0, sticky='W')



can = Canvas(mGui, width=WIDTH, height=HEIGHT, bg="#ffffff")
can.grid(row=8, column=0)


mGui.mainloop()

