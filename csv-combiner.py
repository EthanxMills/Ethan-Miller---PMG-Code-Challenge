#   PMG Code Challenge\csv-combiner.py
#   Author: Ethan R. Miller
#   Date:   03-28-2022
#   Purpose: This script takes in a list of csv files and combines them into a single csv file
#   Input:   csv files
#   Output:  new csv file

import sys # argument work
import csv # csv writer & file work
import os.path as path

DIR = path.abspath(path.dirname(__file__)) # get the absolute path of the directory the script is in from generatefixtures.py

def main():

    # evaluate command line arguments
    if len(sys.argv) < 2:
        print('Usage: {} <csv files>'.format(sys.argv[0])) # message to notify proper form of usage
        sys.exit(1) # Note to self: make more graceful later if time (usr exp !ideal here)

    # create a list of the csv files that are passed through the command line
    cmdArgs = sys.argv[1:] # the first argument is the name of the script so we start at index 1 forward for grabbing the csv files

    # split the args into two lists, one for the csv files and one for the name of the new csv file name to be created
    csvFiles = []
    newCsvFile = "windows_combined.csv" # file used for powershell run case in demonstration 
    flag = False # Flag to help deliminate the csv files from the new csv file name
    for arg in cmdArgs:
        print(arg)
        if arg.endswith('.csv') & flag == True: # the only arg post > with ending csv is the name of the output file (see readme line 13)
            newCsvFile = arg
        if arg.endswith('.csv'): #when we see a csv file add it to the list of csv files, they're all listed before > making it safe
            csvFiles.append(arg)
        if arg == '>':
            flag = True
    
    # create the new csv file with given name and headers (email_hash, category, filename)
    with open(path.join(DIR, newCsvFile), "w", encoding= 'utf-8', newline='') as alpha:
        writer = csv.writer(alpha, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(['email_hash', 'category', 'filename'])     # Headers for the new csv file
        writer.writerow (['|----------', '|--------', '|----------|']) # Buffer row as shown in readme
   
    # record the filenames of the given files for later use in origin column
    filenames = []
    for file in csvFiles:
        filenames.append(file) # add the filename to the list of filenames

    # trim filenames for just base filename
    for i in range(len(filenames)):
        filenames[i] = filenames[i].split('/')[-1]

    # append the rows of each csv file into the new csv file using the rowCount list to know how which rows filename to use
    with open(newCsvFile, "a") as alpha:
        writer = csv.writer(alpha, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL) # create writer
        for i in range(0, len(csvFiles)): # use list of csv's as the thing to iterate over
            with open(csvFiles[i], "r", encoding='utf-8') as alpha:
                reader = csv.reader(alpha)
                for row in reader: # for each row in the csv file
                    if row[0] != 'email_hash': #skip the header row in each file so we just get data
                        writer.writerow([row[0], row[1], filenames[i]]) # filename is aligned with csv records thanks to earlier

if __name__ == '__main__':
    main() # run the main function
    