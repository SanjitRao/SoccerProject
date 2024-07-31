import customtkinter
from tkinter import Canvas


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
        customtkinter.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

        self.title("Soccer Field GUI")
        self.geometry("800x600")

        # Create a canvas widget to draw the soccer field
        self.canvas = Canvas(self, bg="green", width=750, height=500)
        self.canvas.pack(pady=20)

        # Draw the outer boundary of the soccer field
        field_outline = self.canvas.create_rectangle(50, 50, 700, 450, outline="white", width=3)
        # Draw the center line
        center_line = self.canvas.create_line(375, 50, 375, 450, fill="white", width=3)

        # Draw the center circle
        center_circle = self.canvas.create_oval(325, 200, 425, 300, outline="white", width=3)

        # Draw the center spot
        center_spot = self.canvas.create_oval(370, 245, 380, 255, fill="white")

        # Draw the penalty areas
        # Left penalty area
        left_penalty_area = self.canvas.create_rectangle(50, 150, 150, 350, outline="white", width=3)
        left_goal_area = self.canvas.create_rectangle(50, 200, 100, 300, outline="white", width=3)
        left_penalty_spot = self.canvas.create_oval(135, 245, 145, 255, fill="white")

        # Right penalty area
        right_penalty_area = self.canvas.create_rectangle(600, 150, 700, 350, outline="white", width=3)
        right_goal_area = self.canvas.create_rectangle(650, 200, 700, 300, outline="white", width=3)
        right_penalty_spot = self.canvas.create_oval(605, 245, 615, 255, fill="white")

        # Draw the goals
        # Left goal
        left_goal = self.canvas.create_rectangle(45, 225, 50, 275, outline="white", width=3)

        # Right goal
        right_goal = self.canvas.create_rectangle(700, 225, 705, 275, outline="white", width=3)

        # Draw the corner arcs
        # canvas.create_arc(x1, y1, x2, y2, start = from left to right) 
        # (x1,x2) is the corner point
        # Top left
        self.canvas.create_arc(35, 35, 65, 65, start= 270, extent=90, outline="white", width=3)
        # Top right
        self.canvas.create_arc(720, 35, 680, 65, start=180, extent=90, outline="white", width=3)
        # Bottom left
        self.canvas.create_arc(35, 435, 65, 465, start=0, extent=90, outline="white", width=3)
        # Bottom right
        self.canvas.create_arc(685, 435, 715, 465, start=90, extent=90, outline="white", width=3)

        #========================================================================================================


        self.red = self.init_team("red", 0, "433")
        self.blue = self.init_team("blue", 1, "433")
        self.designated_player = self.blue[8] # player starts as a striker

        self.BALL = self.canvas.create_oval(370, 245, 380, 255, fill="white")
        self.DX = 0
        self.DY = 0
        self.has_ball = False
        self.num_gamestates = 0


        # Create buttons for controlling player 1
        btn_player1_up = customtkinter.CTkButton(self, text="Player 1 Up", command=self.move_player1_up)
        btn_player1_up.pack()
        btn_player1_down = customtkinter.CTkButton(self, text="Player 1 Down", command=self.move_player1_down)
        btn_player1_down.pack()
        btn_player1_left = customtkinter.CTkButton(self, text="Player 1 Left", command=self.move_player1_left)
        btn_player1_left.pack()
        btn_player1_right = customtkinter.CTkButton(self, text="Player 1 Right", command=self.move_player1_right)
        btn_player1_right.pack()

        btn_player_pass = customtkinter.CTkButton(self, text="Pass", command = self.PASS_BALL)
        btn_player_pass.pack()

        self.des_player_entry = customtkinter.CTkEntry(self, placeholder_text="Enter Designated Player")
        self.des_player_entry.pack()
        submit = customtkinter.CTkButton(self, text="Submit", command=self.select_des_player)
        submit.pack()

    def select_des_player(self):
        pos_players = ["LB", "LCD", "RCD", "RB", "LMF", "CMF", "RMF", "LW", "ST", "RW", "GK"]
        inits= self.des_player_entry.get()
        print(self.des_player_entry.get())

        if inits not in pos_players:
            return

        if inits == "LB":
            self.designated_player = self.blue[0]
        if inits == "LCD":
            self.designated_player = self.blue[1]
        if inits == "RDC":
            self.designated_player = self.blue[2]
        if inits == "RB":
            self.designated_player = self.blue[3]
        if inits == "LMF":
            self.designated_player = self.blue[4]
        if inits == "CMF":
            self.designated_player = self.blue[5]
        if inits == "RMF":
            self.designated_player = self.blue[6]
        if inits == "LW":
            self.designated_player = self.blue[7]
        if inits == "ST":
            self.designated_player = self.blue[8]
        if inits == "RW":
            self.designated_player = self.blue[9]
        if inits == "GK":
            self.designated_player = self.blue[10]

    def PASS_BALL(self):
        # use self.DX and self.DY in self.pass_ball(self.DX, self.DY)
        self.pass_ball(self.DX, self.DY)
        

    def pass_ball(self, dx, dy):
        # at each gamestate for 5 gamestates, ball move_ball's in the direction defined by dx and dy
        # if ball is picked up by a player before 5 gamestates, then this ftn is overwritten (if not self.has_ball)
        # how to create gamestates? call this ftn every time a button is clicked
        if self.has_ball:
            self.num_gamestates = 5
            self.move_ball(dy * 2, dy * 2)
            self.has_ball = False


    # Move the ball with a specified direction and distance
    def move_ball(self, dx, dy):    
        x1, y1, x2, y2 = self.canvas.coords(self.BALL)
        new_x1, new_y1 = x1 + dx, y1 + dy
        new_x2, new_y2 = x2 + dx, y2 + dy

        # Ensure the ball stays within boundaries
        if new_x1 >= 50 and new_x2 <= 700 and new_y1 >= 50 and new_y2 <= 450:
            self.canvas.move(self.BALL, dx, dy)

    # Check if the player is close enough to kick the ball
    def is_near_ball(self, player):
        px1, py1, px2, py2 = self.canvas.coords(player)
        bx1, by1, bx2, by2 = self.canvas.coords(self.BALL)

        player_center_x, player_center_y = (px1 + px2) / 2, (py1 + py2) / 2
        ball_center_x, ball_center_y = (bx1 + bx2) / 2, (by1 + by2) / 2

        # Calculate distance between player and ball
        distance = ((player_center_x - ball_center_x) ** 2 + (player_center_y - ball_center_y) ** 2) ** 0.5

        # Define the proximity threshold for kicking the ball
        return distance < 15  # Adjust this value as needed

    # Functions for player movement and kicking
    def move_player(self, player, dx, dy):
        x1, y1, x2, y2 = self.canvas.coords(player)
        new_x1, new_y1 = x1 + dx, y1 + dy
        new_x2, new_y2 = x2 + dx, y2 + dy

        # Ensure the player stays within boundaries
        if new_x1 >= 50 and new_x2 <= 700 and new_y1 >= 50 and new_y2 <= 450:
            self.canvas.move(player, dx, dy)

            # Check if player can kick the ball
            if self.is_near_ball(player):
                self.has_ball = True
                self.DX = dx
                self.DY = dy
                self.move_ball(dx * 2, dy * 2)  # Kick the ball in the same direction with greater distance

            if self.num_gamestates > 0:
                self.move_ball(self.DX * 2, self.DY * 2)
                self.num_gamestates -=1

    # Controls for player 1
    def move_player1_up(self):
        self.move_player(self.designated_player, 0, -10)

    def move_player1_down(self):
        self.move_player(self.designated_player, 0, 10)

    def move_player1_left(self):
        self.move_player(self.designated_player, -10, 0)

    def move_player1_right(self):
        self.move_player(self.designated_player, 10, 0)


    def init_team(self, color, half, setup):
        # type == red/blue (0, 1), half == left/right (0, 1), setup == "433/442/etc"
        # return a list of 11 players and the approproate locations to create them
            # (player object, (x1, y1, x2, y2))
        
        if setup == "433":
            if half == 0:
                # Goalkeeper
                GOALKEEPER = self.canvas.create_oval(45, 245, 55, 255, fill=color)
                # Defense
                LEFTBACK = self.canvas.create_oval(145, 95, 155, 105, fill=color)
                LEFT_CENTER_DEFENSE = self.canvas.create_oval(145, 195, 155, 205, fill=color)
                RIGHT_CENTER_DEFENSE = self.canvas.create_oval(145, 295, 155, 305, fill=color)
                RIGHTBACK = self.canvas.create_oval(145, 395, 155, 405, fill=color)
                # Midfield
                LEFT_MF = self.canvas.create_oval(245, 145, 255, 155, fill=color)
                CENT_MF = self.canvas.create_oval(245, 245, 255, 255, fill=color)
                RIGHT_MF = self.canvas.create_oval(245, 345, 255, 355, fill=color)
                # Attack
                RIGHT_WING = self.canvas.create_oval(345, 145, 355, 155, fill=color)
                STRIKER = self.canvas.create_oval(345, 245, 355, 255, fill=color)
                LEFT_WING = self.canvas.create_oval(345, 345, 355, 355, fill=color)

                return [LEFTBACK, LEFT_CENTER_DEFENSE, RIGHT_CENTER_DEFENSE, RIGHTBACK, LEFT_MF, CENT_MF, RIGHT_MF, LEFT_WING, STRIKER, RIGHT_WING, GOALKEEPER]

            else:
                # Goalkeeper"
                GOALKEEPER = self.canvas.create_oval(695, 245, 705, 255, fill=color)
                # Defense
                RIGHTBACK = self.canvas.create_oval(595, 95, 605, 105, fill=color)
                RIGHT_CENTER_DEFENSE = self.canvas.create_oval(595, 195, 605, 205, fill=color)
                LEFT_CENTER_DEFENSE = self.canvas.create_oval(595, 295, 605, 305, fill=color)
                LEFTBACK = self.canvas.create_oval(595, 395, 605, 405, fill=color)
                # Midfield
                RIGHT_MF = self.canvas.create_oval(495, 145, 505, 155, fill=color)
                CENT_MF = self.canvas.create_oval(495, 245, 505, 255, fill=color)
                LEFT_MF = self.canvas.create_oval(495, 345, 505, 355, fill=color)
                # Attack
                LEFT_WING = self.canvas.create_oval(395, 145, 405, 155, fill=color)
                STRIKER = self.canvas.create_oval(395, 245, 405, 255, fill=color)
                RIGHT_WING = self.canvas.create_oval(395, 345, 405, 355, fill=color)
        
                return [RIGHTBACK, RIGHT_CENTER_DEFENSE, LEFT_CENTER_DEFENSE, LEFTBACK, RIGHT_MF, CENT_MF, LEFT_MF, RIGHT_WING, STRIKER, LEFT_WING, GOALKEEPER]

app = App()
app.mainloop()