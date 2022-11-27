#imports
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.font import Font
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from screeninfo import get_monitors


# for m in get_monitors():
#     print(str(m))

#the screen
root = tk.Tk()
root.title("FINAL PROJECT")
root.geometry("1537x795")
# root.configure(background='black')

#FONT
my_font = Font(
    family = 'Arial',
    size = 12,
    weight = 'bold',
)

#the muscle-skeleton images
img1 = PhotoImage(file='front_small.png')

skel_front = tk.Label(
    root,
    image=img1
)
skel_front.place(x=150,y=20)

img2 = PhotoImage(file='back_small.png')
skel_back = tk.Label(
    root,
    image=img2
)

skel_back.place(x=610,y=20)

#Skeleton Text labels
label_front = tk.Label(root, text = "FRONT")

skel_font = Font(
    family = 'Times',
    size = 24,
    weight = 'bold',
)

label_front.config(font = skel_font)   
label_front.place(x=190, y=745)

label_back = tk.Label(root, text = "BACK")

skel_font = Font(
    family = 'Times',
    size = 24,
    weight = 'bold',
)

label_back.config(font = skel_font)   
label_back.place(x=662, y=745)

#Now we need to load in the data from the static optimization output
with open('ExampleStaticOptimizationOutput.sto') as f:
    lines = f.readlines()
#need to split the text file into each variable
labels = lines[6].split('\t')
data = []
for i in range(7,len(lines)):
    temp = lines[i].split('\t')
    temp[-1] = temp[-1].replace('\n','')
    
    data.append(temp)
    
    
#initialize the empty variable lists   
time = []
hamstrings_r = []
bifesh_r = []
glut_max_r = []
iliopsoas_r = []
rect_fem_r = []
vasti_r = []
gastroc_r = []
soleus_r = []
tib_ant_r = []

hamstrings_l = []
bifesh_l = []
glut_max_l = []
iliopsoas_l = []
rect_fem_l = []
vasti_l = []
gastroc_l = []
soleus_l = []
tib_ant_l = []

fx = []
fy = []
mz = []

hip_flexion_r_reserve = []
knee_angle_r_reserve = []
ankle_angle_r_reserve = []

hip_flexion_l_reserve = []
knee_angle_l_reserve = []
ankle_angle_l_reserve = []

#appending each data point in each row to its respective variable list
lumbar_extension_reserve =[]
for i in range(0,len(data)):
    tmp = float(data[i][0])-float(data[0][0])
    time.append(tmp)
    hamstrings_r.append(float(data[i][1]))
    bifesh_r.append(float(data[i][2]))
    glut_max_r.append(float(data[i][3]))
    iliopsoas_r.append(float(data[i][4]))
    rect_fem_r.append(float(data[i][5]))
    vasti_r.append(float(data[i][6]))
    gastroc_r.append(float(data[i][7]))
    soleus_r.append(float(data[i][8]))
    tib_ant_r.append(float(data[i][9]))
    hamstrings_l.append(float(data[i][10]))
    bifesh_l.append(float(data[i][11]))
    glut_max_l.append(float(data[i][12]))
    iliopsoas_l.append(float(data[i][13]))
    rect_fem_l.append(float(data[i][14]))
    vasti_l.append(float(data[i][15]))
    gastroc_l.append(float(data[i][16]))
    soleus_l.append(float(data[i][17]))
    tib_ant_l.append(float(data[i][18]))
    
    fx.append(float(data[i][19]))
    fy.append(float(data[i][20]))
    mz.append(float(data[i][21]))

    hip_flexion_r_reserve.append(float(data[i][22]))
    knee_angle_r_reserve.append(float(data[i][23]))
    ankle_angle_r_reserve.append(float(data[i][24]))

    hip_flexion_l_reserve.append(float(data[i][25]))
    knee_angle_l_reserve.append(float(data[i][26]))
    ankle_angle_l_reserve.append(float(data[i][27]))

    lumbar_extension_reserve.append(float(data[i][28]))


