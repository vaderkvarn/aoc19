tj="tmp.jpeg"
tt="tmp"
python3 both.py input | sed 1d | convert -  -scale 86x12 -gravity center -page A4  -negate pdf:- | convert - $tj
tesseract tmp.jpeg $tt > /dev/null 2>&1
head -1 $tt.txt

rm $tj
rm $tt.txt
