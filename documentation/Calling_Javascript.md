# Calling Javascript from the Backend

Applications must inherit from [BrowserClass][BrowserClass], any methods declared
using the `bind_to_window` decorator are bound to the window object of javascript on the front-end.

```
class App(BrowserClass):
    @bind_to_window
    def say_hello(self):
        print('hello world')
```

The above code allows calls to `window.say_hello()` to be called in javascript, which results in the message being printed to the python console.

Front-end javascript functions can also be triggered from the backend using:
` self.window.function_name()` called from with-in the application object.

[BrowserClass]: file://other.md