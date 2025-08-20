import os    
from chardet import detect

# get file encoding type

srcfile='EditedNotes.txt'
trgfile='EditedNotesUtf.txt'

def get_encoding_type(file):
    with open(file, 'rb') as f:
        rawdata = f.read()
    return detect(rawdata)['encoding']

from_codec = get_encoding_type(srcfile)

# add try: except block for reliability
try: 
    with open(srcfile, 'r', encoding=from_codec) as f, open(trgfile, 'w', encoding='utf-8') as e:
        text = f.read() # for small files, for big use chunks
        e.write(text.replace("Ã¼", "ü").replace("Ã¶", "ö").replace("Ã¤", 'ä').replace('ÃŸ', "ß"))


except UnicodeDecodeError:
    print('Decode Error')
except UnicodeEncodeError:
    print('Encode Error')

