import tkinter as tk
from fractal_generator_func import generator

def generate():
    res_h = int(ent_resolution_h.get())
    res_w = int(ent_resolution_w.get())
    cntr_real = float(ent_window_center_real.get())
    cntr_imag = complex(ent_window_center_imaginary.get() + "j")
    width = int(ent_width.get())
    generator((res_h, res_w), (cntr_real + cntr_imag), width)
    
#setting the widow
window = tk.Tk()
window.title("Mandelbrot")
window.resizable(width=False, height=False)

#since this is the first "app" I made it gets a 
#hello world introduction
greeting = tk.Label(
        text="Hello, world!",
        foreground="green",
        background="black",
        )
greeting.pack()

#frame_a is the input frame that feeds into the 
#madelbrot widget and has the initial conditions
frame_a = tk.Frame()
frame_a.pack()
frame_b = tk.Frame()
frame_btn = tk.Frame()
frame_btn.pack(pady=10, padx=10)

#setting resolution
label_res = tk.Label(master=frame_a, text="Resolution:")
label_x = tk.Label(master=frame_a, text="x")
ent_resolution_h = tk.Entry(master=frame_a, text="height", width=10)
ent_resolution_w = tk.Entry(master=frame_a, text="width", width=10, border=2)
ent_resolution_h.insert(0, "700")
ent_resolution_w.insert(0, "700")

#setting center point of render
label_window_center = tk.Label(master=frame_a, text="Center:")
label_plus = tk.Label(master=frame_a, text="+")
label_imaginary = tk.Label(master=frame_a, text="i")
ent_window_center_real = tk.Entry(master=frame_a, width = 10)
ent_window_center_imaginary = tk.Entry(master=frame_a, width = 10)
ent_window_center_real.insert(0, "-0.75")
ent_window_center_imaginary.insert(0, "0")
label_b = tk.Label(master=frame_b, text="I'm in frame B")

#setting the width of the madelbrot set that is in
#the window
lbl_width = tk.Label(master=frame_a, text="Width")
ent_width = tk.Entry(master=frame_a, width=10)
ent_width.insert(0, "3")

#the big start button
btn_generate = tk.Button(master=frame_btn, text="Generate", command=generate)
btn_generate.pack(padx=10, ipadx=10)

#organizig thing on the window
label_res.grid(row=0)
ent_resolution_h.grid(row=0,column=1)
label_x.grid(row=0, column=2)
ent_resolution_w.grid(row=0, column=3)

label_window_center.grid(row=1, column=0)
ent_window_center_real.grid(row=1, column=1)
label_plus.grid(row=1, column=2)
ent_window_center_imaginary.grid(row=1, column=3)
label_imaginary.grid(row=1, column=4, sticky="w")

lbl_width.grid(row=3)
ent_width.grid(row=3, column=1,columnspan=3, sticky="ew")

label_b.grid(row=0)

window.mainloop()