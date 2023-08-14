# Name: Aryan Aggarwal
# Description: This is a math fighting game. In this game, the user can select
#              an opponent, which determines the level, and launch attacks
#              at the opponent. The user can launch an attack if they answer a
#              math question correctly.

# Imports necessary libraries
from tkinter import *
from tkinter import ttk
import random

# Function to handle start button click and prepares level selection
def start_game():
    global player_health, opponent_health
    canvas.delete("all")  # Clear the canvas
    
    # Create level selection buttons
    level_1_button = Button(window, \
                            image=level_1_image, \
                            width=256, height=568, \
                            bg='black', \
                            command=lambda: \
                            select_level(1, opponent_image=obito_character))
    level_2_button = Button(window, \
                            image=level_2_image, \
                            width=256, height=568,\
                            bg='black', command=lambda:\
                            select_level(2, opponent_image=itachi_character))
    level_3_button = Button(window, \
                            image=level_3_image,\
                            width=256, height=568, \
                            bg='black', command=lambda:\
                            select_level(3, opponent_image=madara_character))
    level_4_button = Button(window, \
                            image=level_4_image, \
                            width=256, height=568, bg='black',\
                            command=lambda:\
                            select_level(4, opponent_image=sasuke_character))
    
    # Add level selection buttons to the canvas
    canvas.create_window(0, 0, anchor='nw', window=level_1_button)
    canvas.create_window(256, 0, anchor='nw', window=level_2_button)
    canvas.create_window(512, 0, anchor='nw', window=level_3_button)
    canvas.create_window(768, 0, anchor='nw', window=level_4_button)
    canvas.create_image(0, 568, anchor='nw', image=choose_opponent_image)
    
    # Defines starting health for the player and opponent
    player_health = 100
    opponent_health = 100

# Function to handle level selection and begin the attack screen
def select_level(level, opponent_image):
    global attack_image, fireball, heavy_attack_answer_state
    # Clear the canvas
    canvas.delete("all")
    
    # Set the image background
    canvas.create_image(0, 0, image=attack_background, anchor="nw")
    
    # Create health bars for user and opponent
    opponent_health_bar = ttk.Progressbar(window, length=300, \
                                          mode="determinate", \
                                          value=opponent_health, \
                                          style="green.Horizontal.TProgressbar")

    # Add opponent health bar to the canvas
    canvas.create_window(700, 20, anchor='nw', window=opponent_health_bar)
    
    # Create the attack button
    heavy_attack_button = Button(window, \
                                 image=rasenshuriken_image, \
                                 width=700, height=108, \
                                 bg='black', command=lambda: \
                                 launch_attack(level))
    # Create the surrender button
    surrender_button = Button(window,\
                              image=surrender_image,
                              width=239, height=108, bg='orange', \
                              command=surrender)
    
    # Add attack buttons to the canvas
    canvas.create_window(38, 615, anchor='nw', window=heavy_attack_button)
    canvas.create_window(743, 615, anchor='nw', window=surrender_button)
    
    # Add user character to the canvas
    canvas.create_image(0,125, anchor='nw', image=naruto_character)
    
    # Add opponent character to the canvas
    canvas.create_image(700, 125, anchor='nw', image=opponent_image)
    
    # Check if the user can attack, then play the attack
    if heavy_attack_answer_state:
        
        # Create the attack image
        attack_image = canvas.create_image(100, 150, \
                                           image=heavy_attack_animation_image,\
                                           anchor='nw')
    
        # Animate the attack's movement
        animate_attack()
        heavy_attack_answer_state = False
    
    opponent_attack(level)
    # Check if the opponent can attack, then play attack
    if opponent_hit_is_true:
        # Create the fireball
        fireball = canvas.create_image(700, 150, \
                                       image=fireball_image, anchor='nw')
        
        # Animate the fireballs movement
        opponent_animate_attack()

    # Add user health bar to the canvas
    user_health_bar = ttk.Progressbar(window, \
                                      length=300, \
                                      mode="determinate", \
                                      value=player_health,\
                                      style="green.Horizontal.TProgressbar")
    canvas.create_window(20, 20, anchor='nw', window=user_health_bar)
    
    # Show win screen if the user wins
    if opponent_health <= 0:
        win_screen()
    
    # Show lose screen if the user loses
    if player_health <= 0:
        lose_screen()
        

