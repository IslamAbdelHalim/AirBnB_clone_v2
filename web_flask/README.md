This is The flask fram work and make the web Dynamic


### What is a Web Framework?
a web framework a software framework that is designed to support the development of web applications including web services, web resources and web APIs are a piece of software that offers a way to create and run web applications. Thus, you don’t need to code on your own and look for probable miscalculations and faults.

### How to build a web framework with Flask?
1. import Flask class in the web app
2. create an instance from this class and
<app = Flask(__name__)>
3. use the route to specific the pages and determine where the function work or somethink like that
4. create a function that manibulate with page and return html or data and manibulate with this data 
5. run this application by <Flask.run()>
and you can specifiy the debug and the port inside the run

### How to define routes in Flask?
by the name of app and use . after that as you can define the method in class 
and give the route the path of page
<@app.route("/")>
/ this mean that you in the root page

### What is a route?
Is a decorator that tell the flask what url should trigger our functions
and also bind functions to url

### How to handle variables in a route?