#Estblish the functions that will drive functionality of the GUI
def plotMe(time,variablel,variabler,state,string):
    fig = Figure(figsize = (7.2,4.7), facecolor='white')
    a = fig.add_subplot(111)
    if state == '0':
        
        print("This variable doesn't have left vs right")
        a.plot(time,variabler, 'r')
        a.set_xlabel('Time')
        a.set_ylabel('Extension')
        a.set_title(string+ ' vs Time')
    if state == 'right':
        a.plot(time,variabler, 'r')
        a.set_xlabel('Time')
        if string in ['Ankle','Knee','Hip Flexion']:
            a.set_ylabel('Angle')
        else:
            a.set_ylabel('Output')
        a.set_title(state.capitalize() + ' ' + string+ ' vs Time')
    if state == 'left':
        a.plot(time,variablel,'b')
        a.set_xlabel('Time')
        if string in ['Ankle','Knee','Hip Flexion']:
            a.set_ylabel('Angle')
        else:
            a.set_ylabel('Output')
        a.set_title(state.capitalize() + ' ' + string+ ' vs Time')
    if state == 'both':
        a.plot(time,variablel, 'b',label = 'Left Leg')
        a.plot(time,variabler,'r', label = 'Right Leg')
        a.set_xlabel('Time')
        if string in ['Ankle','Knee','Hip Flexion']:
            a.set_ylabel('Angle')
        else:
            a.set_ylabel('Output')
        if string[-1] == 's':
            a.set_title(state.capitalize() + ' ' + string + ' vs Time')
        else:
            a.set_title(state.capitalize() + ' ' + string +"s" + ' vs Time')
        fig.legend()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x=990, y=375)
    

def plotForce(time,force,state):
    fig = Figure(figsize = (7.2,4.7), facecolor='white')
    a = fig.add_subplot(111)
    a.plot(time,force,color = 'red')
    a.set_xlabel('Time')
    a.set_ylabel('Output')
    if state == 'FX':
        a.set_title('Fx vs Time')
    if state == 'FY':
        a.set_title('Fy vs Time')
    if state == 'MZ':
        a.set_title('Mz vs Time')
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x=990, y=375)

