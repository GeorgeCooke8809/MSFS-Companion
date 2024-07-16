#Imports
from doctest import debug
from tkinter import *
from tkinter.font import BOLD
from SimConnect import *

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

heading_freeze = False
position_freeze = False
altitude_freeze = False
airspeed_freeze = False

on_flight_freeze = False

on_freezes_page = False


def new_capture():
    print("New Capture")

def flight_freeze_on():
    global heading_freeze, position_freeze, altitude_freeze, airspeed_freeze, fuel_freeze, time_freeze, on_flight_freeze, freezes_frame, on_freezes_page

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
    on_flight_freeze = True
    full_frame.pack(anchor=N, fill = BOTH, expand = TRUE)
    print("Flight Freeze", on_flight_freeze)
    
    flight_freeze = Button(freezes_frame,
                                text = "Flight\nFreeze",
                                command = flight_freeze_off,
                                font = (Font_1, 60, BOLD),
                                background = Flight_Freeze_Background,
                                fg = Flight_Freeze_Text,
                                border = 0,
                                cursor = "hand2"
                                )
    flight_freeze.grid(row = 0, column = 0, rowspan = 3, sticky = W+E+N+S, padx = 5, pady = 5)
    if on_freezes_page:
        freezes_frame.pack(fill = BOTH, expand = TRUE)
    
    if heading_freeze == False:
        heading_freeze_on()
    if position_freeze == False:
        position_freeze_on()
    if altitude_freeze == False:
        altitude_freeze_on()
    if airspeed_freeze == False:
        airspeed_freeze_on()
        
def flight_freeze_off():
    global heading_freeze, position_freeze, altitude_freeze, airspeed_freeze, fuel_freeze, time_freeze, on_flight_freeze, freezes_frame, on_freezes_page

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
    on_flight_freeze = False
    full_frame.pack(anchor=N, fill = BOTH, expand = TRUE)
    print("Flight Freeze", on_flight_freeze)
    

    flight_freeze = Button(freezes_frame,
                                text = "Flight\nFreeze",
                                command = flight_freeze_on,
                                font = (Font_1, 60, BOLD),
                                background = Un_Clicked_Background,
                                fg = Un_clicked_Text,
                                border = 0,
                                cursor = "hand2"
                                )
    flight_freeze.grid(row = 0, column = 0, rowspan = 3, sticky = W+E+N+S, padx = 5, pady = 5)
    if on_freezes_page:
        freezes_frame.pack(fill = BOTH, expand = TRUE)
        
    heading_freeze = False
    position_freeze = False
    altitude_freeze = False
    airspeed_freeze = False
    fuel_freeze = False
    time_freeze = False

    heading_freeze_off()
    position_freeze_off()
    altitude_freeze_off()
    airspeed_freeze_off()
    
def heading_freeze_on():
    global heading_freeze, position_freeze, altitude_freeze, airspeed_freeze, fuel_freeze, time_freeze, on_flight_freeze, freezes_frame
    heading_freeze = True

    heading_freeze_button = Button(freezes_frame,
                                   text = "Heading\nFreeze",
                                   command = heading_freeze_off,
                                   font = (Font_1, 30, BOLD),
                                   background = Accent_Background,
                                   fg = Accent_Text,
                                   border = 0,
                                   cursor = "hand2"
                                   )
    heading_freeze_button.grid(row = 0, column = 1, sticky = N+E+S+W, padx = 5, pady = 5)

    if heading_freeze == True and position_freeze == True and altitude_freeze == True and airspeed_freeze == True and fuel_freeze == True and time_freeze == True:
        flight_freeze_on()

    print("Heading Freeze")
    
def heading_freeze_off():
    global heading_freeze, position_freeze, altitude_freeze, airspeed_freeze, fuel_freeze, time_freeze, on_flight_freeze, freezes_frame
    heading_freeze = False

    heading_freeze_button = Button(freezes_frame,
                                   text = "Heading\nFreeze",
                                   command = heading_freeze_on,
                                   font = (Font_1, 30, BOLD),
                                   background = Un_Clicked_Background,
                                   fg = Un_clicked_Text,
                                   border = 0,
                                   cursor = "hand2"
                                   )
    heading_freeze_button.grid(row = 0, column = 1, sticky = N+E+S+W, padx = 5, pady = 5)

    if on_flight_freeze == True:
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
        on_flight_freeze = False
        full_frame.pack(anchor=N, fill = BOTH, expand = TRUE)
        print("Flight Freeze", on_flight_freeze)
    

        flight_freeze = Button(freezes_frame,
                                    text = "Flight\nFreeze",
                                    command = flight_freeze_on,
                                    font = (Font_1, 60, BOLD),
                                    background = Un_Clicked_Background,
                                    fg = Un_clicked_Text,
                                    border = 0,
                                    cursor = "hand2"
                                    )
        flight_freeze.grid(row = 0, column = 0, rowspan = 3, sticky = W+E+N+S, padx = 5, pady = 5)
        if on_freezes_page:
            freezes_frame.pack(fill = BOTH, expand = TRUE)

    print("Heading Freeze")
    
