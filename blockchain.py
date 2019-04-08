from collections import OrderedDict

import binascii

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4

import requests
from flask import Flask, jsonify, request, render_template

class Block:
    def __init__():
        self.timestamp = timestamp
        self.vote = vote
        self.previous_hash = previous_hash
        self.hash = current_hash
        self.nonce = nonce
    
    def createBlock():
        pass
    
    def hashBlock():
        pass

    

class Blockchain:
    def __init__():
        pass

    def createBlock():
        pass

    def verifyTransaction():
        pass

    def mineBlock():
        pass

    def viewUser():
        pass