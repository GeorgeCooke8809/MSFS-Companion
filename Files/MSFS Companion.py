#Imports
from os import uname_result
from tkinter import *
from tkinter.font import BOLD
from turtle import position, width

#Set Version Number
Version = "0.1.0"


#Set fonts as variables for later use
Font_1 = "Monoton"
Font_2 = "Tw Cen MT"

#Set colours to variables for later customisation
Background = "#353535"
Un_Clicked_Background = "#EFEFEF"
Un_clicked_Text ="Black"
Clicked_Background = "#434343"
Clicked_Text = "White"

Flight_Freeze_Background = "#980000"
Flight_Freeze_Text = "White"
Flight_Freeze_Clicked_Background = "#ff5e5e"
Flight_Freeze_Clicked_Foreground = "Black"

Accent_Background = "#1155CC"
Accent_Text = "White"

headding_freeze = False
position_freeze = False
altitude_freeze = False
airspeed_freeze = False
fuel_freeze = False
time_freeze = False

flight_freeze = False


def flight_freeze_on():
    global headding_freeze, position_freeze, altitude_freeze, airspeed_freeze, fuel_freeze, time_freeze, flight_freeze

    flight_freeze_menu = Button(full_frame,
                            text = "Flight Freeze",
                            command = flight_freeze_off,
                            font = (Font_1, 30, BOLD),
                            background = Flight_Freeze_Background,
                            fg = Flight_Freeze_Text,
                            border = 0,
                            cursor = "hand2"
                            )
    flight_freeze_menu.grid(row = 2, column = 0, sticky = W+E+N+S, padx = 2, pady = 4)
    flight_freeze = True
    full_frame.pack(anchor=N, fill = BOTH, expand = TRUE)
    print("Flight Freeze", flight_freeze)
        
def flight_freeze_off():
    flight_freeze_menu = Button(full_frame,
                            text = "Flight Freeze",
                            command = flight_freeze_on,
                            font = (Font_1, 30, BOLD),
                            background = Un_Clicked_Background,
                            fg = Un_clicked_Text,
                            border = 0,
                            cursor = "hand2"
                            )
    flight_freeze_menu.grid(row = 2, column = 0, sticky = W+E+N+S, padx = 2, pady = 4)
    flight_freeze = False
    full_frame.pack(anchor=N, fill = BOTH, expand = TRUE)
    print("Flight Freeze", flight_freeze)

def pages_none():
    global full_frame, button_accent

    freezes_menu = Button(full_frame,
                                text = "Freezes",
                                command = freezes_page,
                                font = (Font_1, 30, BOLD),
                                background = Un_Clicked_Background,
                                fg = Un_clicked_Text,
                                border = 0,
                                cursor = "hand2"
                                )
    freezes_menu.grid(row = 2, column = 1, sticky = W+E+N+S, padx = 2, pady = 4)

    failures_menu = Button(full_frame,
                                text = "Failures",
                                command = failures_page,
                                font = (Font_1, 30, BOLD),
                                background = Un_Clicked_Background,
                                fg = Un_clicked_Text,
                                border = 0,
                                cursor = "hand2"
                                )
    failures_menu.grid(row = 2, column = 2, sticky = W+E+N+S, padx = 2, pady = 4)

    map_menu = Button(full_frame,
                                text = "Map",
                                command = map_page,
                                font = (Font_1, 30, BOLD),
                                background = Un_Clicked_Background,
                                fg = Un_clicked_Text,
                                border = 0,
                                cursor = "hand2"
                                )
    map_menu.grid(row = 2, column = 3, sticky = W+E+N+S, padx = 2, pady = 4)

    flight_menu = Button(full_frame,
                                text = "Flight",
                                command = flight_page,
                                font = (Font_1, 30, BOLD),
                                background = Un_Clicked_Background,
                                fg = Un_clicked_Text,
                                border = 0,
                                cursor = "hand2"
                                )
    flight_menu.grid(row = 2, column = 4, sticky = W+E+N+S, padx = 2, pady = 4)

    profile_menu = Button(full_frame,
                                text = "Profile",
                                command = profile_page,
                                font = (Font_1, 30, BOLD),
                                background = Un_Clicked_Background,
                                fg = Un_clicked_Text,
                                border = 0,
                                cursor = "hand2"
                                )
    profile_menu.grid(row = 2, column = 5, sticky = W+E+N+S, padx = 2, pady = 4)

    button_accent = Frame(full_frame, background = Background)
    button_accent.grid(row = 1, column = 0, columnspan = 6, sticky = W+E+N+S)

    window_frame.grid(row = 0, column = 0, columnspan = 6)
    full_frame.pack(anchor=N, fill = BOTH, expand = TRUE)
   
def freezes_page():
    global pages_none, button_accent

    pages_none()
    
    button_accent = Frame(full_frame, background = Accent_Background)
    button_accent.grid(row = 1, column = 1, sticky = W+E+N+S)

    freezes_menu = Button(full_frame,
                                text = "Freezes",
                                command = freezes_page,
                                font = (Font_1, 30, BOLD),
                                background = Clicked_Background,
                                fg = Clicked_Text,
                                border = 0,
                                cursor = "hand2"
                                )
    freezes_menu.grid(row = 2, column = 1, sticky = W+E+N+S, padx = 2, pady = 4)
    print("Freezes Page")
    
