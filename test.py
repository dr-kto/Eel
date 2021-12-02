import eel

eel.init("test")

#python -> js
@eel.expose
def call_in_js(x):
    print(x)

#js -> python
eel.call_in_python("Hello, from JS")

eel.start("test.html", mode="edge", size = (500, 500))

