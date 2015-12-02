# -*- coding: utf-8 -*-
"""
Created on Sun May 03 17:29:17 2015

@author: MaGesh
"""

from sys import argv #importing all the python packages
import random, string, numpy as np;
from random import randint

def rand_num(): #this method will return the random hash values
    h=[];
    for j in range(0,8):
        randNum=randint(1000,9999)
        h.append(randNum)
    return h;
    
def False_Positive_Count(bloomfilter_array, hash_Data): #this is the method to find the false positive values
    i=j=count=0;
    false_positive=0;
    for i in range (0,1000000):
        for j in range (0,8):
            if(bloomfilter_array[hash_Data[i][j]]==1): #comparing bloomfilter array and returning false positive values
                count=count+1;
        if(count==8):
            false_positive=false_positive+1;
        count=0
    return false_positive;


def train_and_test_data(length,strings): #this is the function which returns the train and test values
    l=length;
    strings_test=strings;
    t=random.sample(xrange(999999),l); 
    characters=string.letters + string.digits + string.punctuation #strings with punctuations, digits, letters
    i=j=0;
    train_Data=[];
    for i in range(0,1000000):
        value=''.join(random.choice(characters) for j in range(10));
        train_Data.append(value); 
    h=rand_num();
    i=j=k=0;
    trian_value=0
    train_strings=[];
    hash_fun_bf1=np.zeros((1000,1),dtype=int);
    hash_fun_bf2=np.zeros((1000,1),dtype=int);
    for i in range (l):
        train_strings.append(train_Data[t[i]]);
    i=0;
    for i in range (0,l):
        for j in range (0,8):
            hash_1=h[j];
            hash_2=0;
            for k in range (0,10):#training the values
                trian_value=ord(train_strings[i][k]); #taking out the ASCII values of it
                hash_1=((hash_1 << 5)+hash_1)+trian_value; #hash 1 functions
                hash_2=trian_value+(hash_2 << 6)+(hash_2 << 16)-hash_2; #hash 2 functions
            hash_1=int(hash_1%1000)-1;
            hash_2=int(hash_2%1000)-1;
            if(hash_fun_bf1[hash_1]==0):
                hash_fun_bf1[hash_1]=1; #updating bloomfilter for hash 1
            if(hash_fun_bf2[hash_2]==0):
                hash_fun_bf2[hash_2]=1;#updating bloomfilter for hash 2
    h1=rand_num();
    i=j=k=0;
    test_value=0; #testing starts here
    bf1=np.zeros((1000000,8),dtype=int); 
    bf2=np.zeros((1000000,8),dtype=int);
    for i in range (0,1000000):
        for j in range (0,8):
            hash_1=h1[j];
            hash_2=0;
            for k in range (0,10):
                test_value=ord(strings_test[i][k]); #ASCII values of test data
                hash_1=((hash_1 << 5)+ hash_1)+test_value; #hash 1 test 
                hash_2=test_value+(hash_2 << 6)+(hash_2 << 16)-hash_2; #hash 2 test
            hash_1=int(hash_1%1000)-1;
            hash_2=int(hash_2%1000)-1;
            bf1[i][j]=hash_1;
            bf2[i][j]=hash_2;
    false_positive_h1=False_Positive_Count(hash_fun_bf1,bf1) #for first hash function
    false_positive_h2=False_Positive_Count(hash_fun_bf2,bf2) #for second hash function
    print false_positive_h1;
    print false_positive_h2;    

l=int(argv[1]); #Passing Different values
test_strings=np.genfromtxt('F:\\A.txt', dtype=str, delimiter = ' ') #TestStrings
train_and_test_data(l,test_strings); #method to find the train and test functions
