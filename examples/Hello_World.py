from Positron import PositronApp

html_code = """
<button onclick="window.say_hello()" id="button">Click me to change text!</button>
"""


class SolarSystemApp(PositronApp):
    def say_hello(self):
        self.window.document.getElementById('button').innerHTML = "Hello world!"


if __name__ == '__main__':
    app = SolarSystemApp(landing_page=html_code)
    app.run()