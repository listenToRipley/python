# Classes

You can see example of these [here](../Examples/Classes/classes.py).

For a formal summary, see [forums](../Examples/Classes/forum.py)

Attributes of a class will only be modified by the specific instance.

If you want to see the values included included within a classes, you can use `__dict__` with the instance names prior to it to see the complete object.

To see all the attributes/methods that can be call on a class you can use `dir(instance_name)`, this list will include methods you have created on the class object. Those created by you will usually be listed last on the list.

## Self

Self is variable references as a specific instance. 

Within a classes, own instance are you use the magic method of `__init__`. This is allow these to always be unique to each instance. 

If you fail to include the variables listed in `__init__`, this will require in an error as these are now considered required elements to create an object, unless you provide default options. This is also known as encapsulation.

## Static Methods

You would use these when you need to create methods that are independent of the specific instances of the class. Which means that you do note have to have a instance created in order to call these methods, they are functions associated with the class elements, but can be create by themselves. Think of it as a general function located inside of a class.

Non static methods are known as bound methods.

These do not require a self parameter and called directly.

This could be a way to incapsulate a series of methods that can be easily exported and imported.

## Magic Method

Universally accepted methods for instances of the class in which they are provided. They are different from regular methods since these will give you access to operands to use as a shorthand instead of calling the specific method name.

You will do this by using underscore and  the operands name, `__add__`

## Class Attributes

These are meant as a specific value that is associated with all instances of the class and can be changes based values changes inside of the `__init__` Important to note that while this value 

They cannot be modified within an instance, only by the function methodology associated with that variable. If you make changes, it will only be applied to the specific instance.

## Inheritance

There are extended classes, which take in one item and allow for additional methods.

Init is automatically created with the passed element, and all other items added to this class will be an extension.

Think of anything created in this extended class is a child of the passed element.
