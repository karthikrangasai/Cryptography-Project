# Cryptography-Project
An implementation of Blockchain that demonstrates a voting system and uses Zero Knowledge Proof for User Verification. The project uses the Python Language, Flask framework and PyCrypto library to implement it.

# Instructions
1. Use a virtual environment creator like virtualenv (in my case) to create a python virtual environment.
2. Create a python virtual environment using the command `virtualenv -p /usr/bin/python3.5 venv`.
3. Python 3.5.2 must be running in the virtual environment.
4. Install flask 1.0.2 in the virtual environemt using `pip install flask==1.0.2`.
5. Install the dependency in the virtual environment `PyCrypto` using the command `pip install pycrypto` or `pip install pycrypto --user`.
5. Now, fork and clone this repository to work with it.
6. Running `python flaskApp.py` should start the flask server that runs the program.
7. The program initiates a blockchain and adds the genesis block as the program starts.
8. Run `http://127.0.0.1:5000/` on a browser to use the GUI.


# Files
```bash
.
├── blockchain.py
├── flaskApp.py
├── __pycache__
│   └── blockchain.cpython-35.pyc
└── templates
    ├── login.html
    ├── registration.html
    ├── verify.html
    ├── viewUser.html
    └── voting.html
```
