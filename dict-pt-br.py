#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:35:24 2017

Author: André Pacheco
Email: pacheco.comp@gmail.com

"""

from xml.etree import ElementTree as ET
import os
import glob
import json

# This is the dictionary that will save all words and grams
dic_pt_br = dict()

# My path
path = os.getcwd() + '/dicionarioXML'
allFiles = glob.glob(path+'/*.xml')


for fil in allFiles:    
    # reading the XML
    print 'Processing the file: ', fil[-5:]
    root = ET.parse(fil).getroot()    
    
    # Parsing the XML
    for entry in root:
        gotWord = False
        gotGram = False
        for sub in entry:   
            if sub.tag == 'form':
                try:
                    word = sub.find('orth').text
                    gotWord = True
                except AttributeError:
                    pass
            elif sub.tag == 'sense':
                try:
                    gram = sub.find('gramGrp').text
                    gotGram = True
                except AttributeError:
                    pass
            if gotWord and gotGram:
                # Savind the dictionary
                dic_pt_br[word.lower()] = gram.lower()
    
# Saving the dictionary
json.dump(dic_pt_br, open("dic-pt-br.txt",'w'))
    
    
    
    
    
    
    
    
    
