python3 JSFinder.py -f domain.txt -ou out_domain.txt &&
echo "JSFinder finished!!!"
echo "Get directory start..."
python3 get_URL_directory.py out_jsf.txt out_gd.txt &&
echo "Get directory finished!!!"
echo "Dirsearch start..."
python3 dirsearch.py -l out_gd.txt
echo "Dirsearch finished!!!"