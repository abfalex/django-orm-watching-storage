# Bank security console
The famous Cathay Bank had security problems for several years until it went beyond what was acceptable. This project provides the ability to manage the viewing of visits to a bank vault, which will greatly simplify the life of accountants.

## Installation
Before installing, make sure you already have [python](https://www.python.org/) 3.x installed.

To work with a project, you need to install or clone it.

Use the following command in terminal to clone:

```bash
git clone https://github.com/abfalex/django-orm-watching-storage.git
```

Next, you need to create a virtual environment for easy use (recommended):

   ```bash
   python -m venv <venv_name>
   ```

After installing the virtual environment, you need to activate it:

  - On Windows:

     ```bash
     <venv_name>\Scripts\activate
     ```

  - On macOS and Linux:

       ```bash
       source <venv_name>/bin/activate
       ```

To work with the project, you also need to install package dependencies. Enter this command into the terminal:

```bash
pip install -r requirements.txt
```

## Environment variables
For the project to work correctly, you need to put some data in the `.env` file. Create a `.env` file and put some values:

- `DB_ENGINE` - database type

- `DB_HOST` - database host

- `DB_PORT` - database port

- `DB_NAME` - database name

- `DB_USER` - database user

- `DB_PASSWORD` - database user password

- `SECRET_KEY` - secret key

- `DEBUG_MODE` - debug mode (True - enable, False - disable)

- `ALLOWED_HOSTS` - allowed domains or addresses


## Launch
If you succeeded in all of the above, congratulations. All you have to do is run the project by running the following command in the terminal:

```bash
python main.py runserver
```