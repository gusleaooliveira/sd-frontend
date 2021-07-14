from tkinter import *
import socketio as sio


socket = sio.Client()
app = Tk()
app.title('Client Thread')
app.geometry("800x600+100+100")

status = Label(app, text="Status...", bd=1, relief=SUNKEN, anchor=W).pack(side=BOTTOM, fill=X)

@socket.event
def connect():
    status.config(text='Estamos conectados!')

@socket.event
def disconnect():
    status.config(text='Estamos desconectados!')

@socket.event
def error(erro):
    status.config(text=f'Ocorreu um erro {erro}')

socket.connect('http://localhost:3000')
socket.disconnect()


