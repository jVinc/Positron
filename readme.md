# Pysitron
A framework that makes it simple to develop applications using Python and web technologies, HTML/JS/CSS.

This is still extremely early development. The current state might fail, and everything could potentially change moving forwards.
Still if you try it out and have feedback it is very much appreciated.

## How it works
Pysitron uses cefpython to launch a window running the Chromium Embedded Framework browser, and sets it up to show a temporary local webserver ([more...][framework]).

It then binds your defined python functions such that they can be called from javascript in the browser.

This is done simply by inheriting from the class [PysitronApp][PysitronApp]

## Hello World

A simply hello world example can be made all in one file by creating a new class derived from [PositronApp][PositronApp],
and decorating the functions to be made available in the front-end.

```Python
from Pysitron import PysitronApp

html_code = """
<button onclick="window.say_hello()">Click me to change text!</button>
<div id = "textfield">...</div>
"""

class HelloApp(PysitronApp):
    def say_hello(self):
        self.window.document.getElementById('textfield').innerHTML = "Hello world!"


if __name__ == '__main__':
    app = HelloApp(landing_page=html_code)
    app.run()
```

## Examples

[Go to overview of examples](documentation/examples.md)

* [Hello world](examples/Hello_World.py)
* [Form BMI calculator](examples/bmi_calculator.py)
* [jinja2 templates](examples/jinja2_example.py)

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

Pysitron doesn't enforce or make any assumptions on the HTML code, this makes it easy to plug in any particular templating framework you might want to use.
An example using jinja2 is located in the examples folder.


[framework]: file://other.md
[PysitronApp]: /documentation/PysitronApp.md