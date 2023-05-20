from tkinter import Toplevel, Label, LEFT, Button, X, PhotoImage
import os


def open_help():
    help_window = Toplevel()

    window_width = 450
    window_height = 650

    screen_width = help_window.winfo_screenwidth()
    screen_height = help_window.winfo_screenheight()

    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)

    help_window.geometry("450x650+" + str(int(x)) + "+" + str(int(y)))

    help_window.title("Help")
    if os.path.isfile("icon/PyFlyff.ico"):
        help_window.iconbitmap("icon/PyFlyff.ico")
    help_window.resizable(False, False)

    help_label = Label(help_window, text="How to use this tool:"
                                         '\n\n•Separate every key with commas ",".'
                                         '\n\n•Separate every timer with commas ",".'
                                         '\n\n•Click the "Save Key(s)" button to save your current keys.'
                                         '\n\n•To Start/Stop the Mini Ftool loop, press the "Start/Stop" button.'
                                         '\n\nHere is an example of configuration:'
                                         '\n\nAlt Control Key(s): 1,2,3,4,5'
                                         '\n\nThis means that whenever you press either 1,2,3,4 or 5, it will'
                                         '\nthen send those keys to your Alt Client.'
                                         '\n\nMini Ftool Key(s): f1,f2,f3'
                                         '\n\nThis means that when you start the Mini Ftool loop, it will then'
                                         '\nsend those keys sequentially to your Alt Client.'
                                         '\n\nMini Ftool Key(s) Timers: 1,5,10'
                                         '\n\nThis means that after the first key is pressed, there will be'
                                         '\n1 second delay for the second key to be pressed, which will then have'
                                         '\na 5 seconds delay to press the third key, which will then, finally,'
                                         '\nhave 10 seconds delay to start over.'
                                         '\n\nChecking the "Make Timers Random" checkbox, will make it so there will be'
                                         '\na random number that will be generated between 0 and the number you choose.'
                                         '\n\nFollowing the previous example we have:'
                                         '\n\n•A number between 0 - 1.'
                                         '\n•A number between 0 - 5.'
                                         '\n•A number between 0 - 10.'
                                         '\n\nClick the button below to show an image of the tutorial above:',
                       anchor="w", justify=LEFT)
    help_label.pack(fill=X, padx=5, pady=5)

    button_help = Button(help_window, text="Show Image", command=show_image_window)
    button_help.pack(padx=5, pady=5)

    help_window.mainloop()


def show_image_window():
    tutorial_image_window = Toplevel()

    window_width = 260
    window_height = 290

    screen_width = tutorial_image_window.winfo_screenwidth()
    screen_height = tutorial_image_window.winfo_screenheight()

    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)

    tutorial_image_window.geometry("260x290+" + str(int(x)) + "+" + str(int(y)))

    tutorial_image_window.geometry("260x290")

    tutorial_image_window.title("Image Tutorial")
    if os.path.isfile("icon/PyFlyff.ico"):
        tutorial_image_window.iconbitmap("icon/PyFlyff.ico")
    tutorial_image_window.resizable(False, False)

    image_label = Label(tutorial_image_window)
    image_label.la = PhotoImage(file='help/help.PNG')
    image_label['image'] = image_label.la
    image_label.place(x=0, y=0)
