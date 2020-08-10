'''
Quick installation script to get everything up-and-running.
'''
import os

os.system('pip install opus-tools')
os.system('pip install opus')
os.system('pip install sox')
os.system('pip install ffmpeg')
os.system('pip install -U nltk')
import nltk
nltk.download('wordnet')
os.system('pip install -r requirements.txt')
