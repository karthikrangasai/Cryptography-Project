import Crypto
from Crypto.Hash import SHA

from datetime import datetime as dt

import requests
from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from random import randint, sample

# To be used data for testing
votedFor = {
    '1010' : "Amethi : Modi and Patna : Obama",
    '1001' : "Amethi : Modi and Patna : Trump",
    '0110' : "Amethi : Rahul and Patna : Obama",
    '0101' : "Amethi : Rahul and Patna : Trump",
}
votedUsers = []
userVote = []


# Values for the ZKP
p = 11
g = 2
r = sample(range(0,11), 5)
b = [randint(0,1) for i in range(5)]


# User details
users = ['f20171499', 'f20171602', 'f20171501']
passwords = ['ringa', 'chandi', 'shilbi']
keys = [1,2,3]
y = [ (pow(g, val)%p) for val in keys]


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
        data = str(self.index) + str(self.time) + str(self.voter) + str(self.votes) + str(self.prevHash) + str(self.nonce)
        hashed.update(data.encode('utf-8'))
        return hashed



####  Creating the Blockchain Class  ####
class Blockchain:
    def __init__(self, diff):
        self.blockchain = []
        self.diff = diff
        self.verify = []
        self.verifyIndex = 0

    ## Create genesis block ##
    def genesisBlock(self):
        time = dt.now()
        self.createBlock(0, time, "None", "0000", "0", 0)

    ## Create new block ##
    def createBlock(self, index, time, voter, votes, prevHash, nonce):
        block = Block(index, time, voter, votes, prevHash, nonce)
        self.blockchain.append(block)

    def verifyTransaction(self):
        ret = []
        for i in range(5):
            h = pow(g, r[i])%p
            s = self.verify[i]
            ret.append((pow(g, s)%p) == (h * (pow(y[self.verifyIndex], b[i])%p)))
        
        print("In Verify Transaction\n")
        print(ret.count(True))

        if ret.count(True) >= 3:
            return True
        else:
            return False

    def nonceCalcFunc(self, block):
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

blockchain = Blockchain(2)
blockchain.genesisBlock()
print(blockchain)

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
            return render_template('verify.html', value=currentUser, len = len(r), r = r, b = b)
        else:
            error = 'Invalid Credentials. Please try again.'
            # flash('Invalid Credentials. Please try again.')
            return render_template('login.html', error=error)
            # return render_template('login.html')

#Verify User
@app.route('/verifyTransaction', methods=['GET', 'POST'])
def verifyTransaction():
    if request.method == 'POST':
        blockchain.verify.append(int(request.form['one']))
        blockchain.verify.append(int(request.form['two']))
        blockchain.verify.append(int(request.form['three']))
        blockchain.verify.append(int(request.form['four']))
        blockchain.verify.append(int(request.form['five']))
        blockchain.verifyIndex = users.index(request.form['currUser'])
        print(blockchain.verifyIndex)
        if blockchain.verifyTransaction():
            currentUser = request.form['currUser']
            return render_template('voting.html', value=currentUser)
        else:
            error = 'Invalid User.'
            return render_template('login.html', error=error)
    return render_template('verify.html')


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
        keys.append(int(request.form['key']))
        y.append((pow(g, int(request.form['key']))%p))
        print(users)
        print(passwords)
        print("\n")
        print(keys)
        # return render_template(url_for('home'))
    return render_template('registration.html')


@app.route('/viewUser', methods=['GET','POST'])
def viewUser():
    if request.method == 'POST':
        candidate = request.form['username']
        index = votedUsers.index(candidate)
        candidateVote = votedFor[userVote[index]]
        print(candidate)
        print(candidateVote)
        return render_template('login.html', val = candidateVote)
    return render_template('viewUser.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
    # app.run(host='0.0.0.0', port=5000)
