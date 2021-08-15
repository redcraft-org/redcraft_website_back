# Redcraft - Backend

## Setup

### Requirement

- Install:
    - python 3.8 or higher
    - mysql
    - venv


- Create and setup your .env by copying .env.example
- Create your database

### Mac

Use `setup_mac.sh`, or folow these instruction.

- Create your virtual environment with `python3 -m venv env`
- Start your virtual environment with `source ./env/bin/activate`
- Install requirements with `pip install -r requirements.txt`
- Migrate DB with `python manage.py migrate`


### Windows

Use `setup_window.sh`, or folow these instruction.

- Create your virtual env: `python3 -m venv env`
- Start your virtual environment with `"env/Scripts/activate"`
- Install requirements with `pip install -r requirements.txt`
- Migrate DB with `python manage.py migrate`

### Linux

Use `setup_linux.sh`, or folow these instruction.

- Create your virtual environment with `python3 -m venv env`
- Start your virtual environment with `source env/bin/activate`
- Install requirements with `pip install -r requirements.txt`
- Migrate DB with `python manage.py migrate`

## Start development

Create your fixture with: `python manage.py generate_dev_fixtures {min_article_per_category} {max_article_per_category}`
Import your fixture with: `python manage.py loaddata dev_fixtures.json `
Start server with: `python manage.py runserver`

## Contributions

If you would like to contribute you can refer to the documentation and the "modification protocol" made available.

- Doc: 
- Protocol: 
