# A throw-away Python script to generate sample catalog data.

import os
import shutil

# basenotes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

# No flats:
basenotes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

octavemap = [
    ',,,,', 
    ',,,,,', 
    ',,,,',
    ',,,',
    ',,',
    ',',
    '',
    '',
    '\'',
    '\'\'',
    '\'\'\''
]

note2abc = {}
abcnotes = []

for octave in range(10):
    for n in basenotes:
        abcn = n.replace('b', '_');
        if (octave <= 6):
            abcn = abcn.upper()
        else:
            abcn = abcn.lower()
        
        note2abc[n + str(octave)] = abcn + octavemap[octave]
        abcnotes.append(abcn + octavemap[octave])

print('const sample_catalog = new Map([ \n')

rootdir = './_samples/farts/'

print('[\'Farts\', [')
            
noteindex = 5
for _, _, files in os.walk(rootdir):
    for file in files:
        abcnote = abcnotes[noteindex]
        noteindex += 1
        s = '  [ ' + ('\'' + file.replace('.wav','') + '\',').ljust(13) + ' ' + ('\'' + file + '\',').ljust(11) + '  ' + ('\'' + abcnote + '\'').ljust(9) + ' ]'
        if file != files[-1]:
            s += ','

        print(s)
        
        src = rootdir + '/' + file
        dst = rootdir + '../../samples/' + file
        shutil.copyfile(src, dst)
        

'''
rootdir = './_samples/MusyngKite/'

for instrumentpath, _, files in os.walk(rootdir):
  
    instrument = instrumentpath.split('/')
    if len(instrument)==4:
        instrument = instrument[-1]
        
        if instrument:
            print('[\'' + instrument + '\', [')
            for filenote in note2abc.keys():
                file = filenote + '.mp3'
                if file in files:
                    abcnote = note2abc[filenote]
                    sampleid = filenote[:1].upper() + filenote[1:].replace('b', '\\u266d')
                    targetfilename = (instrument + '-' + filenote + '.mp3').replace(' ','-').lower()
                    s = '  [ ' + ('\'' + sampleid + '\',').ljust(13) + ' ' + ('\'' + targetfilename + '\',').ljust(11 + len(instrument)) + '  ' + ('\'' + abcnote + '\'').ljust(9) + ' ]'
                    if filenote != list(note2abc.keys())[-1]:
                        s += ','

                    print(s)
                        
                    src = rootdir + instrument + '/' + file
                    dst = rootdir + '../../samples/' + targetfilename
                    shutil.copyfile(src, dst)

            print(']],')

print(']);')
'''