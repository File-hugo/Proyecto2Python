import tkinter as tk # Python 3
my_w = tk.Tk()
my_w.geometry("420x200") # width and height of the window

b1=tk.Button(my_w,text='One',font=28,
    command=lambda :l1.config(text='Button One '))
b1.grid(row=0,column=0,padx=30,pady=10)
b2=tk.Button(my_w,text='Two',font=28,
    command=lambda :l1.config(text='Button Two'))
b2.grid(row=0,column=1,padx=10,pady=10)

#command=lambda :l1.config(text='Button Two')
#command=lambda :b1.invoke()
l1=tk.Label(my_w,text='No Click ',bg='yellow',
    width=13,font=('Times',26,'normal'))
l1.grid(row=1,column=0,padx=30,pady=10,columnspan=3)
#b2.invoke() # Click or Command of button 2 
my_w.mainloop()

