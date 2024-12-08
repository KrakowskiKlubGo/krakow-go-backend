pip install -r requirements.txt
# update to node 20
npm install -g npm@latest
npm install -D rimraf cross-env@7.0.3
python3.9 manage.py collectstatic
python3.9 manage.py migrate
python3.9 manage.py tailwind build