def plotAll(time,hamstrings_l,bifesh_l,glut_max_l,iliopsoas_l,rect_fem_l,vasti_l,gastroc_l,soleus_l,tib_ant_l,hamstrings_r,bifesh_r,glut_max_r,iliopsoas_r,rect_fem_r,vasti_r,gastroc_r,soleus_r,tib_ant_r, state,muscle_list):
    fig = Figure(figsize = (7.2,4.7), facecolor='white')
    a = fig.add_subplot(111)
    graphing_muscles = []
    if state == 'left':
        if "- Hamstrings\n\n" in muscle_list:
            graphing_muscles.append(hamstrings_l)
        if "- Biceps Femoris\n\n" in muscle_list:
            graphing_muscles.append(bifesh_l)
        if "- Gluteus Maximus\n\n" in muscle_list:
            graphing_muscles.append(glut_max_l)    
        if "- Iliopsoas\n\n" in muscle_list:
            graphing_muscles.append(iliopsoas_l)   
        if "- Rectus Femoris\n\n" in muscle_list:
            graphing_muscles.append(rect_fem_l)
        if "- Vastus muscles\n\n" in muscle_list:
            graphing_muscles.append(vasti_l)
        if "- Gastrocnemius\n\n" in muscle_list:
            graphing_muscles.append(gastroc_l)
        if "- Soleus\n\n" in muscle_list:
            graphing_muscles.append(soleus_l)
        if "- Tibialis Anterior\n\n" in muscle_list:
            graphing_muscles.append(tib_ant_l)
    if state == 'right':
        if "- Hamstrings\n\n" in muscle_list:
            graphing_muscles.append(hamstrings_r)
        if "- Biceps Femoris\n\n" in muscle_list:
            graphing_muscles.append(bifesh_r)
        if "- Gluteus Maximus\n\n" in muscle_list:
            graphing_muscles.append(glut_max_r)    
        if "- Iliopsoas\n\n" in muscle_list:
            graphing_muscles.append(iliopsoas_r)   
        if "- Rectus Femoris\n\n" in muscle_list:
            graphing_muscles.append(rect_fem_r)
        if "- Vastus muscles\n\n" in muscle_list:
            graphing_muscles.append(vasti_r)
        if "- Gastrocnemius\n\n" in muscle_list:
            graphing_muscles.append(gastroc_r)
        if "- Soleus\n\n" in muscle_list:
            graphing_muscles.append(soleus_r)
        if "- Tibialis Anterior\n\n" in muscle_list:
            graphing_muscles.append(tib_ant_r)
    if state == 'both':
        if "- Hamstrings\n\n" in muscle_list:
            graphing_muscles.append(hamstrings_r)
            graphing_muscles.append(hamstrings_l)
        if "- Biceps Femoris\n\n" in muscle_list:
            graphing_muscles.append(bifesh_r)
            graphing_muscles.append(bifesh_l)
        if "- Gluteus Maximus\n\n" in muscle_list:
            graphing_muscles.append(glut_max_r)
            graphing_muscles.append(glut_max_l)  
        if "- Iliopsoas\n\n" in muscle_list:
            graphing_muscles.append(iliopsoas_r)
            graphing_muscles.append(iliopsoas_l) 
        if "- Rectus Femoris\n\n" in muscle_list:
            graphing_muscles.append(rect_fem_r)
            graphing_muscles.append(rect_fem_l)
        if "- Vastus muscles\n\n" in muscle_list:
            graphing_muscles.append(vasti_r)
            graphing_muscles.append(vasti_l)
        if "- Gastrocnemius\n\n" in muscle_list:
            graphing_muscles.append(gastroc_r)
            graphing_muscles.append(gastroc_l)
        if "- Soleus\n\n" in muscle_list:
            graphing_muscles.append(soleus_r)
            graphing_muscles.append(soleus_l)
        if "- Tibialis Anterior\n\n" in muscle_list:
            graphing_muscles.append(tib_ant_r)
            graphing_muscles.append(tib_ant_l)
    
    a.set_xlabel('Time')
    a.set_ylabel('Output')
    for i in range(0,len(muscle_list)):
        muscle_list[i].replace('\n\n','').replace('- ','')
    i = 0
    if state == 'left' or state == 'right':
        for ele in graphing_muscles:
            a.plot(time,ele,label = str(muscle_list[i]))
            fig.legend() 
            i = i+1
    if state == 'both':
        muscle_right = [(muscle_list[i] + ' right').replace('\n\n','').replace('- ','') for i in range(0,len(muscle_list))]
        muscle_left = [(muscle_list[i] + ' left').replace('\n\n','').replace('- ','') for i in range(0,len(muscle_list))]
        muscle_combined = []
        for i in range(0,len(muscle_right)):
            muscle_combined.append(muscle_right[i])
            muscle_combined.append(muscle_left[i])
        
        j = 0
        for ele in graphing_muscles:
            
            a.plot(time,ele,label = str(muscle_combined[j]))
            fig.legend() 
            j = j+1
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x=990, y=375)
#The muscles that will be outputted in the textbox
muscle_list = []

#these functions control what happens when the user selects it
def hamstrings1():
    hamstrings = tk.Button(root, text="Hamstrings", command = lambda:hamstrings2(), font = my_font, borderwidth=2, 
                           relief="solid", fg='white',bg='#345', cursor='hand2', padx=5, pady=5).place(x=522, y=384)
    muscle_list.append("- Hamstrings\n\n")
    Output.insert(tk.END, "- Hamstrings\n\n")
    plotMe(time,hamstrings_l,hamstrings_r,var.get(),'Hamstring')
    
