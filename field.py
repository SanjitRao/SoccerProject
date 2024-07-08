import customtkinter as ctk
from tkinter import Canvas

# Initialize the main window
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

app = ctk.CTk()  # Create a CustomTkinter window
app.title("Soccer Field GUI")
app.geometry("800x600")  # Set the size of the window

# Create a canvas widget to draw the soccer field
canvas = Canvas(app, bg="green", width=750, height=500)
canvas.pack(pady=20)

# Draw the outer boundary of the soccer field
field_outline = canvas.create_rectangle(50, 50, 700, 450, outline="white", width=3)

# Draw the center line
center_line = canvas.create_line(375, 50, 375, 450, fill="white", width=3)

# Draw the center circle
center_circle = canvas.create_oval(325, 200, 425, 300, outline="white", width=3)

# Draw the center spot
center_spot = canvas.create_oval(370, 245, 380, 255, fill="white")

# Draw the penalty areas
# Left penalty area
left_penalty_area = canvas.create_rectangle(50, 150, 150, 350, outline="white", width=3)
left_goal_area = canvas.create_rectangle(50, 200, 100, 300, outline="white", width=3)
left_penalty_spot = canvas.create_oval(135, 245, 145, 255, fill="white")

# Right penalty area
right_penalty_area = canvas.create_rectangle(600, 150, 700, 350, outline="white", width=3)
right_goal_area = canvas.create_rectangle(650, 200, 700, 300, outline="white", width=3)
right_penalty_spot = canvas.create_oval(605, 245, 615, 255, fill="white")

# Draw the goals
# Left goal
left_goal = canvas.create_rectangle(45, 225, 50, 275, outline="white", width=3)

# Right goal
right_goal = canvas.create_rectangle(700, 225, 705, 275, outline="white", width=3)

# Draw the corner arcs
# canvas.create_arc(x1, y1, x2, y2, start = from left to right) 
# (x1,x2) is the corner point
# Top left
canvas.create_arc(35, 35, 65, 65, start= 270, extent=90, outline="white", width=3)
# Top right
canvas.create_arc(720, 35, 680, 65, start=180, extent=90, outline="white", width=3)
# Bottom left
canvas.create_arc(35, 435, 65, 465, start=0, extent=90, outline="white", width=3)
# Bottom right
canvas.create_arc(685, 435, 715, 465, start=90, extent=90, outline="white", width=3)

def control_player(player, x, y):
    canvas.coords(player, x-5, y-5, x+5, y+5)

# Draw players
player1 = canvas.create_oval(370, 240, 380, 250, fill="red")
player2 = canvas.create_oval(370, 260, 380, 270, fill="blue")


# Add control buttons for demonstration
def move_player1_up():
    x1, y1, x2, y2 = canvas.coords(player1)
    control_player(player1, (x1 + x2) // 2, (y1 + y2) // 2 - 10)

def move_player1_down():
    x1, y1, x2, y2 = canvas.coords(player1)
    control_player(player1, (x1 + x2) // 2, (y1 + y2) // 2 + 10)

def move_player1_left():
    x1, y1, x2, y2 = canvas.coords(player1)
    control_player(player1, (x1 + x2) // 2 - 10, (y1 + y2) // 2)

def move_player1_right():
    x1, y1, x2, y2 = canvas.coords(player1)
    control_player(player1, (x1 + x2) // 2 + 10, (y1 + y2) // 2)

# Create buttons for controlling player 1
btn_up = ctk.CTkButton(app, text="Up", command=move_player1_up)
btn_up.pack()
btn_down = ctk.CTkButton(app, text="Down", command=move_player1_down)
btn_down.pack()
btn_left = ctk.CTkButton(app, text="Left", command=move_player1_left)
btn_left.pack()
btn_right = ctk.CTkButton(app, text="Right", command=move_player1_right)
btn_right.pack()

# Run the main loop
app.mainloop()
