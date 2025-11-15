echo "BUILD START"
python3.9m -m pip install -r requirements.txt
python3.9m manage.py collectstatic --noinput
echo "BUILD COMPLETE"
