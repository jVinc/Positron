# PysitronApp

This class defines the main workings of the application.
It exposes a self.window object that can be used to a access javascript functionality in python.
It also makes python code accessible in javascript by binding the class methods to the javascript window object.

This defines the communication path back and forth between front-end and backend.

```Python
class MyApp(PysitronApp):
    def say_hello(self):
        self.window.document.getElementById('button').innerHTML = "Hello world!"

app = MyApp(landing_page="<button onclick="window.say_hello()" id="button">Click me to change text!</button>")
app.run()
```