def failures_page():
    global pages_none
    
    pages_none()
    
    button_accent = Frame(full_frame, background = Accent_Background)
    button_accent.grid(row = 1, column = 2, sticky = W+E+N+S)

    failures_menu = Button(full_frame,
                                text = "Failures",
                                command = failures_page,
                                font = (Font_1, 30, BOLD),
                                background = Clicked_Background,
                                fg = Clicked_Text,
                                border = 0,
                                cursor = "hand2"
                                )
    failures_menu.grid(row = 2, column = 2, sticky = W+E+N+S, padx = 2, pady = 4)

    print("Failures Page")

def map_page():
    global pages_none
    
    pages_none()

    button_accent = Frame(full_frame, background = Accent_Background)
    button_accent.grid(row = 1, column = 3, sticky = W+E+N+S)

    map_menu = Button(full_frame,
                                text = "Map",
                                command = map_page,
                                font = (Font_1, 30, BOLD),
                                background = Clicked_Background,
                                fg = Clicked_Text,
                                border = 0,
                                cursor = "hand2"
                                )
    map_menu.grid(row = 2, column = 3, sticky = W+E+N+S, padx = 2, pady = 4)

    print("Map Page")
    
def flight_page():
    global pages_none
    
    pages_none()
    
    button_accent = Frame(full_frame, background = Accent_Background)
    button_accent.grid(row = 1, column = 4, sticky = W+E+N+S)

    flight_menu = Button(full_frame,
                                text = "Flight",
                                command = flight_page,
                                font = (Font_1, 30, BOLD),
                                background = Clicked_Background,
                                fg = Clicked_Text,
                                border = 0,
                                cursor = "hand2"
                                )
    flight_menu.grid(row = 2, column = 4, sticky = W+E+N+S, padx = 2, pady = 4)

    print("Flight Page")
    
def profile_page():
    global pages_none
    
    pages_none()

    button_accent = Frame(full_frame, background = Accent_Background)
    button_accent.grid(row = 1, column = 5, sticky = W+E+N+S)

    profile_menu = Button(full_frame,
                                text = "Profile",
                                command = profile_page,
                                font = (Font_1, 30, BOLD),
                                background = Clicked_Background,
                                fg = Clicked_Text,
                                border = 0,
                                cursor = "hand2"
                                )
    profile_menu.grid(row = 2, column = 5, sticky = W+E+N+S, padx = 2, pady = 4)

    print("Profile Page")

#Make window
root = Tk()
root.geometry("500x500")
root.state("zoomed")

root.config(bg = Background)
root.title("MSFS Companion - Version " + Version)

#Make main window frame
full_frame = Frame(root, bg = "Black")

full_frame.columnconfigure(0, weight = 3)
full_frame.columnconfigure(1, weight = 2)
full_frame.columnconfigure(2, weight = 2)
full_frame.columnconfigure(3, weight = 2)
full_frame.columnconfigure(4, weight = 2)
full_frame.columnconfigure(5, weight = 2)

full_frame.rowconfigure(0, weight = 80)
full_frame.rowconfigure(1, weight = 1, minsize = 5)
full_frame.rowconfigure(2, weight = 5)

window_frame = Frame(full_frame, bg = Background)

flight_freeze_menu = Button(full_frame,
                            text = "Flight Freeze",
                            command = flight_freeze_on,
                            font = (Font_1, 30, BOLD),
                            background = Un_Clicked_Background,
                            fg = Un_clicked_Text,
                            border = 0,
                            cursor = "hand2"
                            )
flight_freeze_menu.grid(row = 2, column = 0, sticky = W+E+N+S, padx = 2, pady = 4)

freezes_menu = Button(full_frame,
                            text = "Freezes",
                            command = freezes_page,
                            font = (Font_1, 30, BOLD),
                            background = Un_Clicked_Background,
                            fg = Un_clicked_Text,
                            border = 0,
                            cursor = "hand2"
                            )
freezes_menu.grid(row = 2, column = 1, sticky = W+E+N+S, padx = 2, pady = 4)

failures_menu = Button(full_frame,
                            text = "Failures",
                            command = failures_page,
                            font = (Font_1, 30, BOLD),
                            background = Un_Clicked_Background,
                            fg = Un_clicked_Text,
                            border = 0,
                            cursor = "hand2"
                            )
failures_menu.grid(row = 2, column = 2, sticky = W+E+N+S, padx = 2, pady = 4)

map_menu = Button(full_frame,
                            text = "Map",
                            command = map_page,
                            font = (Font_1, 30, BOLD),
                            background = Un_Clicked_Background,
                            fg = Un_clicked_Text,
                            border = 0,
                            cursor = "hand2"
                            )
map_menu.grid(row = 2, column = 3, sticky = W+E+N+S, padx = 2, pady = 4)

flight_menu = Button(full_frame,
                            text = "Flight",
                            command = flight_page,
                            font = (Font_1, 30, BOLD),
                            background = Un_Clicked_Background,
                            fg = Un_clicked_Text,
                            border = 0,
                            cursor = "hand2"
                            )
flight_menu.grid(row = 2, column = 4, sticky = W+E+N+S, padx = 2, pady = 4)

profile_menu = Button(full_frame,
                            text = "Profile",
                            command = profile_page,
                            font = (Font_1, 30, BOLD),
                            background = Un_Clicked_Background,
                            fg = Un_clicked_Text,
                            border = 0,
                            cursor = "hand2"
                            )
profile_menu.grid(row = 2, column = 5, sticky = W+E+N+S, padx = 2, pady = 4)

button_accent = Frame(full_frame, background = Background)
button_accent.grid(row = 1, column = 0, columnspan = 6, sticky = W+E+N+S)

window_frame.grid(row = 0, column = 0, columnspan = 6, sticky = N+E+S+W)
full_frame.pack(anchor=N, fill = BOTH, expand = TRUE)

root.mainloop()