def position_freeze_on():
    global heading_freeze, position_freeze, altitude_freeze, airspeed_freeze, fuel_freeze, time_freeze, on_flight_freeze, freezes_frame
    position_freeze = True
    
    position_freeze_button = Button(freezes_frame,
                                   text = "Position\nFreeze",
                                   command = position_freeze_off,
                                   font = (Font_1, 30, BOLD),
                                   background = Accent_Background,
                                   fg = Accent_Text,
                                   border = 0,
                                   cursor = "hand2"
                                   )
    position_freeze_button.grid(row = 0, column = 2, sticky = N+E+S+W, padx = 5, pady = 5)
    
    if heading_freeze == True and position_freeze == True and altitude_freeze == True and airspeed_freeze == True and fuel_freeze == True and time_freeze == True:
        flight_freeze_on()

    print("Position Freeze")
    
def position_freeze_off():
    global heading_freeze, position_freeze, altitude_freeze, airspeed_freeze, fuel_freeze, time_freeze, on_flight_freeze, freezes_frame
    position_freeze = False
    
    position_freeze_button = Button(freezes_frame,
                                   text = "Position\nFreeze",
                                   command = position_freeze_on,
                                   font = (Font_1, 30, BOLD),
                                   background = Un_Clicked_Background,
                                   fg = Un_clicked_Text,
                                   border = 0,
                                   cursor = "hand2"
                                   )
    position_freeze_button.grid(row = 0, column = 2, sticky = N+E+S+W, padx = 5, pady = 5)
    
    if on_flight_freeze == True:
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
        on_flight_freeze = False
        full_frame.pack(anchor=N, fill = BOTH, expand = TRUE)
        print("Flight Freeze", on_flight_freeze)
    

        flight_freeze = Button(freezes_frame,
                                    text = "Flight\nFreeze",
                                    command = flight_freeze_on,
                                    font = (Font_1, 60, BOLD),
                                    background = Un_Clicked_Background,
                                    fg = Un_clicked_Text,
                                    border = 0,
                                    cursor = "hand2"
                                    )
        flight_freeze.grid(row = 0, column = 0, rowspan = 3, sticky = W+E+N+S, padx = 5, pady = 5)
        if on_freezes_page:
            freezes_frame.pack(fill = BOTH, expand = TRUE)

    print("Position Freeze")
    
def altitude_freeze_on():
    global heading_freeze, position_freeze, altitude_freeze, airspeed_freeze, fuel_freeze, time_freeze, on_flight_freeze, freezes_frame
    altitude_freeze = True
    
    altitude_freeze_button = Button(freezes_frame,
                                   text = "Altitude\nFreeze",
                                   command = altitude_freeze_off,
                                   font = (Font_1, 30, BOLD),
                                   background = Accent_Background,
                                   fg = Accent_Text,
                                   border = 0,
                                   cursor = "hand2"
                                   )
    altitude_freeze_button.grid(row = 1, column = 1, sticky = N+E+S+W, padx = 5, pady = 5)

    if heading_freeze == True and position_freeze == True and altitude_freeze == True and airspeed_freeze == True and fuel_freeze == True and time_freeze == True:
        flight_freeze_on()

    print("Altitude Freeze")
    
def altitude_freeze_off():
    global heading_freeze, position_freeze, altitude_freeze, airspeed_freeze, fuel_freeze, time_freeze, on_flight_freeze, freezes_frame
    altitude_freeze = False
    
    altitude_freeze_button = Button(freezes_frame,
                                   text = "Altitude\nFreeze",
                                   command = altitude_freeze_on,
                                   font = (Font_1, 30, BOLD),
                                   background = Un_Clicked_Background,
                                   fg = Un_clicked_Text,
                                   border = 0,
                                   cursor = "hand2"
                                   )
    altitude_freeze_button.grid(row = 1, column = 1, sticky = N+E+S+W, padx = 5, pady = 5)

    if on_flight_freeze == True:
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
        on_flight_freeze = False
        full_frame.pack(anchor=N, fill = BOTH, expand = TRUE)
        print("Flight Freeze", on_flight_freeze)
    

        flight_freeze = Button(freezes_frame,
                                    text = "Flight\nFreeze",
                                    command = flight_freeze_on,
                                    font = (Font_1, 60, BOLD),
                                    background = Un_Clicked_Background,
                                    fg = Un_clicked_Text,
                                    border = 0,
                                    cursor = "hand2"
                                    )
        flight_freeze.grid(row = 0, column = 0, rowspan = 3, sticky = W+E+N+S, padx = 5, pady = 5)
        if on_freezes_page:
            freezes_frame.pack(fill = BOTH, expand = TRUE)

    print("Altitude Freeze")
    
