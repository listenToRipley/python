# Notes

## Table of Contents

- [Classes](./Classes.md)
- [Modules](./Modules.md)

## General Notes

### Encapsulation

Attributes and scope is specified within a singular function or object. [Example](../Examples/Classes/encap_inher_poly_abst.py)

### Inheritances

Passing down information from one item to the next to allow for content to be share in a parent child relationship [Example](../Examples/Classes/encap_inher_poly_abst.py)

### Polymorphism

A way to group items together, but the form related to the action is different across the group. Since they are unique, but they should be part of a similar group. This allows for a simple way to call on an action without have specified terms for each action for that extended element. [Example](../Examples/Classes/encap_inher_poly_abst.py)

### Abstraction

This is similar to polymorphism. A way to require an action to be included in children elements, include the logic code within it as well. [Example](../Examples/Classes/encap_inher_poly_abst.py)

### JSON and Dictionaries

Since JSON requires double quotes for the key pair values and python dictionaries require a single quote for the key pairs, and we need to convert the boolean values to a python format, you can use `json.loads()` to provide the correct format.

To convert a python dictionary to json formatting, you would use `json.dumps`

[Example](../Examples/General/json_to_dict.py)
