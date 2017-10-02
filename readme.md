# Positron
A framework that makes it simple to develop applications using Python and web technologies, HTML/JS/CSS.

This is still extremely early development. The current state might fail, and everything could potentially change moving forwards.
Still if you try it out and have feedback it is very much appreciated.

## How it works
Positron uses cefpython to launch a window running the Chromium Embedded Framework browser, and sets it up to show a temporary local webserver ([more...][framework]).

It then binds your defined python functions such that they can be called from javascript in the browser.

This is done simply by inheriting from the class [PositronApp][PositronApp]

## Hello World

A simply hello world example can be made all in one file by creating a new class derived from [BrowserClass][BrowserClass],
and decorating the functions to be made available in the front-end.

```Python
from Positron import PositronApp

html_code = """
<button onclick="window.say_hello()">Click me to change text!</button>
<div id = "textfield">...</div>
"""

class HelloApp(PositronApp):
    def say_hello(self):
        self.window.document.getElementById('textfield').innerHTML = "Hello world!"


if __name__ == '__main__':
    app = HelloApp(window_title="Hello World App",
                             default_text=html_code,
                             port_number=8023,
                             window_dimensions=(400, 300))
    app.run()
```

## Larger projects
For larger projects, the default behavior of the server is to serve static files from a given directory. Which
makes it easy to plug in JS or HTML components from web development and quickly get an independent app running.

Typical project structure would be:
```
rootdir/
    app.py
    /static/
        _js/
        _html/
        _css/
```

## Templated HTML

Py-Tron doesn't enforce or make any assumptions on the HTML code, this makes it easy to plug in any particular templating framework you might want to use.

``` Example with jinja2 ```


[framework]: file://other.md
[PositronApp]: file://other.md
[BrowserClass]: file://other.md