def airspeed_freeze_on():
    global heading_freeze, position_freeze, altitude_freeze, airspeed_freeze, fuel_freeze, time_freeze, on_flight_freeze, freezes_frame
    airspeed_freeze = True
    
    airspeed_freeze_button = Button(freezes_frame,
                                   text = "Airspeed\nFreeze",
                                   command = airspeed_freeze_off,
                                   font = (Font_1, 30, BOLD),
                                   background = Accent_Background,
                                   fg = Accent_Text,
                                   border = 0,
                                   cursor = "hand2"
                                   )
    airspeed_freeze_button.grid(row = 1, column = 2, sticky = N+E+S+W, padx = 5, pady = 5)

    if heading_freeze == True and position_freeze == True and altitude_freeze == True and airspeed_freeze == True:
        flight_freeze_on()

    print("Airspeed Freeze")
    
def airspeed_freeze_off():
    global heading_freeze, position_freeze, altitude_freeze, airspeed_freeze, fuel_freeze, time_freeze, on_flight_freeze, freezes_frame
    airspeed_freeze = False
    
    airspeed_freeze_button = Button(freezes_frame,
                                   text = "Airspeed\nFreeze",
                                   command = airspeed_freeze_on,
                                   font = (Font_1, 30, BOLD),
                                   background = Un_Clicked_Background,
                                   fg = Un_clicked_Text,
                                   border = 0,
                                   cursor = "hand2"
                                   )
    airspeed_freeze_button.grid(row = 1, column = 2, sticky = N+E+S+W, padx = 5, pady = 5)
    
    if on_flight_freeze == True:
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
        on_flight_freeze = False
        full_frame.pack(anchor=N, fill = BOTH, expand = TRUE)
        print("Flight Freeze", on_flight_freeze)
    

        flight_freeze = Button(freezes_frame,
                                    text = "Flight\nFreeze",
                                    command = flight_freeze_on,
                                    font = (Font_1, 60, BOLD),
                                    background = Un_Clicked_Background,
                                    fg = Un_clicked_Text,
                                    border = 0,
                                    cursor = "hand2"
                                    )
        flight_freeze.grid(row = 0, column = 0, rowspan = 3, sticky = W+E+N+S, padx = 5, pady = 5)
        if on_freezes_page:
            freezes_frame.pack(fill = BOTH, expand = TRUE)

    print("Airspeed Freeze")

def captures_page():
    global on_freezes_page
    
    pages_none()

    captures_page_frame.pack(fill = BOTH, expand = TRUE)

    on_freezes_page = False

    print("Captures Page")

