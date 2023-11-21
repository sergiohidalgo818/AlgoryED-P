rm -r doc
python3 -m pdoc --html p205.py -o doc
google-chrome doc/p205.html