def bifemsh1():
    bifemsh = tk.Button(root, text="Biceps Femoris", command = lambda:bifemsh2(), font = my_font, borderwidth=2, relief="solid", fg='white',bg='#345', cursor='hand2', padx=5, pady=5).place(x=798, y=430)
    muscle_list.append("- Biceps Femoris\n\n")
    Output.insert(tk.END, "- Biceps Femoris\n\n")
    plotMe(time,bifesh_l,bifesh_r,var.get(),'Bicep Femoris')
    
def glut_max1():
    glut_max = tk.Button(root, text="Gluteus Maximus", command = lambda:glut_max2(), font = my_font, borderwidth=2, relief="solid", fg='white',bg='#345', cursor='hand2', padx=5, pady=5).place(x=798, y=306)
    muscle_list.append("- Gluteus Maximus\n\n")
    Output.insert(tk.END, "- Gluteus Maximus\n\n")
    plotMe(time,glut_max_l,glut_max_r,var.get(),'Gluteus Maximus')
    
def iliopsoas1():
    iliopsoas = tk.Button(root, text="Iliopsoas", command = lambda:iliopsoas2(), font = my_font, borderwidth=2, relief="solid", fg='white',bg='#345', cursor='hand2', padx=5, pady=5).place(x=340, y=264)
    muscle_list.append("- Iliopsoas\n\n")
    Output.insert(tk.END, "- Iliopsoas\n\n")
    plotMe(time,iliopsoas_l,iliopsoas_l,var.get(),'Iliopsoas')
    
def rect_fem1():
    rect_fem = tk.Button(root, text="Rectus Femoris", command = lambda:rect_fem2(), font = my_font, borderwidth=2, relief="solid", fg='white',bg='#345', cursor='hand2', padx=5, pady=5).place(x=30, y=366)
    muscle_list.append("- Rectus Femoris\n\n")
    Output.insert(tk.END, "- Rectus Femoris\n\n")
    plotMe(time,rect_fem_l,rect_fem_l,var.get(),'Rectus Femoris')
    
def vasti1():
    vasti = tk.Button(root, text="Vastus muscles", command = lambda:vasti2(), font = my_font, borderwidth=2, relief="solid", fg='white',bg='#345', cursor='hand2', padx=5, pady=5).place(x=340, y=412)
    muscle_list.append("- Vastus muscles\n\n")
    Output.insert(tk.END, "- Vastus muscles\n\n")
    plotMe(time,vasti_l,vasti_r,var.get(),'Vastus Lateralis')

def gastroc1():
    gastroc = tk.Button(root, text="Gastrocnemius", command = lambda:gastroc2(), font = my_font, borderwidth=2, relief="solid", fg='white',bg='#345', cursor='hand2', padx=5, pady=5).place(x=492, y=532)
    muscle_list.append("- Gastrocnemius\n\n")
    Output.insert(tk.END, "- Gastrocnemius\n\n")   
    plotMe(time,gastroc_l,gastroc_r,var.get(),'Gastrocnemius')

def soleus1():
    soleus = tk.Button(root, text="Soleus", command = lambda:soleus2(), font = my_font, borderwidth=2, relief="solid", fg='white',bg='#345', cursor='hand2', padx=5, pady=5).place(x=798, y=604)
    muscle_list.append("- Soleus\n\n")
    Output.insert(tk.END, "- Soleus\n\n")
    plotMe(time,soleus_l,soleus_r,var.get(),'Soleus')

def tib_ant1():
    tib_ant = tk.Button(root, text="Tibialis Anterior", command = lambda:tib_ant2(), font = my_font, borderwidth=2, relief="solid", fg='white',bg='#345', cursor='hand2', padx=5, pady=5).place(x=30, y=566)
    muscle_list.append("- Tibialis Anterior\n\n")
    Output.insert(tk.END, "- Tibialis Anterior\n\n")   
    plotMe(time,tib_ant_l,tib_ant_r,var.get(),'Tibialis Anterior')
