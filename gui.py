from tkinter import*
import os
def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")


st=Tk()
st.title("ShutDownAPP")
st.config(bg="blue")
st.geometry("500x500")
r_button=Button(st,text="Restart",font=("Time New Roman",20,"bold"),command=restart)
r_button.place(x=150,y=60,height=50,width=200,)
x_button=Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),command=restart_time)
x_button.place(x=150,y=170,height=50,width=200,)
lg_button=Button(st,text="Log-Out",font=("Time New Roman",20,"bold"),command=logout)
lg_button.place(x=150,y=270,height=50,width=200,)
sd_button=Button(st,text="Shut-Down",font=("Time New Roman",20,"bold"),command=shutdown)
sd_button.place(x=150,y=370,height=50,width=200,)
st.mainloop()