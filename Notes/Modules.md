# Modules

Any py file is considered a module.

## Import

you will use the keyword `import` to pull in a file. Export is not required to import a file.

When you import a file, you pull in the whole document.

For a document, you import by the name of the file.

You can rename/ provide an alias by using `as` and give it a different name.

If you want to import only a specific function from a document,(known as select import), you would format the import like `from doc_name import fuc_name`. [Example](../Examples/Modules/module_two.py)

*The name of the import must match across documents.*

If not specified by the from format, then all items will be accessed  through dot notation.
