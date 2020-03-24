# SWENG-35
Group 35, The Drip Allocators


Instructions  to run flask web application

- Make sure you have flask (i recommend using pip to downlaod) and python installed on your system
- Navigate to /SWENG-35/front-end
- Type "python adapt_website.py" into your command prompt
- Open your web browser at the given local host url which is given by the following text that should appear in the terminal:  

Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 336-907-092

Use flask-sqlalchemy for database
 - type "pip install flask-sqlalchemy" in the "front-end" file

How to use "implement_with_backend" in "front-end"
 - install flask-sqlalchemy, torchvision, scipy, matplotlib by typing
   "pip install flask-sqlalchemy",
   "pip install torchvision",
   "pip install scipy",
   "pip install matplotlib" in ".../SWENG-35/front-end/implement_with_backend/ClothCoParse"
 - Make sure you have flask (i recommend using pip to downlaod) and python installed on your system
 - extract the files in "photos" (".../clothing-co-parsing-master/photos") from "https://github.com/morawi/ClothExtract" and put them into ".../SWENG-35/front-end/implement_with_backend/Data/ClothCoParse/train/A"
 - extract the files in "photos" (".../clothing-co-parsing-master/annotations/pixel-leve") from "https://github.com/morawi/ClothExtract" and put them into ".../SWENG-35/front-end/implement_with_backend/Data/ClothCoParse/train/B"
 - change the path on line 94 in "adapt_website.py", 
   the path on line 53 in "load_then_test_model.py" and
   the path on line 42 in "datasets.py"