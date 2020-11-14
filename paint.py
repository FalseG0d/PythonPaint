from tkinter import *
from tkinter import colorchooser,filedialog,messagebox
from tkinter.ttk import Scale
from PIL.ImageGrab as ImageGrab


class Paint():
    def __init__(self,root):
        self.root=root
        self.root.title("Paint")
        self.root.geometry("800x520")
        self.root.configure(background="white")
        self.root.resizable(0,0)

        self.pen_color="black"
        self.eraser_color="white"

        self.color_frame=LabelFrame(self.root,text='Color',font=('arial',15),bd=5,relief=RIDGE,bg="white")
        self.color_frame.place(x=0,y=0,width=70,height=185)

        colors=['red','blue','yellow','green','cyan','purple','violet','pink','orange','brown','black','white']

        i=j=0
        for color in colors:
            Button(self.color_frame,bg=color,bd=2,relief=RIDGE,width=3,command=lambda col=color:self.select_color(col)).grid(row=i,column=j)
            i+=1
            if i==6:
                i=0
                j+=1

        self.eraser_button=Button(self.root,text="ERASER",bd=4,bg='white',command=self.eraser,width=8,relief=RIDGE)
        self.eraser_button.place(x=0,y=187)

        
        self.clear_button=Button(self.root,text="CLEAR",bd=4,bg='white',command=lambda : self.canvas.delete("all"),width=8,relief=RIDGE)
        self.clear_button.place(x=0,y=217)
        

        self.save_button=Button(self.root,text="SAVE",bd=4,bg='white',command=self.save,width=8,relief=RIDGE)
        self.save_button.place(x=0,y=247)
        

        self.canvas_color_button=Button(self.root,text="CANVAS",bd=4,bg='white',command=self.canvas_color,width=8,relief=RIDGE)
        self.canvas_color_button.place(x=0,y=277)
        

        self.custom_color_button=Button(self.root,text="COLOR",bd=4,bg='white',command=self.custom_color,width=8,relief=RIDGE)
        self.custom_color_button.place(x=0,y=307)

        self.pen_size_scale_frame=LabelFrame(self.root,text='Size',font=('arial',15),bd=5,relief=RIDGE,bg="white")
        self.pen_size_scale_frame.place(x=0,y=337,width=70,height=170)

        self.pen_size=Scale(self.pen_size_scale_frame,orient=VERTICAL,from_=50,to=0,length=140)
        self.pen_size.set(1)
        self.pen_size.grid(row=0,column=1,padx=15)

        self.canvas=Canvas(self.root,bg='white',bd=5,relief=GROOVE,height=500,width=700)
        self.canvas.place(x=80,y=0)

        self.canvas.bind("<B1-Motion>",self.paint)

    def paint(self,event):
        x1,y1=(event.x-2),(event.y-2)
        x2,y2=(event.x+2),(event.y+2)

        self.canvas.create_oval(x1,y1,x2,y2,fill=self.pen_color,outline=self.pen_color,width=self.pen_size.get())

    def select_color(self,col):
        self.pen_color=col

    def eraser(self):
        self.pen_color=self.eraser_color

    def canvas_color(self):
        color=colorchooser.askcolor()
        self.eraser_color=color[1]
        self.canvas.configure(background=color[1])

    def custom_color(self):
        color=colorchooser.askcolor()
        self.pen_color=color[1]

    def save(self):
        try:
            filename=asksaveasfilename(defaultextension='.jpg')
            
            x=self.root.winfo_rootx()+self.canvas.winfo_x()
            y=self.root.winfo_rooty()+self.canvas.winfo_y()

            x1=x+self.canvas.winfo_width()
            y1=y+self.canvas.winfo_width()

            ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
            messagebox.showinfo('Paint Says ','Image Is Saved As '+str(filename))

        except:
            messagebox.showinfo('Paint Says ','Something Went Wrong, Cannot Save File')






if __name__=="__main__":
    root=Tk()
    p=Paint(root)
    root.mainloop()