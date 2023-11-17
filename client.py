import socket
from tkinter import *
import tkinter as tk
from  threading import Thread
import random
from PIL import ImageTk, Image
from tkmacosx import Button
import platform

screen_width = None
screen_height = None
font_size =None

SERVER = None
PORT  = 8080
IP_ADDRESS = '127.0.0.1'
player_name = None

canvas1 = None
canvas2 = None

name_entry = None
name_window = None
gameWindow = None

ticket_grid  = []
current_number_list = []
marked_number_list = []
flash_number_list = []
flash_number_label = None
game_over = False

def place_numbers():
    global ticket_grid
    global current_number_list

    for row in range(0,3):
        random_col_list = []
        counter = 0
        
        while counter<=4:
            random_col = random.randint(0,8)
            if(random_col not in random_col_list):
                random_col_list.append(random_col)
                counter+=1

        number_container = {
        "0": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "1": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        "2": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
        "3": [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
        "4": [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
        "5": [50 , 51, 52, 53, 54, 55, 56, 57, 58, 59],
        "6": [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
        "7": [70, 71, 72, 73, 74, 75, 76, 77, 78, 79],
        "8": [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
        }

        counter = 0
        while (counter < len(random_col_list)):
            col_num = random_col_list[counter]
            numbers_list_by_index = number_container[str(col_num)]
            random_number = random.choice(numbers_list_by_index)

            if(random_number not in current_number_list):
                number_box = ticket_grid[row][col_num]
                number_box.configure(text=random_number, fg="black")
                current_number_list.append(random_number)

                counter+=1


    for row in ticket_grid:
        for number_box in row:
            if(not number_box['text']):
                number_box.configure(state='disabled', background='#ff8a65')

def show_wrong_marking():
    global ticket_grid
    global flash_number_list

    for row in ticket_grid:
        for numberBox in row:
            if(numberBox['text']):
                if(int(numberBox['text']) not in flash_number_list):
                    if(platform.system() == 'Darwin'):
                        numberBox.configure(state='disabled', disabledbackground='#f48fb1',
                            disabledforeground="white")
                    else:
                        numberBox.configure(state='disabled', background='#f48fb1',
                            foreground="white")
                        
def mark_number(button):
    global marked_number_list, flash_number_list, current_number_list, gameOver, flash_number_label, canvas2, player_name, SERVER

    button_text = int(button['text'])
    marked_number_list.append(button_text)
    button.configure(state='disabled',background='#c5e1a5', foreground="black")

    # Check if all items in flash_number_list exits in marked_number_list and set the result in winner variable
    

    # Check if winner is True and sorter current_number_list is equal to marked_number_list
    
        # Store player_name+ 'wins the game' in message variable
        
        # Send the message to SERVER
        
        # Return
        
    
    # Check if length of current_number_list is equal to length of marked_number_list
    
        # Check if all items in flash_number_list exits in marked_number_list and set the result in winner variable
        
        # Check if not winner
        
            # Set gameOver to True
            
            # Set message variable to text 'You Lose the Game'
            
            # Configure flash_number_label from canvas2 and set the text tp message
            
            # Call show_wrong_marking() function
            
    

def create_ticket():
    global gameWindow
    global ticket_grid
    
    xPos = 105
    yPos = 130
    
    for row in range(0, 3):
        row_list = []
        for col in range(0, 9):
            box_button = tk.Button(gameWindow, font = ("Chalkboard SE",30), width=3, height=2,borderwidth=5, bg="#fff176")
            box_button.place(x=xPos, y=yPos)
            
            box_button.configure(command = lambda box_button=box_button :mark_number(box_button))

            row_list.append(box_button)
            xPos += 64
        
        ticket_grid.append(row_list)
        
        xPos = 105
        yPos +=92

def gameWindow():
    global gameWindow
    global canvas2
    global screen_width
    global screen_height
    global flash_number_label
    global image

    gameWindow = Tk()
    gameWindow.title("Tambola Family Fun")

    screen_width = gameWindow.winfo_screenwidth()
    screen_height = gameWindow.winfo_screenheight()
    
    font_size = int(screen_width * 0.03)

    bg = ImageTk.PhotoImage(image)

    canvas2 = Canvas( gameWindow, width = screen_width,height = screen_height)
    canvas2.pack(fill = "both", expand = True)
    canvas2.create_image( 0, 0, image = bg, anchor = "nw")
    canvas2.create_text( screen_width/2,50, text = "Tambola Family Fun", font=("Chalkboard SE",font_size), fill="#3e2723")

    create_ticket()
    place_numbers()

    flash_number_label = canvas2.create_text(screen_width/2,screen_height/1.3, text = "Waiting for other to join...", font=("Chalkboard SE",30), fill="#3e2723")

    gameWindow.resizable(True, True)
    gameWindow.mainloop()

def save_name():
    global SERVER, player_name, name_window, name_entry
    player_name = name_entry.get()
    name_entry.delete(0, END)
    name_window.destroy()

    SERVER.send(player_name.encode())

    gameWindow()

def ask_player_name():
    global player_name, name_entry, name_window, canvas1, font_size, image

    name_window  = Tk()
    name_window.title("Tambola Family Fun")

    screen_width = name_window.winfo_screenwidth()
    screen_height = name_window.winfo_screenheight()
    font_size = int(screen_width * 0.03)
    
    image = Image.open("./assets/background.png")
    image = image.resize((screen_width, screen_height))
    bg = ImageTk.PhotoImage(image)

    canvas1 = Canvas( name_window, width = screen_width, height = screen_height)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text( screen_width/2,screen_height/8, text = "Enter Name", font=("Chalkboard SE",font_size), fill="#3e2723")

    name_entry = Entry(name_window, justify='center', font=('Chalkboard SE', int(font_size/2)), bd=5, bg='white')
    name_entry.place(relx = 0.25, rely=0.3, relwidth = 0.5)

    button = tk.Button(name_window, text="Save", font=("Chalkboard SE", int(font_size/2)),width=11, command=save_name, height=1, bd=3)
    button.place(relx= 0.33, rely=0.5, relwidth = 0.34)

    name_window.resizable(True, True)
    name_window.mainloop()


def receive_msg():
    global SERVER
    global flash_number_label
    global canvas2

    numbers = [ str(i) for i in range(1, 91)]

    while True:
        chunk = SERVER.recv(2048).decode()
        if(chunk in numbers and flash_number_label):
            flash_number_list.append(int(chunk))
            canvas2.itemconfigure(flash_number_label, text = chunk, font = ('Chalkboard SE', 60))
        
def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    thread = Thread(target=receive_msg)
    thread.start()

    ask_player_name()

setup()
