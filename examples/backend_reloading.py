""" Example of dynamic reloading of the python source on page reload.

Example usage:
1. Run the app.
2. Press print, and see the text printed from version 1.
3. Update the version string in the static method version() to '2'
4. Save changes, do not re-run the script
5. Press reload in the front end.
6. Press print, and see the text printed from version 2.
"""

from pysitron import PysitronApp as App, reloader_obj
import inspect
import importlib.util
import types
import itertools
import __main__

class MyApp(App, reloader_obj):
    def backend_function(self, arg):
        print(arg)
        val = 42**2
        return f'backend value {val}'

    @staticmethod
    def version():
        return '1'

    def shout(self):
        return f'This was printed from version v{self.__class__.version()} of the script'


if __name__ == '__main__':
    page = """
    <button onclick='shout().then(function(res){document.getElementById("output").innerHTML=res;});'>Print</button>
    <button onclick='location.reload();'>Reload</button>
    <div id="output"></div>
    """
    app = MyApp(landing_page=page, developer_mode=True)

    print('from file:', inspect.getfile(app.__class__))

    app.run()

