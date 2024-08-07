# Modules

Any py file is considered a module.

*Do not name any files or directories the same as any built in modules, you will have issues.*

To go over how this might be managed on a project, [review virtual environments](./VirtualEnv.md)

## Import

you will use the keyword `import` to pull in a file. Export is not required to import a file.

When you import a file, you pull in the whole document.

For a document, you import by the name of the file.

You can rename/ provide an alias by using `as` and give it a different name. This syntax can also be used on specific items that are imported.

If you want to import only a specific function from a document,(known as select import), you would format the import like `from doc_name import fuc_name`. [Example](../Examples/Modules/module_two.py)

You can import multiple items, even different types of items, from the same document simple by placing a common between each item. [Example](../Examples/Modules/main.py)

*The name of the import must match across documents.*

If not specified by the from format, then all items will be accessed  through dot notation. The same is true if you the as formatting.

There is an option to import all by using `*` it would look like from doc_name import *`, this format is not recommended though. It can cause possible collisions in names, it if you use from, it is recommended you name the specific items you need from the imported document.

### Nested Imports

If the file you are trying to access is located in another folder, then you would use the from syntax to show the parent folder and specify the file you are trying to get to.

If you are importing based on a specific items, then you will use the from dot notation to show the parent file and then the document name. `from parent_folder.child_doc import fun_name`. [Example](../Examples/Modules/main.py)

## Built In Modules

These are items that can be imported to provide specific functionality.

Some of these built in options are:

- [os](./Files.md/#os)
- [pathlib](./Files.md/#pathlib)
- [time](./Modules.md/#datetime)
- [sys]()
- [math](../Examples/Modules/math_mod.py)
- [smtplib](../Notes/Files.md/#smtp)
- zipfile
- csv
- statistics
- pprint
- calendar
- [regex](../Examples/Modules/reg_exp.py)
- [random](../Examples/Modules/random_run.py)
- [secrets](../Examples/Modules/secerts_mod.py)

You can use `help` to see information about these built in functions.

To see what you can do with those modules, you would use `type` with the name: `type(module)`

To see the attributes, you would use `dir` with the module: `dir(module)`

### __name__

This is part of the directory system and allows you to see what document you are currently in or document you are currently accessing.[Example](../Examples/Modules/main.py)

### Convert to package

Create a folder, place your module files inside of the folder. Create a file called `__init__.py` in the folder. Import the modules into the file and provide a description of what this package does. If you wanted to register this package for public use, you could do so at [pypi](www.pypi.org).

[Example](../Examples/Modules/my_package/)

If you want/ need to install a specific version, you can find the different releases under, "release history" on the package pack. You will then run `pip install packagename==#.#.#`

### Datetime

This import creates objects for date and time.

[Example](../Examples/Modules/date_time.py)

[Official docs](https://docs.python.org/3/library/datetime.html)

You can use module `time` to measure how much time it takes to run some

### array

This function very similar to list and tuples. You specify the type of array you are creating as the first argument.

If the values you are trying to append to the array are not of the type, an error will occur and you will not be added to the list; unless, the value can be converted to that type.

[Example](../Examples/Modules/array_mod.py)

#### Reading and writing

The path provided for read and write are absolute.

The files are usually saved as binary.

If you want to read from a binary file, you will have to create an empty array where the values can be stored until read.

### sys

Sys is for system arguments. These are values that are stored within the python application itself. You can also get information about your application and system.

They are passed through the file item, it looks something like `python3 main.py username password`

If not agr are passed, then just the file name will be your agr.

[Example](../Examples/Modules/sys_mod.py)

### webbrowser

[Example](../Examples/Modules/web_browser.py)