import tkinter as tk
from tkinter import ttk
from tkinter import font, messagebox, filedialog, colorchooser
import os

# starting our main program----->
main_application = tk.Tk()
main_application.geometry('1200x686')
main_application.title('7pad text editor')

#######################  main menu #######################
main_menu = tk.Menu(main_application)

# ----------- file menu--------- #
file = tk.Menu(main_menu, tearoff=False)
# file icon----->
new_icon = tk.PhotoImage(file='./menu icons/new.png')
open_icon = tk.PhotoImage(file='./menu icons/open.png')
save_icon = tk.PhotoImage(file='./menu icons/save.png')
save_as_icon = tk.PhotoImage(file='./menu icons/save_as.png')
exit_icon = tk.PhotoImage(file='./menu icons/exit.png')
# adding file commands ----->
        # global variable for path of file
url = ''
                    # new file
def new_file(event=None):
    main_application.title('7pad text editor')
    global url
    url = ''
    text_editor.delete(1.0, tk.END)
#....................................
main_application.bind("<Control-n>",new_file)
#....................................
file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Control-n', command=new_file)

                    # open file
def open_file(event=None):
    global url
    try:
        url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select file', filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    else:
        main_application.title(os.path.basename(url))
#....................................
main_application.bind("<Control-o>",open_file)
#....................................
file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Control-o', command=open_file)

                    # save file
def save_file(event=None):
    global url
    try:
        content = str(text_editor.get(1.0, tk.END))
        if url:
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',filetypes=(('Text Files','*.txt'),('All Files','*.*')))
            url.write(content)
            url.close()
    except:
        return
    else:
        new_saved_filename=url.name.split('/')[-1]
        main_application.title(new_saved_filename)
        global text_changed
        text_changed=False
#....................................
main_application.bind('<Control-s>',save_file)
#....................................
file.add_command(label='Save', image=save_icon,compound=tk.LEFT, accelerator='Control-s', command=save_file)

                    # save as file
def save_as_file(event=None):
    global url
    try:
        content=text_editor.get(1.0,tk.END)
        url=filedialog.asksaveasfile(mode='w', defaultextension='.txt',filetypes=(('Text Files','*.txt'),('All Files','*.*')))
        url.write(content)
        url.close()
    except:
        return
    else:
        new_saved_filename=url.name.split('/')[-1]
        main_application.title(new_saved_filename)
        global text_changed
        text_changed=False
#....................................
main_application.bind('<Control-Alt-s>',save_as_file)
#....................................
file.add_command(label='Save As', image=save_as_icon, compound=tk.LEFT, accelerator='Control-Alt-s',command=save_as_file)

                    # exit
