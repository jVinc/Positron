""" This example shows how to open a file and read its contents"""

from pysitron import PysitronApp


class FileOpenApp(PysitronApp):
    def doprint(self, content):
        print(content)
        self.window.document.getElementByID('content').innerHTML = content


html_content = """
<input type="file" onchange="read = new FileReader();read.readAsBinaryString(this.files[0]);read.onloadend = function(){doprint(read.result);}">
<div id="content"></div>
"""

if __name__ == '__main__':
    app = FileOpenApp(landing_page=html_content)
    app.run()
