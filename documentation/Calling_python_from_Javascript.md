# Calling python from javascript

Applications must inherit from [PysitronApp][PysitronApp], any methods declared
are automatically bound in the front-end

```
class App(PysitronApp):
    def say_hello(self):
        print('hello world')
```

The above code allows calls to `window.say_hello()` to be called in javascript, which results in the message being printed to the python console.

Front-end javascript functions can also be triggered from the backend using:
` self.window.function_name()` called from with-in the application object.

## Return values from python to javascript

The way return values are passed from python to javascript relies on Promises, and can be used with the async/await language features.
[Learn more about async/await ...][asyncawait]

The python functions are bound to javascript functions that return a Promise with the result of the python evaluation
Therefore there are several options for calling back-end functions:
* A) Call the function without return values by simply calling it. The function will execute asynchronously while javascript execution continues. `result = backend_fun()`
* B) Call the function with await in a async function. The async function will pause execution until the return value is ready. inside async function call: `result = await backend_fun()`
* C) Call the function and attach a callback to the Promise which will be executed when the result is ready. `backend_fun().then(result => handle(result))`

## Return values javascript to python

[PysitronApp]: PysitronApp.md
[asyncawait]: https://blog.sessionstack.com/how-javascript-works-event-loop-and-the-rise-of-async-programming-5-ways-to-better-coding-with-2f077c4438b5