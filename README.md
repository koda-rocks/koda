# koda

1. Pull the ladi-koda branch locally.
2. Have Python3 running locally and virtual environment and virtualenvwrapper.
*  `brew install python3` to install python3
* `pip install virtualenv` to install the virtualenv
* `pip install virtualenvwrapper` hopefully for virtualenvwrapper
* further instructions on getting your virtualenvwrapper to work
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
3. I hope you got the virtualenv to work if not, fret not we are just going to be installing modules globally
4. Create a virtualenv ` mkvirtualenv koda --python=/path/to/python3`.
5. Install the requirements `pip install -r requirements.txt`
6. Navigate to the koda directory and the entry is the pizza.py file
7. Run `python pizza.py` to test what we currently have.