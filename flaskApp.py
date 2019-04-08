import Crypto
from Crypto.Hash import SHA

from datetime import datetime as dt

import requests
from flask import Flask, jsonify, request, render_template, redirect, url_for, flash


# To be used data for testing
votedFor = {
    '1010' : "Amethi : Modi and Patna : Obama",
    '1001' : "Amethi : Modi and Patna : Trump",
    '0110' : "Amethi : Rahul and Patna : Obama",
    '0101' : "Amethi : Rahul and Patna : Trump",
}

votedUsers = []
userVote = []

users = ['f20171499', 'f20171602', 'f20171501']
passwords = ['ringa', 'chandi', 'shilbi']


####  Creating the Block Class  ####
class Block:
    def __init__(self, index, time, voter, votes, prevHash, nonce):
        self.index = index
        self.time = time
        self.voter = voter
        self.votes = votes
        self.prevHash = prevHash
        self.nonce = nonce
        self.currHash = self.hashBlock()

    def hashBlock(self):
        hashed = SHA.new()
        data = str(self.time) + sself.voterstr(self.votes) + str(self.prevHash) + str(self.nonce)
        hashed.update(data.encode('utf-8'))
        return hashed



####  Creating the Blockchain Class  ####
class Blockchain:
    def __init__(self, diff):
        self.blockchain = []
        self.diff = diff
        self.index = 0

    ## Create genesis block ##
    def genesisBlock(self):
        self.createBlock(self.index, dt.now(), "None", "0000", "0", 0)

    ## Create new block ##
    def createBlock(index, time, voter, votes, prevHash, nonce):
        block = Block(index, time, voter, vote, prevHash, nonce)
        self.blockchain.append(block)

    def verifyTransaction():
        pass

    def nonceCalcFunc(block):
        prev = block
        nonce = 0
        
        testHash = SHA.new()
        testHash.update((str(nonce) + str(prev.index) + str(prev.time) + str(prev.voter) + str(prev.votes) + str(prev.prevHash) + str(prev.nonce)).encode('utf-8'))
        
        while (testHash.hexdigest()[:self.diff] == '0'*self.diff):
            nonce += 1
            testHash.update((str(nonce) + str(prev.index) + str(prev.time) + str(prev.voter) + str(prev.votes) + str(prev.prevHash) + str(prev.nonce)).encode('utf-8'))

        return nonce

    ## Calculate NONCE using proof of work ##
    def mineBlock(voter, votes):
        prevBlock = blockchain[-1]
        nonce = self.nonceCalcFunc(prevBlock)
        self.createBlock((prevBlock.index + 1), dt.now(), voter, votes, prevBlock.currUser, nonce)

    def viewUser():
        pass


app = Flask(__name__)
# Route for Login Page
@app.route('/')
@app.route('/home')
def home():
    # return redirect(url_for('login'))
    return render_template('login.html')

# Route for Voting Page
@app.route('/vote/')
def vote():
    return render_template('voting.html')

# Login check and if successful route to Voting page
@app.route('/login', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        currentUser = request.form['username']
        currentUserPass = request.form['password']
        if currentUser in users and currentUserPass in passwords and users.index(currentUser) == passwords.index(currentUserPass):
            return render_template('voting.html', value=currentUser)
        else:
            error = 'Invalid Credentials. Please try again.'
            # flash('Invalid Credentials. Please try again.')
            return render_template('login.html', error=error)
            # return render_template('login.html')

# Take Votes
@app.route('/calculateVote', methods=['POST'])
def calVote():
    if request.method == 'POST':
        votedUsers.append(request.form['currUser'])
        userVote.append(request.form['Amethi'] + request.form['Patna'])
        # userVote.append(request.form['Patna'])
        print(votedUsers)
        print("\n")
        print(userVote)
    return render_template('login.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        users.append(request.form['username'])
        passwords.append(request.form['password'])
        print(users)
        print(passwords)
        # return render_template(url_for('home'))
    return render_template('registration.html')


@app.route('/viewUser', methods=['POST'])
def viewUser():
    if request.method == 'GET':
        # candidate = users.append(request.form['username'])
        candidate = username
        print(candidate)
        candidateVote = userVote[votedUsers.index(candidate)]
        return render_template('viewUser.html', val = candidateVote)
    return render_template('viewUser.html')


if __name__ == '__main__':
    # app.debug = True
    app.run(host='127.0.0.1', port=5000)
    # app.run(host='0.0.0.0', port=5000)