def graph_all1():
    plotAll(time,hamstrings_l,bifesh_l,glut_max_l,iliopsoas_l,rect_fem_l,vasti_l,gastroc_l,soleus_l,tib_ant_l,hamstrings_r,bifesh_r,glut_max_r,iliopsoas_r,rect_fem_r,vasti_r,gastroc_r,soleus_r,tib_ant_r, var.get(),muscle_list)

#this is the textbox with muscle list
listbox = tk.Label(root, text = "Selected Muscles")

my_font2 = Font(
    family = 'Times',
    size = 20,
    weight = 'bold',
    underline = 1,
)

listbox.config(font = my_font2)   
listbox.place(x=1152, y=10)

Output = tk.Text(root, height = 9, width = 30, fg = 'white', bg = "black", padx=20, pady=10, font=my_font)
Output.place(x=1100, y=50)


#The functions will control the button when the user de-selects it
def hamstrings2():
    hamstrings = tk.Button(root, text="Hamstrings", command = lambda:hamstrings1(), font = my_font, borderwidth=2, 
                           relief="solid", bg='white',fg='black', cursor='hand2', padx=5, pady=5).place(x=522, y=384)
    Output.delete('1.0', tk.END)
    muscle_list.remove("- Hamstrings\n\n")
    muscle_string = ''.join(muscle_list)
    Output.insert(tk.END, muscle_string)  
    
def bifemsh2():
    bifemsh = tk.Button(root, text="Biceps Femoris", command = lambda:bifemsh1(), font = my_font, borderwidth=2, relief="solid", bg='white',fg='black', cursor='hand2', padx=5, pady=5).place(x=798, y=430)
    Output.delete('1.0', tk.END)
    muscle_list.remove("- Biceps Femoris\n\n")
    muscle_string = ''.join(muscle_list)
    Output.insert(tk.END, muscle_string) 
    
def glut_max2():
    glut_max = tk.Button(root, text="Gluteus Maximus", command = lambda:glut_max1(), font = my_font, borderwidth=2, relief="solid", bg='white',fg='black', cursor='hand2', padx=5, pady=5).place(x=798, y=306)
    Output.delete('1.0', tk.END)
    muscle_list.remove("- Gluteus Maximus\n\n")
    muscle_string = ''.join(muscle_list)
    Output.insert(tk.END, muscle_string)  
    
def iliopsoas2():
    iliopsoas = tk.Button(root, text="Iliopsoas", command = lambda:iliopsoas1(), font = my_font, borderwidth=2, relief="solid", bg='white',fg='black', cursor='hand2', padx=5, pady=5).place(x=340, y=264)
    Output.delete('1.0', tk.END)
    muscle_list.remove("- Iliopsoas\n\n")
    muscle_string = ''.join(muscle_list)
    Output.insert(tk.END, muscle_string)  
    
def rect_fem2():
    rect_fem = tk.Button(root, text="Rectus Femoris", command = lambda:rect_fem1(), font = my_font, borderwidth=2, relief="solid", bg='white',fg='black', cursor='hand2', padx=5, pady=5).place(x=30, y=366)
    Output.delete('1.0', tk.END)
    muscle_list.remove("- Rectus Femoris\n\n")
    muscle_string = ''.join(muscle_list)
    Output.insert(tk.END, muscle_string)  
    
def vasti2():
    vasti = tk.Button(root, text="Vastus muscles", command = lambda:vasti1(), font = my_font, borderwidth=2, relief="solid", bg='white',fg='black', cursor='hand2', padx=5, pady=5).place(x=340, y=412)
    Output.delete('1.0', tk.END)
    muscle_list.remove("- Vastus muscles\n\n")
    muscle_string = ''.join(muscle_list)
    Output.insert(tk.END, muscle_string)  
    
