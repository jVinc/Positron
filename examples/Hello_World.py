from pysitron import PysitronApp

html_code = """
<button onclick="window.say_hello()" id="button">Click me to change text!</button>
"""


class SolarSystemApp(PysitronApp):
    def say_hello(self):
        self.window.document.getElementById('button').innerHTML = "Hello world!"


from pysitron.syntax_helpers import document

if __name__ == '__main__':
    app = SolarSystemApp(landing_page=html_code)
    app.run()
