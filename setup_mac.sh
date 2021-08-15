set -e
rm -rf env
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
python manage.py migrate