def gastroc2():
    gastroc = tk.Button(root, text="Gastrocnemius", command = lambda:gastroc1(), font = my_font, borderwidth=2, relief="solid", bg='white',fg='black', cursor='hand2', padx=5, pady=5).place(x=492, y=532)
    Output.delete('1.0', tk.END)
    muscle_list.remove("- Gastrocnemius\n\n")
    muscle_string = ''.join(muscle_list)
    Output.insert(tk.END, muscle_string)  
    
def soleus2():
    soleus = tk.Button(root, text="Soleus", command = lambda:soleus1(), font = my_font, borderwidth=2, relief="solid", bg='white',fg='black', cursor='hand2', padx=5, pady=5).place(x=798, y=604)
    Output.delete('1.0', tk.END)
    muscle_list.remove("- Soleus\n\n")
    muscle_string = ''.join(muscle_list)
    Output.insert(tk.END, muscle_string)  
    
def tib_ant2():
    tib_ant = tk.Button(root, text="Tibialis Anterior", command = lambda:tib_ant1(), font = my_font, borderwidth=2, relief="solid", bg='white',fg='black', cursor='hand2', padx=5, pady=5).place(x=30, y=566)
    Output.delete('1.0', tk.END)
    muscle_list.remove("- Tibialis Anterior\n\n")
    muscle_string = ''.join(muscle_list)
    Output.insert(tk.END, muscle_string)  
    
    
#all of the buttons for the muscles
#FRONT
iliopsoas = tk.Button(root, text="Iliopsoas", command = lambda:iliopsoas1(), font = my_font, borderwidth=2, relief="solid", activebackground='#345',activeforeground='white', cursor='hand2', padx=5, pady=5).place(x=340, y=264)

rect_fem = tk.Button(root, text="Rectus Femoris", command = lambda:rect_fem1(), font = my_font, borderwidth=2, relief="solid", activebackground='#345',activeforeground='white', cursor='hand2', padx=5, pady=5).place(x=30, y=366)

vasti = tk.Button(root, text="Vastus muscles", command = lambda:vasti1(), font = my_font, borderwidth=2, relief="solid", activebackground='#345',activeforeground='white', cursor='hand2', padx=5, pady=5).place(x=340, y=412)

tib_ant = tk.Button(root, text="Tibialis Anterior", command = lambda:tib_ant1(), font = my_font, borderwidth=2, relief="solid", activebackground='#345',activeforeground='white', cursor='hand2', padx=5, pady=5).place(x=30, y=566)


#BACK
glut_max = tk.Button(root, text="Gluteus Maximus", command = lambda:glut_max1(), font = my_font, borderwidth=2, relief="solid", activebackground='#345',activeforeground='white', cursor='hand2', padx=5, pady=5).place(x=798, y=306)

hamstrings = tk.Button(root, text="Hamstrings", command = lambda:hamstrings1(), font = my_font, borderwidth=2, relief="solid", bg='white',fg='black', cursor='hand2', padx=5, pady=5).place(x=522, y=384)

bifemsh = tk.Button(root, text="Biceps Femoris", command = lambda:bifemsh1(), font = my_font, borderwidth=2, relief="solid", activebackground='#345',activeforeground='white', cursor='hand2', padx=5, pady=5).place(x=798, y=430)

gastroc = tk.Button(root, text="Gastrocnemius", command = lambda:gastroc1(), font = my_font, borderwidth=2, relief="solid", activebackground='#345',activeforeground='white', cursor='hand2', padx=5, pady=5).place(x=492, y=532)

soleus = tk.Button(root, text="Soleus", command = lambda:soleus1(), font = my_font, borderwidth=2, relief="solid", activebackground='#345',activeforeground='white', cursor='hand2', padx=5, pady=5).place(x=798, y=604)

