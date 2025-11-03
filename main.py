import tkinter as tk
import math

# إنشاء النافذة
root = tk.Tk()
root.title("Modern calculator")
root.geometry("300x450")
root.resizable(False, False)

# إنشاء Canvas للخلفية المتدرجة
canvas = tk.Canvas(root, width=300, height=450)
canvas.pack(fill="both", expand=True)

# دالة لرسم Gradient
def draw_gradient(canvas, color1, color2):
    steps = 100
    r1,g1,b1 = canvas.winfo_rgb(color1)
    r2,g2,b2 = canvas.winfo_rgb(color2)
    r_ratio = (r2 - r1) / steps
    g_ratio = (g2 - g1) / steps
    b_ratio = (b2 - b1) / steps
    for i in range(steps):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = f"#{nr>>8:02x}{ng>>8:02x}{nb>>8:02x}"
        canvas.create_rectangle(0, i*4.5, 300, (i+1)*4.5, outline=color, fill=color)

draw_gradient(canvas, "#1E2A38", "#3498DB")  # من كحلي غامق للأزرق الفاتح

# شاشة الإدخال
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='ridge', bg="white", fg="#1E2A38", justify='right')
canvas.create_window(0, 0, anchor='nw', window=entry, width=300, height=50)

# دوال الأزرار
def click_button(value):
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        expr = entry.get()
        if "%" in expr:
            expr = expr.replace("%", "/100")
        if "√" in expr:
            expr = expr.replace("√", "math.sqrt")
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# تأثير الضغط على الأزرار
def on_press(e):
    e.widget['bg'] = '#34495E'
def on_release(e, color):
    e.widget['bg'] = color

# تأثير Hover
def on_enter(e):
    e.widget['bg'] = '#5DADE2'
def on_leave(e, color):
    e.widget['bg'] = color

# قائمة الأزرار
buttons = [
    ("7",1,0,"#ffffff"), ("8",1,1,"#ffffff"), ("9",1,2,"#ffffff"), ("/",1,3,"#2C3E50"),
    ("4",2,0,"#ffffff"), ("5",2,1,"#ffffff"), ("6",2,2,"#ffffff"), ("*",2,3,"#2C3E50"),
    ("1",3,0,"#ffffff"), ("2",3,1,"#ffffff"), ("3",3,2,"#ffffff"), ("-",3,3,"#2C3E50"),
    ("0",4,1,"#ffffff"), (".",4,0,"#ffffff"), ("+",4,3,"#2C3E50"), ("=",4,2,"#2C3E50"),
    ("C",5,0,"#E74C3C"), ("%",5,1,"#2C3E50"), ("√",5,2,"#2C3E50")
]

# إنشاء الأزرار على الـ Canvas
for (text,row,col,color) in buttons:
    if text == "=":
        btn = tk.Button(
            root, text=text, width=4, height=2, bg=color, fg="white", font=('Arial', 14), command=calculate,
            anchor='center', justify='center'
        )
    elif text == "C":
        btn = tk.Button(
            root, text=text, width=4, height=2, bg=color, fg="white", font=('Arial', 14), command=clear_entry,
            anchor='center', justify='center'
        )
    else:
        btn = tk.Button(
            root, text=text, width=4, height=2, bg=color, fg="#1E2A38", font=('Arial', 14), 
            command=lambda t=text: click_button(t),
            anchor='center', justify='center'
        )
    
    canvas.create_window(col*75, 50+row*60, anchor='nw', window=btn, width=70, height=50)
    
    # تأثير الضغط
    btn.bind("<ButtonPress-1>", on_press)
    btn.bind("<ButtonRelease-1>", lambda e, c=color: on_release(e, c))
    
    # تأثير Hover
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", lambda e, c=color: on_leave(e, c))

# تشغيل النافذة
root.mainloop()
