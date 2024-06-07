# Virtual Environments

Virtual Environments are created in Python project in order to manage the project dependencies and keep information truncated. This also allows you to preserve specific versions of packages.

Since you manage in this way, it means you won't have to global install all packages (PIP files) onto your computer.

You create such an environment by running  `python3 -m venv venv`

The second `venv` is the name of the folder. It is best practice to keep it under that name.

This folder will contain all required files to run a python application will be included inside of the venv folder.

## Activate

From your main folder run, `source venv/bin/activate`

This command will run the environment from the terminal. 

To verify it is running, you may see `(venv)` to the left of your cursor.

If you do not, then you can try `which python` and you should show as being inside `$PATH/venv/bin/python`

To turn off, run `deactivate`

To verify it has been turned on, you can try running `which python` again and it should say, "python not found".

## Dependencies Management 

Do not copy your `venv` file to your repo, they are too large. For the dependencies managements/coordination, you can copy the dependencies to a separate files, `pip freeze > requirements.txt`. 

Now you should update your .gitignore file to include venv files, and only upload the developed code along with your requirements.txt *this file is not best practice, look over the [pipenv section](./VirtualEnv.md/#pipenv)*

If you are now retrieving this repo without the venv file, you will need to run the `python3 -m venv venv` command again. Then run `pip install -r requirements.txt`, this will pull in all your dependencies. To verify they were installed run `pip freeze`

### Remove dependencies

You use the same pip functionality of `pip uninstall package_name`

This will not remove dependencies that were included with that package, so be very careful with uninstalling.

### PIPENV

This is the best practice and you can ignore the steps previously to set up your new env. To view an example file, [go here](../pipenv_project/)

If you just you a requirements doc, then this can easily out of sync with any added items. We want your dependencies list to always stay updated with any changes.

One of the most popular solutions to this problem is [pipenv](https://pypi.org/project/pipenv/)

This functions very similar to package.json or yarn files if you are familiar with those package management systems.

In order to use this package, it does have to be install globally.

Once installed, inside your file, run `pipenv shell`

This will create the venv and activate it, so additional commands will not be required.

There should now see file Pipfile creates.

If you need to see which virtual environment is currently being used, you can run `pipenv --venv`

You can also use `pipenv --where` to see the physical path or `which python` to see the virtual location.

To see the dependencies inside this environment, you can use `pip list` or `pipenv graph`

#### Install packages

Instead of using the `pip install`, we want to use `pipenv install` to ensure that our pipenv files is updated for any changes. 