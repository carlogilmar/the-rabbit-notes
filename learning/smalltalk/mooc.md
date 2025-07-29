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

# Pharo Syntax

```pharo
exampleWithNumber: x # Method Definition with argument
  "This method illustrates the complete syntax."
  <aMethodAnnotation>

  |y| # Local variable definition
  true & false not & (nil isNil)
  	ifFalse: [self halt].
  y := self size + super size. # Instruction separator
  #($a #a 'a' 1 1.0)
  do: [:each| Transcript # Loops
  		show: (each class name);
  		show: (each printString);
  		show: ''].
  ^x<y # Return
```

## Hello World

```
'Hello World' asMorph openInWindow
```

A String is sending as a message to asMorph, we get a graphical element that can be open in a window object.

```pharo
|var| # Temporary variable declaration
var := aValue # Variable assignment
message . message # Separator
^expression # Return
[:x|x+2] value: 5 # Block
```

`Essense of Pharo`
1. Creating objects by using messages
2. Sending messages
3. Use blocks for anonymous methods

`Kind of messages`
1. Unary message
2. Binary message
3. Keyword message

`Sending messages to the same object`
```
ZnClient new # Creating a new object, unary message
	url: 'https://en.wikipedira.index.php';
	queryAt: 'title' put: 'Pharo';
	queryAt: 'action' put: 'edit';
	get # Unary message 
```

`Messages everywhere`
```
factorial
	"Answer the factorial of the receiver. #comment"
	self = 0 ifTrue: [^1].
	self > ifTrue: [^self * (self-1)factorial].
	self error: 'Not valid for negative integers'
```

```pharo
1 ro:4 do: [:i|Transcript <<i]
```