# Function to handle attack selection
def launch_attack(level):
    global answer_entry
    canvas.delete("all")  # Clear the canvas
    canvas.create_image(0, 0, image=question_background, anchor="nw")
    canvas.create_image(50,20, image=math_title, anchor="nw")
    
    # Display an equal sign for the math question
    canvas.create_image(475,175, image=equal_sign_image, anchor="nw")

    # Generate a math question based on the selected level
    question = generate_math_question(level)

    # Display the math question on the canvas
    canvas.create_text(250, 220, text=question, font=("Arial", 69),\
                       fill="black")
    
    # Display text for counters 
    canvas.create_text(200, 500, text='Successful attacks: ',
                       font=("Arial", 20), fill = "black")
    canvas.create_text(170, 550, text='Missed attacks: ', font=("Arial", 20), \
                       fill = "black")
    canvas.create_text(150, 600, text='Total attacks: ', font=("Arial", 20), \
                       fill = "black")
    
    # Display the counters on the canvas
    canvas.create_text(385, 500, text=successful_attacks, font=("Arial", 20), \
                       fill = "black")
    canvas.create_text(385, 550, text=missed_attacks, font=("Arial", 20),\
                       fill = "black")
    canvas.create_text(385, 600, text=total_attacks, font=("Arial", 20), \
                       fill = "black")

    # Create an entry field for the user to input the answer
    answer_entry = Entry(window, font=("Arial", 48), width=3)
    answer_window = canvas.create_window(600, 175, anchor='nw', \
                                         window=answer_entry)
    answer_entry.focus()

    # Create a submit button
    submit_button = Button(window, \
                           image=button_images[7],\
                           bd=0, command=lambda: \
                           check_answer(question, answer_entry.get(), level))
    submit_window = canvas.create_window(775, 175, \
                                         anchor='nw', window=submit_button)
    window.bind('<Return>', lambda event: \
                check_answer(question, answer_entry.get(), level))

    # Create numberpad for math input
    buttons = [
        ("1", 0, 0),
        ("2", 1, 0),
        ("3", 2, 0),
        ("Backspace", 3, 0),
        ("4", 0, 1),
        ("5", 1, 1),
        ("6", 2, 1),
        ("Enter", 3, 1),
        ("7", 0, 2),
        ("8", 1, 2),
        ("9", 2, 2),
        ("0", 3, 2)
    ]
    
    for i, (label, col, row) in enumerate(buttons):
        if label == "Backspace":
            button = Button(window,\
                            image=button_images[3], \
                            width=100, height=100,\
                            command=lambda: \
                            answer_entry.delete(len(answer_entry.get()) - 1))
        elif label == "Enter":
            button = Button(window,\
                            image=button_images[7], \
                            bd=0, command=lambda: \
                            check_answer(question, answer_entry.get(), level))
        else:
            button = Button(window,\
                            image=button_images[i], \
                            width=100, height=100,\
                            command=lambda num=i: numberpad_clicked(num))
            
        button_window = canvas.create_window(475 + col * 100,\
                                             375 + row * 100, anchor='nw',\
                                             window=button)


# Function to handle number pad click
def numberpad_clicked(i):
    if i < 3:
        answer_entry.insert(END, str(i + 1))
    elif i == 3:  # Backspace
        answer_entry.delete(len(answer_entry.get()) - 1)
    elif i == 4:  # 4
        answer_entry.insert(END, "4")
    elif i == 5:  # 5
        answer_entry.insert(END, "5")
    elif i == 6:  # 6
        answer_entry.insert(END, "6")
    elif i == 7:  # Enter
        check_answer(question, answer_entry.get())
    elif i == 11:  # 0
        answer_entry.insert(END, "0")
    elif i > 7:
        answer_entry.insert(END, str(i - 1))

    
    
# Function to generate a math question based on the selected level and attack
# type
def generate_math_question(level):
    if level == 1:
        num_range = range(1, 4)
    elif level == 2:
        num_range = range(1, 7)
    elif level == 3:
        num_range = range(1, 10)
    elif level == 4:
        num_range = range(1, 13)

    num1 = random.choice(num_range)
    num2 = random.choice(num_range)

    
    operator = random.choice(["+", "-", chr(215), chr(247)])

    if operator == chr(247):
        # Generate a divisor that ensures the answer is within the range
        divisor_range = range(1, max(num_range))
        divisor = random.choice(divisor_range)

        # Calculate the dividend by multiplying the divisor and the quotient
        dividend = num2 * divisor

        question = f"{dividend} {operator} {divisor}"
    else:
        question = f"{num1} {operator} {num2}"
    
    return question

