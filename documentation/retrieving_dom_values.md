# Retrieving DOM values in python

When accessing sub objects of the dom, certain "end points" will retrieve the values of the dom.
Examples are:

1. .nodeValue is a little more confusing to use, but faster than innerHTML.
1. .innerHTML parses content as HTML and takes longer.
1. .textContent uses straight text, does not parse HTML, and is faster.
1. .innerText Takes styles into consideration. It won't get hidden text for instance.
1. .value typically used for input and form elements

And example can be seen in the [bmi calculator example][other] where `getElementByID()` is
used to select a tag, and `.value` is the used to get the value in text form.
```
height = float(self.window.document.getElementById('height').value)
weight = float(self.window.document.getElementById('weight').value)
```






[other]: other.md