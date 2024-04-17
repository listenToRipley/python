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
