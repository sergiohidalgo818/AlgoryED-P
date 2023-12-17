#rm -r doc
# python3 -m pdoc --html p205.py -o doc
python3 -m pdoc p205.py -o doc
#google-chrome doc/p205.html
python3 -m pylint p205.py 