# Function to check the users answer and send them back to the attack screen
def check_answer(question, answer, level):
    global heavy_attack_answer_state, total_attacks, successful_attacks
    global missed_attacks
    try:
        question = question.replace(chr(247),"/")
        question = question.replace(chr(215),"*")
        # Evaluate the correct answer to the math question
        correct_answer = str(eval(question))
        total_attacks += 1

        if float(answer) == float(correct_answer):
            # Perform actions when the answer is correct
            heavy_attack_answer_state = True
            successful_attacks += 1
            
            # Decrease opponent's health by 20
            global opponent_health
            opponent_health -= 20
        else:
            heavy_attack_answer_state = False
            missed_attacks += 1
            

        # Go back to the attack screen
        if level == 1:
            opponent_image = obito_character
        elif level == 2:
            opponent_image = itachi_character
        elif level == 3:
            opponent_image = madara_character
        elif level == 4:
            opponent_image = sasuke_character
        
        # Pass the appropriate level and opponent image
        select_level(level, opponent_image)  
        # Clear the answer entry field
        answer_entry.delete(0, END)

    except:
       # Clear the answer entry field
        answer_entry.delete(0, END) 

# Function to handle surrender button click
def surrender():
    # Define starting counters for user
    global successful_attacks, missed_attacks, total_attacks
    successful_attacks = 0
    missed_attacks = 0
    total_attacks = 0
    start_game()

# Function to handle rules button
def rules():
    canvas.delete("all")  # Clear the canvas
    canvas.create_image(0, 0, image=rules_background, anchor="nw")
    rtrn_to_strt_scrn_btn = Button(window, \
                                           image=return_to_start_screen_image,\
                                           width=293, height=111,\
                                           command=start_game)
    rtrn_to_strt_scrn_wndw = canvas.create_window(700,\
                                                  30,
                                                  anchor='nw',\
                                                  window=rtrn_to_strt_scrn_btn)
    
# Function to make attacks move
def animate_attack():
    try:
        # Move the attack image horizontally
        canvas.move(attack_image, 10, 0)
        
        # Get the current position of the attack image
        x, _ = canvas.coords(attack_image)
        
        # Check if the attack has reached the desired x coordinate
        if x < 750:
            # Schedule the next movement after a certain delay
            canvas.after(15, animate_attack)
        else:
            canvas.delete(attack_image)
    except:
        pass

# Function to handle the animation for opponent attacks
def opponent_animate_attack():
    try:
        # Move the fireball
        canvas.move(fireball, -10, 0)  # Move 10 pixels to the left

        # Schedule the next animation frame
        if canvas.coords(fireball)[0] > 120:
            window.after(15, opponent_animate_attack) 
        else:
            canvas.delete(fireball)
    except:
        pass

    
# Function to handle opponent attacks
def opponent_attack(level):
    global opponent_hit_is_true

    # Set probability for the opponent to hit the user
    lvl_1_hit_probability = 50
    lvl_2_hit_probability = 60
    lvl_3_hit_probability = 70
    lvl_4_hit_probability = 80
    
    if level == 1:
        hit_probability = lvl_1_hit_probability
    elif level == 2:
        hit_probability = lvl_2_hit_probability
    elif level == 3:
        hit_probability = lvl_3_hit_probability
    elif level == 4:
        hit_probability = lvl_4_hit_probability
    
    # Logic to decide if opponent hits user
    hit_number = random.randint(0,100)
    hit_number = int(hit_number)
    if hit_number <= hit_probability:
        opponent_hit_is_true = True
        global player_health
        player_health -= 20
    else:
        opponent_hit_is_true = False

# Function to generate the win screen
def win_screen():
    canvas.delete("all")
    # Define starting counters for user
    global successful_attacks, missed_attacks, total_attacks
    successful_attacks = 0
    missed_attacks = 0
    total_attacks = 0
    canvas.create_image(0, 0, image=win_background, anchor="nw")
    rtrn_to_strt_scrn_btn = Button(window,\
                                           image=return_to_start_screen_image, \
                                           width=293, height=111, \
                                           command=start_game)
    rtrn_to_strt_scrn_wndw = canvas.create_window(165,\
                                                  400,\
                                                  anchor='nw', \
                                                  window=rtrn_to_strt_scrn_btn)