def exit_func(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel('Warning','Do you want to save the file?')
            if mbox is True:
                content=text_editor.get(1.0,tk.END)
                if url:
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return
#....................................
main_application.bind('<Control-q>',exit_func)
#....................................                    
file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Control-q',command=exit_func)
# ---------adding(cascading) file menu to main menu------------ #
main_menu.add_cascade(label='File', menu=file)




# ----------- edit menu--------- #
edit = tk.Menu(main_menu, tearoff=False)
# edit icon----->
cut_icon = tk.PhotoImage(file='./menu icons/cut.png')
copy_icon = tk.PhotoImage(file='./menu icons/copy.png')
paste_icon = tk.PhotoImage(file='./menu icons/paste.png')
clear_all_icon = tk.PhotoImage(file='./menu icons/clear_all.png')
find_icon = tk.PhotoImage(file='./menu icons/find.png')
# adding edit commands ----->
                    # cut
edit.add_command(image=cut_icon, label='Cut', compound=tk.LEFT, accelerator='Ctrl+X',command=lambda:text_editor.event_generate("<Control x>"))
#####################

                    # copy
edit.add_command(image=copy_icon, label='Copy', compound=tk.LEFT, accelerator='Ctrl+C',command=lambda:text_editor.event_generate("<Control c>"))
#####################

                    # paste
edit.add_command(image=paste_icon, label='Paste', compound=tk.LEFT, accelerator='Ctrl+V',command=lambda:text_editor.event_generate("<Control v>"))
#####################

                    # clear all
edit.add_command(image=clear_all_icon, label='Clear All', compound=tk.LEFT, accelerator='Ctrl+Alt+X',command=lambda:text_editor.delete(1.0,tk.END))
#####################

                    # find
def find_func(event=None):
    find_dialog = tk.Toplevel()
    find_dialog.geometry("450x250+500+200")
    find_dialog.title('Find')
    find_dialog.resizable(0,0)

    #frame
    find_frame=ttk.LabelFrame(find_dialog,text="Find/Replace")
    find_frame.pack(pady=20)

    text_find_lbl = ttk.Label(find_frame,text='Find')
    text_find_lbl.grid(row=0,column=0,padx=4,pady=4)

    text_replace_lbl = ttk.Label(find_frame,text='Replace')
    text_replace_lbl.grid(row=1,column=0,padx=4,pady=4)

    find_input=ttk.Entry(find_frame,width=30)
    find_input.grid(row=0,column=1,padx=4,pady=4)

    replace_input=ttk.Entry(find_frame,width=30)
    replace_input.grid(row=1,column=1,padx=4,pady=4)

    def find_the_word():
        word = find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches += 1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')
    # .............................
    find_button=ttk.Button(find_frame,text='Find',command=find_the_word)
    find_button.grid(row=2,column=0,padx=4,pady=4)

    def replace_the_word():
        old_word=find_input.get()
        new_word=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(old_word,new_word)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)
    # .............................
    replace_button = ttk.Button(find_frame,text='Replace',command=replace_the_word)
    replace_button.grid(row=2,column=1,padx=4,pady=4)

    find_dialog.mainloop()

#....................................
main_application.bind('<Control-f>',find_func)

edit.add_command(image=find_icon, label='Find', compound=tk.LEFT, accelerator='Control-f',command=find_func)
# ---------adding(cascading) edit menu to main menu------------ #
main_menu.add_cascade(label='Edit', menu=edit)


# ----------- view menu--------- #
view = tk.Menu(main_menu, tearoff=False)
# edit icon----->
tool_bar_icon = tk.PhotoImage(file='./menu icons/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='./menu icons/status_bar.png')
# adding edit commands with checkbutton ----->
toolbar_var=tk.BooleanVar()
toolbar_var.set(True)
def hide_toolbar():
    global toolbar_var
    if toolbar_var:
        tool_bar.pack_forget()
        toolbar_var=False
    else:
        text_editor.pack_forget()
        tool_bar.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side = tk.BOTTOM)
        toolbar_var=True
view.add_checkbutton(image=tool_bar_icon, label='Tool Bar', compound=tk.LEFT, onvalue=True,offvalue=False,command=hide_toolbar,variable=toolbar_var)
    ############################
statusbar_var=tk.BooleanVar()
statusbar_var.set(True)
def hide_statusbar():
    global statusbar_var
    if statusbar_var:
        status_bar.pack_forget()
        statusbar_var=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(tk.BOTTOM)
        statusbar_var=True
view.add_checkbutton(image=status_bar_icon, label='Status Bar', compound=tk.LEFT, onvalue=True,offvalue=False,command=hide_statusbar,variable=statusbar_var)
# ---------adding(cascading) edit menu to main menu------------ #
main_menu.add_cascade(label='View', menu=view)


