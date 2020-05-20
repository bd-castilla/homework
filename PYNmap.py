#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ben Castilla"
__email__ = "ben@castilla.us"
__date_ = "Spring 2020"
__version__ = "0.0.1"

# LIBRARIES
from datetime import date
import os
import pickle
import json
import subprocess

# SET VARIABLES
my_dir = r'C:\Users\benca\Downloads\18'
#my_pickle = r'c:\users\benca\downloads\18' + date_str + ".pickle"
#my_json = date_str.json
port_list = ['192.168.0.1:80', '192.168.0.1:23', '192.168.0.1:22']
nmap_path = r'C:\Program Files (x86)\Nmap\nmap.exe'
nmap_network = '192.168.0.119'
print("#18 and #19 and #20")
print(" ")
print("my_dir variable: ", my_dir)
#print(my_pickle)
#print(my_json)
print("port_list: ", port_list)
print("nmap path: ", nmap_path)
print("nmap network: ", nmap_network)


def create_directory():   
    if(os.path.isdir(my_dir)) == False:
        try:  
            os.mkdir(my_dir)
            print ("INFO: The directory was created:", my_dir) 
        except OSError:  
            print ("ERROR: Failed to create directory:", my_dir)
    else:
        print ("INFO: The directory already exists:", my_dir) 
        
def create_date_string():
    date_str = date.today().strftime("%m%d%y")
    print("Date String:", date_str)
    return date_str
    
    

def write_files():
    # write the pickle file
    with open(my_pickle, 'wb') as fp:
        pickle.dump(port_list, fp)
    fp.close()
    
    # write the json file
    with open(my_json, 'w') as fp:  
        json.dump(port_list, fp)
    fp.close()

def read_files():
    port_list = []
    
    # read the pickle file
    with open (my_pickle, 'rb') as fp:
        port_list = pickle.load(fp)
    fp.close()
    
    print("pickle:", port_list)
    
    port_list = []
    
    # read the json file
    with open(my_json, 'r') as fp:  
        port_list = json.load(fp)
    fp.close()
    
    print("json:", port_list)

def run_nmap():
    nmap_out = subprocess.run([nmap_path, "-T4", nmap_network], capture_output=True)
    nmap_data = nmap_out.stdout.splitlines()
    
    print(nmap_data)
    return nmap_data
    
# Check directory

create_directory()

# Create date string and variables
datefile = create_date_string()
datefile_pickle = datefile +".pickle"
datefile_json = datefile +".json"
datefile_results =  datefile + "_results.txt"
print("datefile: ", datefile)
print("datefile_pickle: ", datefile_pickle)
print("datefile_json: ", datefile_json)
print("datefile_results", datefile_results)

my_pickle = r'c:\users\benca\downloads\18\\' + datefile_pickle
my_json = r'c:\users\benca\downloads\18\\' + datefile_json
my_results = r'c:\users\benca\downloads\18\\' + datefile_results
print("my_pickle: ", my_pickle)
print("my_json: ", my_json)

# Run nmap
results = run_nmap()
sourceFile = open(my_results, 'w')
print(results, file = sourceFile)
sourceFile.close()

# Write 
write_files()



print("finished")
print(" ")



