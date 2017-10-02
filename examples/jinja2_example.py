from jinja2 import Environment, FileSystemLoader
from Positron import PositronApp


class SolarSystemApp(PositronApp):
    def say_hello(self):
        self.window.document.getElementById('textfield').innerHTML = "Hello world!"


if __name__ == '__main__':
    # Set up a simple environment and load the template
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('jinja2_template.html')

    app = SolarSystemApp(
        landing_page=template.render(my_string="Wheeeee!", my_list=[0, 1, 2, 3, 4, 5]),
        window_dimensions=(800, 600))
    app.run()