def pages_none():
    global full_frame, button_accent, on_freezes_page

    freezes_menu = Button(full_frame,
                                text = "Flight\nControls",
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
                                text = "Reposition",
                                command = flight_page,
                                font = (Font_1, 30, BOLD),
                                background = Un_Clicked_Background,
                                fg = Un_clicked_Text,
                                border = 0,
                                cursor = "hand2"
                                )
    flight_menu.grid(row = 2, column = 4, sticky = W+E+N+S, padx = 2, pady = 4)

    profile_menu = Button(full_frame,
                                text = "My\nFlights",
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

    freezes_frame.pack_forget()
    on_freezes_page = False
    
    captures_page_frame.pack_forget()

    window_frame.grid(row = 0, column = 0, columnspan = 6)
    full_frame.pack(anchor=N, fill = BOTH, expand = TRUE)
   
def freezes_page():
    global pages_none, button_accent

    pages_none()
    
    button_accent = Frame(full_frame, background = Accent_Background)
    button_accent.grid(row = 1, column = 1, sticky = W+E+N+S)

    freezes_menu = Button(full_frame,
                                text = "Flight\nControls",
                                command = freezes_page,
                                font = (Font_1, 30, BOLD),
                                background = Clicked_Background,
                                fg = Clicked_Text,
                                border = 0,
                                cursor = "hand2"
                                )
    freezes_menu.grid(row = 2, column = 1, sticky = W+E+N+S, padx = 2, pady = 4)
    
    freezes_frame.pack(fill = BOTH, expand = TRUE)
    

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
                                text = "Reposition",
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
                                text = "My\nFlights",
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


freezes_frame = Frame(window_frame, bg = Background)

freezes_frame.columnconfigure(0, weight = 3)
freezes_frame.columnconfigure(1, weight = 5)
freezes_frame.columnconfigure(2, weight = 5)

freezes_frame.rowconfigure(0, weight = 1)
freezes_frame.rowconfigure(1, weight = 1)
freezes_frame.rowconfigure(2, weight = 1)

flight_freeze = Button(freezes_frame,
                            text = "Flight\nFreeze",
                            command = flight_freeze_on,
                            font = (Font_1, 60, BOLD),
                            background = Un_Clicked_Background,
                            fg = Un_clicked_Text,
                            border = 0,
                            cursor = "hand2"
                            )
flight_freeze.grid(row = 0, column = 0, rowspan = 3, sticky = W+E+N+S, padx = 5, pady = 5)

heading_freeze_button = Button(freezes_frame,
                               text = "Heading\nFreeze",
                               command = heading_freeze_on,
                               font = (Font_1, 30, BOLD),
                               background = Un_Clicked_Background,
                               fg = Un_clicked_Text,
                               border = 0,
                               cursor = "hand2"
                               )
heading_freeze_button.grid(row = 0, column = 1, sticky = N+E+S+W, padx = 5, pady = 5)

position_freeze_button = Button(freezes_frame,
                               text = "Position\nFreeze",
                               command = position_freeze_on,
                               font = (Font_1, 30, BOLD),
                               background = Un_Clicked_Background,
                               fg = Un_clicked_Text,
                               border = 0,
                               cursor = "hand2"
                               )
position_freeze_button.grid(row = 0, column = 2, sticky = N+E+S+W, padx = 5, pady = 5)

altitude_freeze_button = Button(freezes_frame,
                               text = "Altitude\nFreeze",
                               command = altitude_freeze_on,
                               font = (Font_1, 30, BOLD),
                               background = Un_Clicked_Background,
                               fg = Un_clicked_Text,
                               border = 0,
                               cursor = "hand2"
                               )
altitude_freeze_button.grid(row = 1, column = 1, sticky = N+E+S+W, padx = 5, pady = 5)

airspeed_freeze_button = Button(freezes_frame,
                               text = "Airspeed\nFreeze",
                               command = airspeed_freeze_on,
                               font = (Font_1, 30, BOLD),
                               background = Un_Clicked_Background,
                               fg = Un_clicked_Text,
                               border = 0,
                               cursor = "hand2"
                               )
airspeed_freeze_button.grid(row = 1, column = 2, sticky = N+E+S+W, padx = 5, pady = 5)

captures_page_button = Button(freezes_frame,
                               text = "Captures",
                               command = captures_page,
                               font = (Font_1, 30, BOLD),
                               background = Un_Clicked_Background,
                               fg = Un_clicked_Text,
                               border = 0,
                               cursor = "hand2"
                               )
captures_page_button.grid(row = 2, column = 1,columnspan = 2, sticky = N+E+S+W, padx = 5, pady = 5)



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
                            text = "Flight\nControls",
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
                            text = "Reposition",
                            command = flight_page,
                            font = (Font_1, 30, BOLD),
                            background = Un_Clicked_Background,
                            fg = Un_clicked_Text,
                            border = 0,
                            cursor = "hand2"
                            )
flight_menu.grid(row = 2, column = 4, sticky = W+E+N+S, padx = 2, pady = 4)

profile_menu = Button(full_frame,
                            text = "My\nFlights",
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

captures_page_frame = Frame(window_frame, background = Background)

captures_page_frame.rowconfigure(0)
captures_page_frame.rowconfigure(1)
captures_page_frame.rowconfigure(2)
captures_page_frame.rowconfigure(3)
captures_page_frame.rowconfigure(4)
captures_page_frame.rowconfigure(5)
captures_page_frame.rowconfigure(6)
captures_page_frame.rowconfigure(7)
captures_page_frame.rowconfigure(8)
captures_page_frame.rowconfigure(9)

captures_page_frame.columnconfigure(0, weight = 2)
captures_page_frame.columnconfigure(1, weight = 3)
captures_page_frame.columnconfigure(2, weight = 3)

captures_back_button = Button(captures_page_frame,
                            text = "Back",
                            command = freezes_page,
                            font = (Font_1, 30, BOLD),
                            background = Un_Clicked_Background,
                            fg = Un_clicked_Text,
                            border = 0,
                            cursor = "hand2"
                            )
captures_back_button.grid(row = 0, column = 0, sticky = W+E+N+S, padx = 2, pady = 4)

new_capture_button = Button(captures_page_frame,
                            text = "New Capture",
                            command = new_capture,
                            font = (Font_1, 30, BOLD),
                            background = Un_Clicked_Background,
                            fg = Un_clicked_Text,
                            border = 0,
                            cursor = "hand2"
                            )
new_capture_button.grid(row = 1, rowspan = 9, column = 0, sticky = W+E+N+S, padx = 2, pady = 4)


root.mainloop()