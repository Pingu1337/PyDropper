import tkinter as tk
import tkinter.ttk as ttk
import pyautogui
import keyboard
import pyperclip
import colormap
import re
import webbrowser

last_color = '#fff'

def callback(url):
    webbrowser.open_new(url)

def on_closing():
    global newWindow
    settings()
    newWindow.destroy()
    

def print_value(val):
    print('value: ' + str(val))

def openNewWindow():
    global newWindow
    global c1
    newWindow = tk.Toplevel(root)
    newWindow.attributes('-topmost', True)
    newWindow.resizable(False, False)
    newWindow.iconbitmap('ico\settings.ico')
    newWindow.title("settings")
    width = 210
    height = 200
    x = root.winfo_x() + 50
    y = root.winfo_y() + 10
    newWindow.geometry('%dx%d+%d+%d' % (width, height, x, y))

    newWindow.protocol("WM_DELETE_WINDOW", on_closing)
 
    tk.Label(newWindow,
          text ="EyeDropper settings").pack()
    c1 = tk.Checkbutton(newWindow, text='always on top',variable=var1, onvalue=1, offvalue=0)
    c1.pack()

    drop_var = var2

    languages = ['HEX', 'RGB']
                        
    drop = ttk.OptionMenu(newWindow, drop_var,var2.get() , *languages)
    drop.pack()

    link1 = tk.Label(newWindow, text="GitHub", fg="blue", cursor="hand2")
    link1.pack(expand=True)
    link1.bind("<Button-1>", lambda e: callback("https://github.com/Pingu1337"))

    ok_btn = tk.Button(newWindow, text = 'Save', command = on_closing, padx=10, pady=5)
    ok_btn.pack(expand=True)

def settings():
    global frame
    global another_frame
    global btn

    if (var1.get() == 1):
        root.attributes('-topmost', True)
    elif (var1.get() == 0):
        root.attributes('-topmost', False)
    if(var2.get() == 'HEX'):
        width = 300
        height = 50
        another_frame.place(x=80,y=10)
        frame.place(x=10,y=10)
        btn.place(x=245, y=10) 

    elif(var2.get() == 'RGB'):
        width = 310
        height = 50
        another_frame.place(x=110,y=10)
        btn.place(x=270, y=10)
        
    root.geometry('%dx%d' % (width, height))
    root.update()

def getColor():
    while True: 
        global last_color
        posXY = pyautogui.position() 
        color = pyautogui.pixel(posXY[0], posXY[1])
        win_x  = root.winfo_x()
        win_y  = root.winfo_y()
        win_w = root.winfo_width()
        win_h = root.winfo_height()
        win_left = win_x + win_w
        win_bottom = win_y + win_h

        if (posXY[1] >= win_y and posXY[1] <= win_bottom + 32):
            mouse_y = True
        else:
            mouse_y = False
        
        if(posXY[0] >= win_x and posXY[0] <= win_left + 10):
            mouse_x = True
        else:
            mouse_x = False

        color = re.sub('[()]', '', str(color))
        color = color.split(',')
        r = color[0].strip()
        g = color[1].strip()
        b = color[2].strip()
        hexcolor = colormap.rgb2hex(int(r),int(g),int(b))

        if (mouse_y and mouse_x):
            hexcolor = last_color
        
        return(hexcolor)

def getRgb():
    while True: 
        global last_color_rgb
        posXY = pyautogui.position() 
        color = pyautogui.pixel(posXY[0], posXY[1])
        win_x  = root.winfo_x()
        win_y  = root.winfo_y()
        win_w = root.winfo_width()
        win_h = root.winfo_height()
        win_left = win_x + win_w
        win_bottom = win_y + win_h

        if (posXY[1] >= win_y and posXY[1] <= win_bottom + 32):
            mouse_y = True
        else:
            mouse_y = False
        
        if(posXY[0] >= win_x and posXY[0] <= win_left + 10):
            mouse_x = True
        else:
            mouse_x = False

        output = color

        if (mouse_y and mouse_x):
            output = last_color_rgb

        return(output)

def get_complementary(c):

        c = c[1:];      
        rgb = int(c, 16);   
        r = (rgb >> 16) & 0xff;  
        g = (rgb >>  8) & 0xff;  
        b = (rgb >>  0) & 0xff; 

        luma = 0.2126 * r + 0.7152 * g + 0.0722 * b
        if (luma < 40):
            return('#fff')
        else:
            return('#000')

def get_icon_color(c):
        c = c[1:];      
        rgb = int(c, 16);   
        r = (rgb >> 16) & 0xff;  
        g = (rgb >>  8) & 0xff;  
        b = (rgb >>  0) & 0xff; 

        luma = 0.2126 * r + 0.7152 * g + 0.0722 * b
        if (luma < 40):
            return(settings_light)
        else:
            return(settings_dark)

root = tk.Tk()

width = 300
height = 50

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y/2))

#stored variables
var1 = tk.IntVar(value=1)
var2 = tk.StringVar(value='HEX')

root.iconbitmap('ico\eyedropper.ico')
settings_dark = tk.PhotoImage(file='img\cogwheel32.png')
settings_light = tk.PhotoImage(file='img\cogwheel32light.png')
root.resizable(False, False)
root.update()
def Draw():
    global text
    global txt
    global frame
    global another_frame
    global btn
    frame=tk.Frame(root,width=100,height=30,relief='solid',bd=0)
    frame.place(x=10,y=10)
    another_frame=tk.Frame(root,width=300,height=30,relief='solid',bd=0)
    another_frame.place(x=80,y=10)
    root.title('EyeDropper v1.0')
    text=tk.Label(frame,text='EyeDropper v1.0', fg='#fff')
    text.pack()
    txt=tk.Label(another_frame,text="press 'c' to copy color code",fg='#fff')
    txt.pack()
    btn = tk.Button(root,image=settings_light,borderwidth=0, text = 'settings', command = openNewWindow, pady=10)
    btn.place(x=245, y=10)

def Refresher():
    global text
    global txt
    global another_frame
    global btn
    global last_color
    global last_color_rgb
    color = getColor()
    last_color = color
    inverted = get_complementary(color)

    if(var2.get() == 'HEX'):
        output_color = getColor()
        last_color = color
    if(var2.get() == 'RGB'):
        output_color = getRgb()
        last_color_rgb = output_color
        output_color = 'rgb' + str(output_color)

    text.configure(text=output_color,bg=color,fg=inverted)
    txt.configure(bg=color,fg=inverted)
    frame.configure(bg=color)
    another_frame.configure(bg=color)
    btn.configure(bg=color, image=get_icon_color(color))
    root.configure(background=color)
    if keyboard.is_pressed('c'):
        pyperclip.copy(str(output_color))
        text.configure(text='Copied!')
    root.after(10, Refresher)
Draw()
settings()
Refresher()
root.mainloop()
