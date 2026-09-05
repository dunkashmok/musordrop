import tkinter as tk
import random

b, price = 500, 268
items = [("Махачкала", 387, "gold"), ("Пузо алишера", 500, "red"), ("День города", 400, "pink"), ("Солярис лехи", 300, "purple"), ("МИРЭА", 200, "blue"), ("фури", 100, "white")]

def animate(speed: float | int = 30.0):
    global b
    canvas.move("tape", -speed, 0)

    for i in canvas.find_withtag("card"):
        coords = canvas.coords(i)
        if coords and coords[0] < -110:
            canvas.move(i, 12 * 110, 0)
            canvas.move(i + 1, 12 * 110, 0)

    if speed > 0.4:
        root.after(15, animate, speed * 0.95)
    else:
        center_item = canvas.find_closest(165, 40)[0]
        if "text" in canvas.gettags(center_item):
            center_item -= 1

        win_idx = (center_item - 1) // 2 % len(items)
        name, win_p, col = items[win_idx]

        b += win_p
        lbl_bal.config(text=f"Баланс: {b} рублей", fg="white")
        lbl_status.config(text=f"Выпало: {name} и эта хуета стоит {win_p} рублей", fg=col)

        if b < price:
            lbl_bal.config(text=f"Баланс: {b} рублей, ты нищий", fg="white")
            btn.config(text="Начать сначала", bg="red", state="normal", command=restart)
        else:
            btn.config(state="normal")

def buy():
    global b
    b -= price
    lbl_bal.config(text=f"Баланс: {b} рублей")
    lbl_status.config(text="Рулеточка крутится", fg="white")
    btn.config(state="disabled")
    animate(random.uniform(30.0, 45.0))

def restart():
    global b
    b = 500
    lbl_bal.config(text=f"Баланс: {b} рублей", fg="white")
    lbl_status.config(text="Мусор дроп крути!", fg="gray")
    btn.config(text=f"Открыть кейс ({price}p)", bg="#ff9900", command=buy)

root = tk.Tk()
root.title("Musor drop")
root.geometry("360x280")
root.configure(bg="#1a1a1a")

lbl_bal = tk.Label(root, text=f"Баланс: {b} рублей", font=("Arial", 14, "bold"), bg="#1a1a1a", fg="white")
lbl_bal.pack(pady=5)

canvas = tk.Canvas(root, width=330, height=80, bg="#252525", highlightthickness=0)
canvas.pack(pady=5)

for i in range(12):
    name, _, col = items[i % len(items)]
    x = i * 110
    canvas.create_rectangle(x, 5, x + 100, 75, fill="#333", outline=col, width=2, tags=("tape", "card"))
    canvas.create_text(x + 50, 40, text=name, fill="white", font=("Arial", 10, "bold"), tags=("tape", "text"))

canvas.create_polygon(155, 0, 175, 0, 165, 15, fill="red")

lbl_status = tk.Label(root, text="Испытай удачу", font=("Arial", 10, "italic"), bg="#1a1a1a", fg="gray")
lbl_status.pack(pady=5)

btn = tk.Button(root, text=f"Открыть кейс ({price}p)", font=("Arial", 10, "bold"), bg="#ff9900", fg="black", command=buy)
btn.pack(pady=10)

root.mainloop()

root.mainloop()
