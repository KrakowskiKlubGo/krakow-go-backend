pip install -r requirements.txt
npm install -D rimraf cross-env
npm install
python3.9 manage.py collectstatic
python3.9 manage.py migrate
python3.9 manage.py tailwind build