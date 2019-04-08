from collections import OrderedDict

import binascii

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

import hashlib
import json
from datetime import datetime as dt
from urllib.parse import urlparse
from uuid import uuid4

import requests
from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
# from flask_cors import CORS


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
        self.votes = votes
        self.voter = voter
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
        block = Block(self.index, dt.now(), "None", "0000", "0", 0)
        return block

    ## Create new block ##
    def createBlock(user, vote, prevHash, nonce):
        self.index += 1
        block = Block(self.index, dt.now(), user, vote, prevHash, nonce)
        return block

    def verifyTransaction():
        pass

    # def nonceFunc(nonce, block):
    #     testHash = SHA.new()
    #     testHash.update((str(block.time) + str(self.voter) + str(block.votes) + str(self.prevHash) + str(nonce)).encode('utf-8')))
    #     return testHash[:self.diff] == '0'*self.diff 


    ## Calculate NONCE using proof of work ##
    def mineBlock(block):
        nonce = 0
        testHash = SHA.new()
        while True:
            # data = 
            testHash.update((str(block.time) + str(self.voter) + str(block.votes) + str(self.prevHash) + str(nonce)).encode('utf-8'))
            if (testHash.hexdigest()[:self.diff] == '0'*self.diff):
                break
            else:
                nonce += 1
        return nonce


    ## View respective user's Vote ##
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


# @app.route('/viewUser', methods=['POST'])
# def viewUser():
#     if request.method == 'GET':
#         # candidate = users.append(request.form['username'])
#         candidate = username
#         print(candidate)
#         candidateVote = userVote[votedUsers.index(candidate)]
#         return render_template('viewUser.html', val = candidateVote)
#     return render_template('viewUser.html')


if __name__ == '__main__':
    # app.debug = True
    app.run(host='127.0.0.1', port=5000)
    # app.run(host='0.0.0.0', port=5000)
