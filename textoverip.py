import socket
import threading
import tkinter as tk

root = tk.Tk()

spravy = []

def server_program():
    global spravy
    host = ''
    port = 5841
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.bind((host, port))
    ss.listen(9999999)
    
    while True:
        print("Server started, listening for connections...")
        conn, address = ss.accept()
        print("Connection from: " + str(address))
        while True:
            rec_message = conn.recv(1024)
            if not rec_message:
                break
            message = rec_message.decode('utf-8')
            print("Received from client: " + message)
            s = str(address) + " - " + str(message)
            spravy.insert(0, s)
            canvas.delete("all")
            for i in range(len(spravy)):
                canvas.create_text(5, 785 - (i*15), text = spravy[i], font="Arial, 15", anchor = tk.W)
            canvas.update()
            break
        conn.close()
    
 
def client_program():
    global spravy
    host = entry_ip.get()
    port = 5841
    if entry_message != "": 
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cs.connect((host, port))
    
        message = entry_message.get()
        cs.sendall(message.encode('utf-8'))
        
        s = str(address) + " - " + str(message)
        spravy.insert(0, s)
        canvas.delete("all")
        for i in range(len(spravy)):
            canvas.create_text(5, 785 - (i*15), text = spravy[i], font="Arial, 15", anchor = tk.W)
        canvas.update()
        cs.close()

server_thread = threading.Thread(target=server_program)
server_thread.start()

entry_ip = tk.Entry(root, font="Arial, 15", width=20)
entry_ip.grid(row=0, column=0)

canvas = tk.Canvas(root, width=1000, height=800, bg="white")
canvas.grid(row=1, column=0)

entry_message = tk.Entry(root, font="Arial, 15", width=70)
entry_message.grid(row=2, column=0, padx=(0, 220))

send = tk.Button(root, text="Send", font="Arial, 15", command=client_program)
send.grid(row=2, column=0, padx=(915, 0))
tk.mainloop()