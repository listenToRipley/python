# Files

## Built in Modules

### os

Package that contains various modules, including path. This is a function approach.

[Examples](../Examples/Files/os.py)

### pathlib

Object-oriented approach to working with files.

[Examples](../Examples/Files/pathlib.py)

## Reading and Writing

Files must be opened and closed when readings.

If you use the `with` keyword, the file will be closed after you read it.

### Write

In the `with open('file_name.type')` you must provide a second argument. The second argument is known as the "mode". The default mode is read, so if the second argument is left out, it is assumed you want to read.

To write to a new file, the mode will be 'w'.

To add to an existing file, use 'a' as your mode. If you don't, use 'a' and still use 'w', it will overwrite the existing concent.

'a' stands for append.

Best practice is the create the path to the file you want to write to if it does not exist in your current directory.

The mode itself won't provide content to be created, it just shows what you will be doing in the file. You will provide the path, file name and the the method associated with the mode to use it.

[Example](../Examples/Files/read_write.py)

### Removing

You can do this by using pathlib's unlink method.

## Zip Archives

You do this through another built in module of `zipfile`.

[Examples](../Examples/Files/zip_arch.py)

## CSV

Comma seperated values.

[Examples](../Examples/Files/csvs.py)

## Sending Emails

We are using the module [EmailMessage](https://docs.python.org/3/library/email.message.html) for this work.

[The example](../Examples/Files/emails.py), will not work unless you have the [smtp](./Files.md/#smtp) running before you start this.

You should see on your localhost the email sent once the code is run.

These files have to be opened and closed like other examples of files. You can do this using the `with` keyword.

### SMTP

This example used the [docker container smtp4dev](https://github.com/rnwood/smtp4dev) as a server. This allows us to run sample emails from this docker server simulation.

To start container run `docker run --rm -it -d -p 3000:80 -p 2525:25 rnwood/smtp4dev`

To verify you container is running from the terminal, you can see it through `docker ps`

To see the activity of the server, you can use `docker log container_id`. This will include messages sent through the server.

#### Formatting for HTML

Create an [HTML file](../Examples/Files/templates/template.html)

You will then use the modules `Template` and `Path` to specific the location and format of your document. You can pass the values you used as marker through `$` and then process email as you would other email.

## SQLite

This examples used [sqlite3](https://docs.python.org/3/library/sqlite3.html)

Database connections have to be opened and closed like other files. This can be done using the `with` keyword. If you can not connecting through a local instance, then make sure you specify the path to the db.

To see output of this content, make use you do go [sqlitebrowser](https://sqlitebrowser.org/) and download the option for your system.

Open it and then open your "db" by open the files created through your connection in your project.

[Example](../Examples/Files/sqllite.py)