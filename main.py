import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#379237"
MY_BG = "#F8FFDB"
MY = "#BBD6B8"
MY_FG = "#F0FF42"
YELLOW = "#f7f5dd"
FONT_NAME = "Mute"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_timer_text, text="00:00")
    timer_text.config(text="Timer")
    check_text.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_text.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_text.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_text.config(text="Work Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(canvas_timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        # print("I'm Running")
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_text.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro Tracker")
window.config(padx=150, pady=150, bg=MY)
canvas = tkinter.Canvas(width=224, height=224, bg=MY, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(112, 112, image=tomato_img)
canvas_timer_text = canvas.create_text(112, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer Text

timer_text = tkinter.Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=MY, fg=MY_BG, highlightthickness=0)
timer_text.grid(column=1, row=0)

# Check Text

check_text = tkinter.Label(font=(FONT_NAME, 20, "bold"), bg=MY, fg=MY_FG, highlightthickness=0)
check_text.grid(column=1, row=4)

# Start Button
start_button = tkinter.Button(text="Start", bg=MY, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

# Reset Button

reset_button = tkinter.Button(text="Reset", bg=MY, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=3)

window.mainloop()
