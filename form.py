import eel

eel.init("web")

@eel.expose
def recv_data(login, password):
    print(login, password)

eel.start("index.html", mode = 'edge', size = (200,200))