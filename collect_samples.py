import os
import shutil

print(  'const sample_catalog = new Map([ \n' \
    '[\'Percussion\', [\n' \
    '    [ \'hihat-808\',   \'hihat-808.wav\',   \'C\' ],\n' \
    '    [ \'clap-808\',    \'clap-808.wav\',    \'D\' ],\n' \
    '    [ \'kick-plain\',  \'kick-plain.wav\',  \'E\' ],\n' \
    '    [ \'kick-808\',    \'kick-808.wav\',    \'F\' ],\n' \
    '    [ \'snare-808\',   \'snare-808.wav\',   \'G\' ],\n' \
    '    [ \'openhat-808\', \'openhat-808.wav\', \'A\' ],\n' \
    '    [ \'top-808\',     \'tom-808.wav\',     \'B\' ],\n' \
    ']],')

rootdir = './_samples/MusyngKite/'

basenotes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
octavemap = [
    ',,,,', 
    ',,,,,', 
    ',,,,',
    ',,,',
    ',,',
    ',',
    '',
    '',
    '\''
]

note2abc = {}

for octave in range(8):
    for n in basenotes:
        abcn = n.replace('b', '_');
        if (octave <= 6):
            abcn = abcn.upper()
        else:
            abcn = abcn.lower()
        
        note2abc[n + str(octave)] = abcn + octavemap[octave]

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