from templates import *
import webbrowser
import os
import tkinter.scrolledtext as scrolledText
from tkinter import *
from tkinter import messagebox, simpledialog
from tkinter.filedialog import askopenfilename, asksaveasfilename

class Data:
    rbg= "#56554C"
    bg = "black"
    text_c = "#ffffff"

class Paths:
    path = ""
    fontsize = 8

root = Tk()
root.title("Notepad#")
root.config(bg=Data.rbg)

btns = Frame(bg=Data.rbg)

btns.pack(side=LEFT)


class Commands:
    def run():
        fileLoc = Paths.path
        if fileLoc == "":
            messagebox.showinfo("Run Error","Path is None, Can Not run.")
        if fileLoc.endswith(".py"):
            os.system("start python "+fileLoc)
        elif fileLoc.endswith(".rb"):
            os.system("start ruby "+fileLoc)
        elif fileLoc.endswith(".java"):
            os.system("start java "+fileLoc)
        elif fileLoc.endswith(".html") or fileLoc.endswith(".htm"):
            webbrowser.open("file://"+fileLoc)
    def open():
        r = askopenfilename()
        Paths.path = r
        with open(r, "r") as f:
            global tk_scroll_txt
            tk_scroll_txt.delete(1.0, END)
            try:
                tk_scroll_txt.insert("1.0", f.read())
            except UnicodeDecodeError:
                messagebox.showinfo("Unicode Decode Error", "The File you gave can not be decoded, as, there is an unkown character, This Can Be Fixed, Just Have To Remove the Unkown Character")
    def close_file():
        global tk_scroll_txt
        tk_scroll_txt.delete(1.0, END)
        Paths.path = ""
        
    def save_as():
        fileDir = asksaveasfilename()
        global tk_scroll_txt
        gett = tk_scroll_txt.get("1.0", END)
        gettLen = len(gett)
        if gett != 0:
            gett = gett[0:gettLen-1]
            with open(fileDir, "w") as f:
                f.write(f"{gett}")
        else:
            with open(fileDir, "w") as f:
                f.write(f"{gett}") 
        Paths.path = fileDir
    class size:
        def u():
            global tk_scroll_txt
            if Paths.fontsize == 26:
                return
            Paths.fontsize += 2
            tk_scroll_txt.config(bg=Data.bg, fg="white", insertbackground='white', insertwidth=7, font=("Consolas", Paths.fontsize))
            
        def m():
            global tk_scroll_txt
            if Paths.fontsize == 2:
                return
            Paths.fontsize -= 2
            tk_scroll_txt.config(bg=Data.bg, fg="white", insertbackground='white', insertwidth=7, font=("Consolas", Paths.fontsize))
            
    def save():
        global tk_scroll_txt
        gett = tk_scroll_txt.get("1.0", END)
        gettLen = len(gett)
        gett = gett[0:gettLen-1]
        if Paths.path != "":
            with open(Paths.path, 'w') as f:
                f.write(gett)
        else:
            Commands.save_as()
    def autocomplete(widget, first, last):
        widget.insert("insert", first + last)
        widget.mark_set("insert", "insert-1c")
        return "break"
    def reload():
        global tk_scroll_txt
        tk_scroll_txt.delete(1.0, END)
        if Paths.path == "":
            messagebox.showinfo("Reload Error","Can Not reload file as current path is "+ '""')
            return
        with open(Paths.path,"r") as f:
            tk_scroll_txt.insert("1.0",f.read())


def press(keys):
    if keys.state in [4, 6] and keys.keysym == "s":
        Commands.save()
    elif keys.state in [4, 6] and keys.keysym == "p":
        Commands.size.u()
    elif keys.state in [4, 6] and keys.keysym == "m":
        Commands.size.m()
    elif keys.state == 5 and keys.keysym == "S":
        Commands.save_as()
    elif keys.state in [4, 6] and keys.keysym == "o":
        Commands.open()
    elif keys.state == 5 and keys.keysym == "C":
        Commands.close_file()
    elif keys.state == 5 and keys.keysym == "R":
        Commands.reload()
    elif keys.state in [4, 6] and keys.keysym == "r":
        Commands.run()
    else:
        return
"""
sidebar = Frame(root)

# Set the default value of the variable
tab_path = StringVar(sidebar)
tab_path.set("Tabs")
question_menu = OptionMenu(sidebar, tab_path, *["N","Y"])
question_menu.grid(row=0,column=0)
def submit():
    print(tab_path)

question_menu_submit = Button("✓", command=submit)
question_menu_submit.grid(row=0,column=1)

sidebar.pack(side=LEFT)
"""

ScrolledText = scrolledText.ScrolledText
tk_scroll_txt = ScrolledText(bg=Data.bg, fg="white", insertbackground='white', insertwidth=7, font=("Consolas", Paths.fontsize))
tk_scroll_txt.pack(expand=1,fill=BOTH)
tk_scroll_txt.bind("<Key>", press)
tk_scroll_txt.bind("(", lambda event: Commands.autocomplete(event.widget, "(", ")"))
tk_scroll_txt.bind("{", lambda event: Commands.autocomplete(event.widget, "{", "}"))
tk_scroll_txt.bind("[", lambda event: Commands.autocomplete(event.widget, "[", "]"))
tk_scroll_txt.bind("'", lambda event: Commands.autocomplete(event.widget, "'", "'"))
tk_scroll_txt.bind('"', lambda event: Commands.autocomplete(event.widget, '"', '"'))


menuBar = Menu(root, fg='#ffffff')

Filebar = Menu(menuBar, tearoff=0)
Filebar.add_command(label='Open', command=Commands.open)
Filebar.add_command(label='Save', command=Commands.save)
Filebar.add_command(label='Save as', command=Commands.save_as)
Filebar.add_command(label='Exit', command=exit)
menuBar.add_cascade(label='File', menu=Filebar)


runBar = Menu(menuBar, tearoff=0)
runBar.add_command(label='Run', command=Commands.run)
menuBar.add_cascade(label='Code', menu=runBar)

editorBar = Menu(menuBar, tearoff=0)
editorBar.add_command(label='Increase Size', command=Commands.size.u)
editorBar.add_command(label='Decrease Size', command=Commands.size.m)
menuBar.add_cascade(label='Editor', menu=editorBar)

templatesBar = Menu(menuBar, tearoff=0)
templatesBar.add_command(label="Python", command= lambda: tk_scroll_txt.insert("1.0",template("py")))
templatesBar.add_command(label="Java", command= lambda: tk_scroll_txt.insert("1.0",template("java")))
templatesBar.add_command(label="C#", command= lambda: tk_scroll_txt.insert("1.0",template("csharp")))
templatesBar.add_command(label="C++", command= lambda: tk_scroll_txt.insert("1.0",template("cpp")))
templatesBar.add_command(label="HTML", command= lambda: tk_scroll_txt.insert("1.0",template("html")))
templatesBar.add_command(label="Go/Golang", command= lambda: tk_scroll_txt.insert("1.0",template("golang")))
templatesBar.add_command(label="C", command= lambda: tk_scroll_txt.insert("1.0",template("c")))
menuBar.add_cascade(label='Template', menu=templatesBar)

root.config(menu=menuBar)
root.mainloop()