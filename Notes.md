# Notes

## Classes

You can see example of these [here](./classes.py)

Attributes of a class will only be modified by the specific instance.

If you want to see the values included included within a classes, you can use `__dict__` with the instance names prior to it to see the complete object.

To see all the attributes/methods that can be call on a class you can use `dir(instance_name)`, this list will include methods you have created on the class object. Those created by you will usually be listed last on the list.

### Self

Self is variable references as a specific instance. 

Within a classes, own instance are you use the magic method of `__init__`. This is allow these to always be unique to each instance. 

If you fail to include the variables listed in `__init__`, this will require in an error as these are now considered required elements to create an object, unless you provide default options. This is also known as encapsulation. 

### Static Methods

You would use these when you need to create methods that are independent of the specific instances of the class. Which means that you do note have to have a instance created in order to call these methods, they are functions associated with the class elements, but can be create by themselves. Think of it as a general function located inside of a class.

Non static methods are known as bound methods.

These do not require a self parameter and called directly.