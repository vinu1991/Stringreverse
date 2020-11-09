#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: vinu

Source:
    
'''

# Import necessary modules
 
DEFAULT_TAGS = """
#datascience #machinelearning #feature #featurepreneur #deeplearning #python #artificialintelligence #deeplearning #datascientist #python #dataanalytics #artificialintelligence #ml #bigdata #data #statistics #businessanalytics #r #kaggle #tableau #github #rprogramming #linearregression #timeseries #classification #clustering  #logisticregression #ai #analytics
"""

def generate_content(content_base):

    content = content_base

    content += "\n" + DEFAULT_TAGS

    return content


def startpy():
    
    content = """
Once ML video can not make you a Data Scientist. Check the roadmap for the Data Science career.
    """

    new_content = generate_content(content)

    print(new_content)
    print(Mystrreverse(new_content))


def Mystrreverse(orignalstr):
    return orignalstr[::-1]
    """temp=""
    length=len(orignalstr)
    for i in range(length-1,-1,-1):
        temp+=orignalstr[i]
    return temp"""
    

if __name__ == '__main__':
    startpy()