# Function to generate the lose screen
def lose_screen():
    canvas.delete("all")
    # Define starting counters for user
    global successful_attacks, missed_attacks, total_attacks
    successful_attacks = 0
    missed_attacks = 0
    total_attacks = 0
    canvas.create_image(0, 0, image=lose_background, anchor="nw")
    rtrn_to_strt_scrn_btn = Button(window,\
                                   image=return_to_start_screen_image, \
                                   width=293, height=111, command=start_game)
    rtrn_to_strt_scrn_wndw = canvas.create_window(565,250,\
                                                  anchor='nw', \
                                                  window=rtrn_to_strt_scrn_btn)



# Create a window and set the dimensions
window = Tk()
window.title("Math Game")
window.geometry("1024x768")  # Set the dimensions of the window
window.resizable(False, False)

# Create a style for the progress bars
style = ttk.Style()
style.theme_use('clam')
style.configure("blue.Horizontal.TProgressbar", foreground='blue', \
                background='blue')
style.configure("green.Horizontal.TProgressbar", foreground='green', \
                background='green')

# Define start screen images
start_background = PhotoImage(file='start_background.png')
title = PhotoImage(file='title.png')
begin_training_image = PhotoImage(file='begin_training.png')

# Define rules background image
rules_background = PhotoImage(file='rules_background.png')
return_to_start_screen_image = PhotoImage(file='return_to_start_screen.png')

# Define level selection screen images
level_1_image = PhotoImage(file='obito.png')
level_2_image = PhotoImage(file='itachi.png')
level_3_image = PhotoImage(file='madara.png')
level_4_image = PhotoImage(file='sasuke.png')
choose_opponent_image = PhotoImage(file='choose_your_opponent.png')

# Define attack screen images
attack_background = PhotoImage(file='attack_background.png')
rasenshuriken_image = PhotoImage(file='attack_button.png')
surrender_image = PhotoImage(file='surrender.png')

# Define character images
naruto_character = PhotoImage(file='naruto.png')
obito_character = PhotoImage(file='obito_character.png')
itachi_character = PhotoImage(file='itachi_character.png')
madara_character = PhotoImage(file='madara_character.png')
sasuke_character = PhotoImage(file='sasuke_character.png')

# Defines starting health for the player and opponent
player_health = 100
opponent_health = 100

# Define starting counters for user
successful_attacks = 0
missed_attacks = 0
total_attacks = 0

# Define attack images
attack_image = None
heavy_attack_animation_image = PhotoImage(file='rasenshuriken_new.png')
fireball_image = PhotoImage(file='fireball.png')

# Sets default answer state to false
heavy_attack_answer_state = False

# Define numberpad button images
button_images = [
    PhotoImage(file="button_1.png"),
    PhotoImage(file="button_2.png"),
    PhotoImage(file="button_3.png"),
    PhotoImage(file="button_backspace.png"),
    PhotoImage(file="button_4.png"),
    PhotoImage(file="button_5.png"),
    PhotoImage(file="button_6.png"),
    PhotoImage(file="button_enter.png"),
    PhotoImage(file="button_7.png"),
    PhotoImage(file="button_8.png"),
    PhotoImage(file="button_9.png"),
    PhotoImage(file="button_0.png")
]

# Define math screen background image
question_background = PhotoImage(file='question_background.png')

# Define math screen title
math_title = PhotoImage(file='answer_the_following_math_question.png')

# Define operators images
equal_sign_image = PhotoImage(file='equal_sign.png')

# Create a canvas
canvas = Canvas(window, width=1024, height=768)
canvas.pack(fill='both', expand=True)

# Set background in canvas
canvas.create_image(0, 0, image=start_background, anchor="nw")

# Add title to canvas
canvas.create_image(0, 50, image=title, anchor='nw')

# Add start button
begin_training_button = Button(window, image=begin_training_image, width=400, \
                               height=100, bg='orange', command=start_game)
begin_training_window = canvas.create_window(340, 200, anchor='nw',\
                                             window=begin_training_button)

# Set win and lose background
win_background = PhotoImage(file='win_background.png')
lose_background = PhotoImage(file='lose_background.png')

# Add rules button
rules_button = Button(window, text='Rules',font=("Arial", 24), \
                      width=14, height=1, bg='blue', command=rules)
rules_window = canvas.create_window(340,350, anchor='nw', window=rules_button)

# Keeps the window open
window.mainloop()




