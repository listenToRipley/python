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