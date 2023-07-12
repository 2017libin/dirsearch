@echo off
pip install -r requirements.txt
python JSFinder.py -f in_jsf.txt -ou out_jsf.txt
python get_URL_directory.py out_jsf.txt out_gd.txt
python dirsearch.py -l out_gd.txt
pause