# ----------- color theme menu--------- #
color_theme = tk.Menu(main_menu, tearoff=False)
# color theme icon----->
light_default_icon = tk.PhotoImage(file='./menu icons/light_default.png')
light_plus_icon = tk.PhotoImage(file='./menu icons/light_plus.png')
dark_color_icon = tk.PhotoImage(file='./menu icons/dark.png')
red_color_icon = tk.PhotoImage(file='./menu icons/red.png')
monokai_color_icon = tk.PhotoImage(file='./menu icons/monokai.png')
night_blue_color_icon = tk.PhotoImage(file='./menu icons/night_blue.png')
# variable for color----->
theme_choice = tk.StringVar()
# adding edit commands with rediobutton ----->
# creating tuple for color icons
color_icons = (light_default_icon, light_plus_icon, dark_color_icon, red_color_icon, monokai_color_icon, night_blue_color_icon)
# creating dictionary for color and themes
color_dict = {
    'Light Default': ('#000000', '#ffffff'),
    'Light Plus': ('#474747', '#e0e0e0'),
    'Dark': ('#c4c4c4', '#2d2d2d'),
    'Red': ('#2d2d2d', '#ffe8e8'),
    'Monokai': ('#d3b744', '#474747'),
    'Night Blue': ('#ededed', '#6b9dc2')
}
# now adding all color to color theme menu
def change_theme():
    chosen_theme=theme_choice.get()
    fg,bg=color_dict[chosen_theme]
    text_editor.config(background=bg,fg=fg)
# ........................................
for i in color_dict:
    color_theme.add_radiobutton(image=color_icons[list(color_dict).index(i)], label=i, compound=tk.LEFT, variable=theme_choice,command=change_theme)
# ---------adding(cascading) color theme menu to main menu------------ #
main_menu.add_cascade(label='  Color Theme', menu=color_theme)
# ----------------------- end main menu --------------------


#######################  toolbar #######################
# adding a label to main application
tool_bar = tk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

# variables font properties:-
current_font_family = 'Abyssinica SIL'
current_font_size = 12
text_bold_status = 'normal'
text_italic_status = 'roman'
text_underline_status = 'normal'

# adding font style selector box to toolbar label and its configuration
font_tuples = list(tk.font.families())
font_tuples.sort()
font_familiy = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, state='readonly', textvariable=font_familiy)
font_box['values'] = font_tuples
font_box.current(0)
font_box.grid(row=0, column=0, padx=5, pady=5)
##################################################################

# adding font size selector box to toolbar label
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, state='readonly', textvariable=size_var)
font_size['values'] = tuple(range(8, 80, 2))
font_size.current(0)
font_size.grid(row=0, column=1, padx=5)
##################################################################

# bold button
# text_editor niche bnane k baad hi ye function banega*****
def change_bold():
    global text_bold_status
    text_property = tk.font.Font(font=text_editor['font']).actual()
    if text_property['weight'] == 'normal':
        text_bold_status = 'bold'
        weight_slant_underline = f'{text_bold_status} {text_italic_status} {text_underline_status}'
    else:
        text_bold_status = 'normal'
        weight_slant_underline = f'{text_bold_status} {text_italic_status} {text_underline_status}'
    text_editor.configure(font=(current_font_family, current_font_size, weight_slant_underline))
