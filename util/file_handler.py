#Code by http://denis.papathanasiou.org/2012/05/07/using-microsofts-translator-api-with-python/
# Vem um XML, falta pegar o valor!
from os import listdir
from os.path import isfile, join
from text_handler import extractFormattedTweet
from translator import translate_text
from text_handler import fixWords
import os

def getFilesFromFolder(folder_file_location):
        onlyFiles = [f for f in listdir(folder_file_location) if isfile(join(folder_file_location, f))]
        return onlyFiles
    

def parseFiles(file_to_parse, folder_destination):
    print ' ***** Abrindo:',file_to_parse, '******'
    file_name = file_to_parse[file_to_parse.rfind('\\'):file_to_parse.rfind('.txt')]
    qnt_lines = 0
    qnt_repetitions = 0
    qnt_minimum_words = 0
    qnt_fixed = 0
    lineArray = []
    try:
        file_opened =  open(file_to_parse)
        
        while 1:
            line = file_opened.readline()
            if not line:
                break
            else:
                qnt_lines+=1
                formattedTwitter = extractFormattedTweet(line)
                if len(formattedTwitter.text.split(" ")) < 3:
                    qnt_minimum_words+=1
                elif formattedTwitter.text in lineArray:
                    qnt_repetitions+=1
                else:
                    lineArray.append(formattedTwitter.text)
                #print '*****'
                #print formattedTwitter.text
                #print '*****'
    except IOError:
        print ("Error, could not open file:", file_to_parse)


    file_folder = folder_destination+'\\Filtered\\'
    if not os.path.exists(file_folder):
        os.makedirs(file_folder)
    
    file_filtered = file_folder+file_name+'_filetered.txt'

    file_txt_filtered = open(file_filtered, "w")
    
    qnt_errors = 0

    for line in lineArray:
        try:
            text,words =  fixWords(line)
            if len(words) > 0:
                qnt_fixed+=1
            file_txt_filtered.writelines(text+'\n')
        except:
            print 'Error in line:', line
            qnt_errors+=1
            
        
        #file_txt_translated.writelines(translate_text(text)+'\n')
    
        
    print 'Total lines: ', qnt_lines
    print 'Total errors: ', qnt_errors
    print 'Total repetitions: ', qnt_repetitions
    print 'Total Fixed: ', qnt_fixed
    print 'Total minimum words: ', qnt_minimum_words
    print 'Total valid: ', len(lineArray)
    
def parseAllFilesFromFolder(folder_file_location):
    onlyFiles = getFilesFromFolder(folder_file_location)
    for fileinfolder in onlyFiles:
        file_location = folder_file_location+'\\'+fileinfolder
        parseFiles(file_location, folder_file_location)
                

def translateAllFilesFromFolder(folderLocation):
    onlyFiles = getFilesFromFolder(folderLocation)
    for fileinfolder in onlyFiles:
        file_location = folderLocation+'\\'+fileinfolder
        try:
            file_opened =  open(file_location)
            
            file_translated = file_location.replace(".txt","")
            file_translated = file_translated+'_translated.txt'
            print file_translated
            
            file_txt_translated = open(file_translated, "w")
    
            
            while 1:
                line = file_opened.readline()
                if not line:
                    break
                else:
                    translated = translate_text(line)
                    print translated
                    file_txt_translated.writelines(translated+'\n')
            
        except:
            print ("Error, could not open file:", file_opened)
            
                

# --- Starting here ----
program_name = "Ratinho"
print ' ---- Starting Search for %s ---- ' %(program_name)

folder_location = "C:\\Users\\avt\\Dropbox\\Mestrado\\workspace\\TweetResults\\"

folder_file_location = folder_location+program_name
print ' ---- looking txt files at %s ---- ' %(folder_file_location)

parseAllFilesFromFolder(folder_file_location)

filtered_folder_location = folder_file_location+"\\Filtered\\"

translateAllFilesFromFolder(filtered_folder_location)
    

print ' ---- end ---- '
