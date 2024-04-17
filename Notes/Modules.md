# Modules

Any py file is considered a module.

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

- os
- time
- sys
- math
- smtplib
- zipfile
- csv
- statistics
- pprint
- calendar
- regex
- random

You can use `help` to see information about these built in functions.

To see what you can do with those modules, you would use `type` with the name: `type(module)`

To see the attributes, you would use `dir` with the module: `dir(module)`
