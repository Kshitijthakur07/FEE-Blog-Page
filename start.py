import eel

eel.init("Fee-Project")

@eel.expose

def App():
    print("Application Running !")
    3
App()

eel.start("index.html", size=(800, 600))cvv