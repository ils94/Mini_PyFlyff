from tkinter import Toplevel, Label, LEFT, Button, X, PhotoImage
import os

text = """How to use this tool:

•Separate every key with commas ","
•Separate every timer with commas ","

You can enable/disable Alt Control keys by clicking the button to 
enable/disable it.

You can set up timers for each key in the Mini Ftool. Each timer 
will be executed once that key is pressed.

You can create a shortcut to make it easier to start/stop the 
Mini Ftool loop.

You can check the box "Make Timers Random" to generate a random
delay between each key press.

You can start/stop the Mini Ftool loop by clicking the button to 
Start/Stop it, you also can setup a shortcut.

You can enable/disable the Mini Ftool by clicking the button to
enable/disable it.

Click the button below to see a picture of a valid Mini PyFlyff 
configuration:"""


def open_help():
    help_window = Toplevel()

    window_width = 400
    window_height = 425

    screen_width = help_window.winfo_screenwidth()
    screen_height = help_window.winfo_screenheight()

    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)

    help_window.geometry("400x425+" + str(int(x)) + "+" + str(int(y)))

    help_window.title("Help")
    if os.path.isfile("icon/PyFlyff.ico"):
        help_window.iconbitmap("icon/PyFlyff.ico")
    help_window.resizable(False, False)

    help_label = Label(help_window, text=text, anchor="w", justify=LEFT)
    help_label.pack(fill=X, padx=5, pady=5)

    button_help = Button(help_window, text="Show Image", command=show_image_window)
    button_help.pack(padx=5, pady=5)

    help_window.mainloop()


def show_image_window():
    tutorial_image_window = Toplevel()

    window_width = 260
    window_height = 325

    screen_width = tutorial_image_window.winfo_screenwidth()
    screen_height = tutorial_image_window.winfo_screenheight()

    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)

    tutorial_image_window.geometry("260x325+" + str(int(x)) + "+" + str(int(y)))

    tutorial_image_window.title("Image Tutorial")
    if os.path.isfile("icon/PyFlyff.ico"):
        tutorial_image_window.iconbitmap("icon/PyFlyff.ico")
    tutorial_image_window.resizable(False, False)

    image_label = Label(tutorial_image_window)
    image_label.la = PhotoImage(file='help/help.PNG')
    image_label['image'] = image_label.la
    image_label.place(x=0, y=0)
