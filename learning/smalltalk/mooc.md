# Learning Pharo 

[MOOC Link to YT Video](https://mooc.pharo.org/)
[MOOC Lessons](https://mooc.pharo.org/)

## Download the IDE

1. Create the Pharo image by choosing the proper version.
	- An image is a snapshot of the Pharo app.
2. After create the image, you'll get the Pharo environment.

- Full syntax in a postcard
- Dynamically typed
- Everything is an object instance
- All methods are public virtual
- Attributes are protected
- Single inheritance
- Is fully inspectable and reflective
- You can get immersed in objects

1. Go to Playground
2. Go to System Browser
3. Go to Debug -> Finder

Pharo Object Model
- Objects
- Messages: intents (what)
- Methods: how to do it
- Closure: Anonymous methods (blocks `[]`)
- Everything is an object
- All computations are done via message passing
- Sending a message
- Instance variables are protected
- All methods are public
- No constructors or static methods or type declarations or interfaces

`10@20`
- A new point is create
- `@` sending the message
- `10` is an object SmallInteger
- `20` is the argument

`'Pharo','is Cool'`
- String concatenation

`Monster new` 
- Create new class

`Tomagoshi withHunger: 10`
- Create new class
- Class Method with parameter

