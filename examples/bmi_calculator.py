from Positron import PositronApp

html_code = """
<link rel="shortcut icon" href="file:///C:/Users/vincent/Documents/Positon-Framework/resources/logo/logo_vector.svg" />
<form>
<input type="text" hint="height" id="height"></input>cm<br/>
<input type="text" hint="weight" id="weight"></input>kg<br/>
<button type="button" onclick="calc_bmi()">Submit</button><br/>
bmi: <span id="bmi">...</span>
</form>
"""


class SolarSystemApp(PositronApp):
    def calc_bmi(self):
        # Note that when getting things from the dom, you get back a string, so you need to do type conversion if you
        # want to do math.
        height = float(self.window.document.getElementById('height').value)
        weight = float(self.window.document.getElementById('weight').value)
        bmi = round(weight/height**2*10**4, 2)
        self.window.document.getElementById('bmi').innerHTML = str(bmi)


if __name__ == '__main__':
    app = SolarSystemApp(landing_page=html_code)
    app.run()