# ..........................
bold_icon = tk.PhotoImage(file='./menu icons/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon, command=change_bold)
bold_btn.grid(row=0, column=2, padx=5)
###################################################################


# italic button
def change_italic():
    global text_italic_status
    text_property = tk.font.Font(font=text_editor['font']).actual()
    if text_property['slant'] == 'roman':
        text_italic_status = 'italic'
        weight_slant_underline = f'{text_bold_status} {text_italic_status} {text_underline_status}'
    else:
        text_italic_status = 'roman'
        weight_slant_underline = f'{text_bold_status} {text_italic_status} {text_underline_status}'
    text_editor.configure(font=(current_font_family, current_font_size, weight_slant_underline))
italic_icon = tk.PhotoImage(file='./menu icons/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon, command=change_italic)
italic_btn.grid(row=0, column=3, padx=5)
###################################################################


# underline button
def change_underline():
    global text_underline_status
    text_property = tk.font.Font(font=text_editor['font']).actual()
    if text_property['underline'] == 0:
        text_underline_status = 'underline'
        weight_slant_underline = f'{text_bold_status} {text_italic_status} {text_underline_status}'
    else:
        text_underline_status = 'normal'
        weight_slant_underline = f'{text_bold_status} {text_italic_status} {text_underline_status}'
    text_editor.configure(font=(current_font_family, current_font_size, weight_slant_underline))
#.....................................
underline_icon = tk.PhotoImage(file='./menu icons/underline.png')
underline_btn = ttk.Button(
    tool_bar, image=underline_icon, command=change_underline)
underline_btn.grid(row=0, column=4, padx=5)
###################################################################


# font color button
def change_font_color():
    selected_color = tk.colorchooser.askcolor()
    text_editor.configure(fg=selected_color[1])
#.............................
font_color_icon = tk.PhotoImage(file='./menu icons/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon, command=change_font_color)
font_color_btn.grid(row=0, column=5, padx=5)
###################################################################


# left align button
def align_left():
    text_content = text_editor.get(1.0, tk.END)
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')
#..................................
align_left_icon = tk.PhotoImage(file='./menu icons/align_left.png')
align_left_btn = ttk.Button(
    tool_bar, image=align_left_icon, command=align_left)
align_left_btn.grid(row=0, column=6, padx=5)
###################################################################


# center align button
def align_center():
    text_content = text_editor.get(1.0, tk.END)
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')
#..................................
align_center_icon = tk.PhotoImage(file='./menu icons/align_center.png')
align_center_btn = ttk.Button(
    tool_bar, image=align_center_icon, command=align_center)
align_center_btn.grid(row=0, column=7, padx=5)
###################################################################


# right align button
def align_right():
    text_content = text_editor.get(1.0, tk.END)
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')
#.................................
align_right_icon = tk.PhotoImage(file='./menu icons/align_right.png')
align_right_btn = ttk.Button(
    tool_bar, image=align_right_icon, command=align_right)
align_right_btn.grid(row=0, column=8, padx=5)
###################################################################
# ----------------------- end toolbar --------------------




####################### text editing area #######################
text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)
scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family and font size functionality
# to use bind function we need to write like this
def change_font_family(event=None):
    global current_font_family
    current_font_family = font_familiy.get()
    weight_slant_underline = f'{text_bold_status} {text_italic_status} {text_underline_status}'
    text_editor.configure(font=(current_font_family, current_font_size, weight_slant_underline))
#........... using bind function to link combobox and function
font_box.bind("<<ComboboxSelected>>", change_font_family)


def change_font_size(event=None):
    global current_font_size
    current_font_size = size_var.get()
    weight_slant_underline = f'{text_bold_status} {text_italic_status} {text_underline_status}'
    text_editor.configure(
        font=(current_font_family, current_font_size, weight_slant_underline))
#......... using bind function to link combobox and function 
font_size.bind("<<ComboboxSelected>>", change_font_size)

# setting default size and style
text_editor.configure(font=('Abyssinica SIL', 12))
# ----------------------- end text editing area --------------------



####################### status bar #######################
status_bar = ttk.Label(main_application, text='status bar')
status_bar.pack(side=tk.BOTTOM)

text_changed=False
def text_edited_in_text_editor(event=None):
    if text_editor.edit_modified():
        global text_changed
        text_changed=True
        words = len(text_editor.get(1.0, 'end-1c').split())
        # we can use tk.END insted of end-1c but tk.END will also count
        # the \n(new line character) present in end of each line
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Words : {words}\tCharacters : {characters}')
    text_editor.edit_modified(False)
#............. binding function with status bar as per it is modified
text_editor.bind("<<Modified>>", text_edited_in_text_editor)
# ----------------------- end status bar --------------------



####################### main menu functionality #######################
# ----------------------- end main menu --------------------

# ending main application
main_application.config(menu=main_menu)
main_application.mainloop()
