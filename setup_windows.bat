rmdir /S /Q env
python3 -m venv env
"env/Scripts/activate"
pip install -r requirements.txt
python manage.py migrate