#GRAPH ALL BUTTON
graph_all = tk.Button(root, text="Graph Selected", command = lambda:graph_all1(), font = my_font, borderwidth=2, relief="raised", bg = 'green', fg = 'white', activebackground='white',activeforeground='green', cursor='hand2', padx=5).place(x=1180, y=735)


'''
whatever the user selects in the radiobutton will be stored in var. 

This can be accessed by: var.get()

the values will either be "left" or "right" or "both"

please edit the leg() function. Print statement is just an example
'''
var = tk.StringVar()

#I have it set to default to the left leg
var.set("left")
 
def leg(value):
    print(value)
    return value

#radiobutton font
my_font3 = Font(
    family = 'Futura',
    size = 18,
    weight = 'bold',
)

#3 radiobuttons
R1 = tk.Radiobutton(root, text="L", font=my_font3, variable=var, command = lambda:leg(var.get()), value="left", cursor='hand2').place(x=1105, y = 250)

R2 = tk.Radiobutton(root, text="R", font=my_font3, variable=var, command = lambda:leg(var.get()), value="right", cursor='hand2').place(x=1205, y=250)

R3 = tk.Radiobutton(root, text="Both", font=my_font3, variable=var, command = lambda:leg(var.get()), value="both", cursor='hand2').place(x=1305, y = 250)


# Dropdown menu options
force_options = ["Forces","FX","FY","MZ"]
angle_options = ["Angles","Hip Flexion","Knee","Ankle", "Lumbar Extension"]

  
# datatype of menu text
clicked_force = tk.StringVar()
clicked_angle = tk.StringVar()
  
'''
whatever the user selects in the dropdowns will be stored in StringVar(). 

This can be accessed by: clicked_force.get() and clicked_angle.get()

the values will either be strings, "FX","FY","MZ" and "Hip Flexion","Knee","Ankle", "Lumbar Extension"

please edit the 2 functions below. Print statement is just an example
'''

def force_selection(event):
    force_selected = clicked_force.get()
    print(force_selected)
    
    if force_selected == 'FX':
        plotForce(time,fx,force_selected)
    if force_selected == 'FY':
        plotForce(time,fy,force_selected)
    if force_selected == 'MZ':
        plotForce(time,mz,force_selected)
    
    return force_selected
  
def angle_selection(event):
   angle_selected = clicked_angle.get()
   if angle_selected == "Hip Flexion":
       plotMe(time,hip_flexion_l_reserve,hip_flexion_r_reserve, var.get(),'Hip Flexion')
   if angle_selected == 'Knee':
       plotMe(time,knee_angle_l_reserve,knee_angle_r_reserve, var.get(),'Knee')
   if angle_selected == 'Ankle':
       plotMe(time,ankle_angle_l_reserve,ankle_angle_r_reserve, var.get(),'Ankle')
   if angle_selected == 'Lumbar Extension':
       plotMe(time,lumbar_extension_reserve,lumbar_extension_reserve, '0','Lumbar Extension')
   print(angle_selected)
   
   return angle_selected

#dropdown fonts
style = ttk.Style()

my_font4 = Font(
    family = 'Arial',
    size = 14,
)

style.configure("TMenubutton", font=my_font3)

#Create Dropdown menus
force_menu = ttk.OptionMenu(root,clicked_force,*force_options, command = force_selection)
force_menu['menu'].configure(font=my_font4)
force_menu.place(x=1105, y = 300)

angle_menu = ttk.OptionMenu(root,clicked_angle,*angle_options, command = angle_selection)
angle_menu['menu'].configure(font=my_font4)
angle_menu.place(x=1280, y = 300)

#root.attributes('-fullscreen', True)
exit_button = tk.Button(root, text='Exit', font = my_font, relief="raised", bg = 'red', fg = 'white', activebackground='red',activeforeground='white', cursor='hand2', padx=5, pady=5, command = root.destroy)
exit_button.place(x=1485, y=0)

root.resizable(width=False, height=False)
root.mainloop()