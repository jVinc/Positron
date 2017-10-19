from pysitron import PysitronApp

html_code = """
<script>
function set_button2(msg) {
    window.document.getElementById('button2').innerHTML = msg;
}
</script>
<button onclick="window.update_counter()" id="button">Hello world!</button><br/>
"""


class FastLoop(PysitronApp):
    def update_counter(self):
        for n in range(10000):
            self.window.document.getElementById('button').innerHTML = "Hello world!" + str(n)


""" Result I'm getting 100,000 updates in 35sec which is 2857 updates per second"""

if __name__ == '__main__':
    app = FastLoop(landing_page=html_code)
    app.run()
