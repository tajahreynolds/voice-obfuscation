import os, sys, librosa, shutil, time, random, math
from pydub import AudioSegment
import soundfile as sf  

def remove_json():
    listdir=os.listdir()
    for i in range(len(listdir)):
        if listdir[i][-5:]=='.json':
            os.remove(listdir[i])
            
def convert_audio():
    listdir=os.listdir()
    for i in range(len(listdir)):
        if listdir[i][-4:]!='.wav':
            os.system('ffmpeg -i %s %s'%(listdir[i], listdir[i][0:-4]+'.wav'))
            os.remove(listdir[i])

def obfuscate_dataset(filename, opusdir, curdir):

    def normalize_pitch(filename):
        '''
        takes in an audio file and outputs files normalized to 
        different pitches. This corrects for gender ane time-of-day differences.

        where gives the pitch shift as positive or negative ‘cents’ (i.e. 100ths of a semitone). 
        There are 12 semitones to an octave, so that would mean ±1200 as a parameter.
        '''
        filenames=list()

        basefile=filename[0:-4]

        # pitch down random
        pitchDown = random.randint(-800, -400)
        os.system('sox %s %s pitch %s'%(filename, basefile+'_freq_1.wav', pitchDown))
        filenames.append(basefile+'_freq_one.wav')
        #print('basefile %s pitched down %s\n'%(basefile,pitchDown))

        # pitch up random
        pitchUp = random.randint(200, 400)
        os.system('sox %s %s pitch %s'%(filename, basefile+'_freq_2.wav', pitchUp))
        filenames.append(basefile+'_freq_two.wav')
        #print('basefile %s pitched up %s\n'%(basefile,pitchUp))

        return filenames
    
    _1=normalize_pitch(filename)

    obfuscated_filenames=_1

    return obfuscated_filenames

## augment by 'python3 obfuscate.py [folderpath]
## '/Users/tjrey/Documents/dev/voice-obfuscation/audio'
opusdir=os.getcwd()+'/opustools'
directory=sys.argv[1]
curdir=os.getcwd()
os.chdir(directory)
remove_json()
convert_audio()
time.sleep(5)
listdir=os.listdir()
wavfiles=list()

for i in range(len(listdir)):
    if listdir[i][-4:] in ['.wav']:
        new_name=listdir[i].replace(' ','_')
        os.rename(listdir[i],new_name)
        wavfiles.append(new_name)

print(wavfiles)

obfuscated_files=list()

for i in range(len(wavfiles)):
    try:
        print(os.getcwd())
        obfuscated_files=obfuscate_dataset(wavfiles[i], opusdir, curdir)
        print(obfuscated_files)
        #sort(wavfiles[i],obfuscated_files,directory)
        #print(obfuscated_files) 
    except:
        print('error')

print('obfuscated dataset with %s files'%(str(len(obfuscated_files))))