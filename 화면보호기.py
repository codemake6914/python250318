import tkinter as tk
import random
import ctypes

def prevent_sleep():
    ES_CONTINUOUS = 0x80000000
    ES_DISPLAY_REQUIRED = 0x00000002
    ES_SYSTEM_REQUIRED = 0x00000001
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_DISPLAY_REQUIRED | ES_SYSTEM_REQUIRED)

def animate_firework(x, y, size, color):
    particles = []
    colors = ["red", "orange", "yellow", "white", "blue", "purple", "pink", "green"]
    max_radius = min(width, height) * 0.25  # 입자가 퍼지는 반경을 화면의 0.25로 설정
    for _ in range(160):  # 기존보다 4배 더 많은 입자 생성
        dx = random.randint(-int(max_radius), int(max_radius))
        dy = random.randint(-int(max_radius), int(max_radius))
        particle_color = random.choice(colors)  # 각 입자의 색상을 다르게 설정
        p = canvas.create_oval(x, y, x+0.5, y+0.5, fill=particle_color, outline=particle_color)  # 입자 크기를 0.1배로 축소
        particles.append((p, dx, dy))
    
    def move_particles(step=0, speed=11):
        if step < 22:  # 기존보다 2단계 더 길게 퍼지게 설정
            for p, dx, dy in particles:
                canvas.move(p, dx / speed, dy / speed)
            new_speed = max(1, speed * (0.05 ** (4 / (22 * 0.01))))  # 속도를 0.05로 설정하여 더 느리게 퍼짐
            root.after(10, move_particles, step + 1, new_speed)
        else:
            for p, _, _ in particles:
                canvas.delete(p)
            root.after(1000, create_firework)  # 1초 뒤 새 불꽃 생성
    
    move_particles()

def create_firework():
    x = random.randint(50, width - 50)
    y = random.randint(50, height - 50)
    size = random.randint(20, 50)
    color = random.choice(["red", "orange", "yellow", "white"])
    animate_firework(x, y, size, color)

def exit_screensaver(event):
    root.destroy()

root = tk.Tk()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.attributes("-fullscreen", True)
root.configure(bg="black")
root.bind("<Button-1>", exit_screensaver)

canvas = tk.Canvas(root, width=width, height=height, bg="black", highlightthickness=0)
canvas.pack()

prevent_sleep()  # 화면 잠금 및 절전 모드 방지
create_firework()
root.mainloop()
