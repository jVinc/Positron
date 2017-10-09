from itertools import chain
import random
from Pysitron import PysitronApp


html_code = """
<h2>Hello demo</h2>

<p>
    <div id = "greet" style="background-color:purple;">...</div>
    <button onclick="window.greet()">Click me repeatedly!</button>
<p>

<div id = "explain">...</div>
<button onclick="window.explain()">And click me repeatedly too!</button>
"""
# todo: imports will be an issue. Which ones should go toe the frontend and which to the backend?


class SolarSystemApp(PysitronApp):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.planets = [list(chain(planet, (index + 1,))) for index, planet in enumerate((
            ('Mercury', 'hot', 2240),
            ('Venus', 'sulphurous', 6052),
            ('Earth', 'fertile', 6378),
            ('Mars', 'reddish', 3397),
            ('Jupiter', 'stormy', 71492),
            ('Saturn', 'ringed', 60268),
            ('Uranus', 'cold', 25559),
            ('Neptune', 'very cold', 24766)
        ))]

        self.lines = (
            '{} is a {} planet',
            'The radius of {} is {} km',
            '{} is planet nr. {} counting from the sun'
        )
        self.lineIndex = 0
        self.planet = self.planets[int(random.random() * len(self.planets))]

    def greet(self):
        self.planet = self.planets[int(random.random() * len(self.planets))]
        string_to_set = 'Hello {}'.format(self.planet[0])
        self.window.document.getElementById('greet').innerHTML = string_to_set
        self.explain()

    def explain(self):

        string_to_set = self.lines[self.lineIndex].format(self.planet[0], self.planet[self.lineIndex + 1])
        self.window.document.getElementById('explain').innerHTML = string_to_set
        self.lineIndex = (self.lineIndex + 1) % 3


if __name__ == '__main__':
    app = SolarSystemApp(landing_page=html_code)
    app.run()
