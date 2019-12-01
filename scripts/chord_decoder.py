from music21 import *

def newMusicXMLFile(content, path):
    content.write('xml', fp = path+'.xml')

def chordDecoder(chordStr):
  minor = False
  diminished = False
  augmented = False
  seventh = False
  majSeventh = False
  bass = False

  root = note.Note(chordStr[0]+'4').pitch.midi

  if('/' in chordStr):
    chordParts = chordStr.split('/')
    chordStr = chordParts[0]
    bass = True
  if('m' in chordStr):
    minor = True
  if('dim' in chordStr):
    diminished = True
  if('+' in chordStr):
    augmented = True
  if(len(chordStr) > 1):
    if(chordStr[1] is '#'):
      root += 1
    if(chordStr[1] is 'b'):
      root -= 1
  if('7' in chordStr):
    if('7M' in chordStr):
      majSeventh = True
    else:
      seventh = True

  intervalVector = [0, 4, 7]

  if(seventh):
    intervalVector.append(10)
  if(majSeventh):
    intervalVector.append(11)
  if(minor or diminished):
    intervalVector[1] -= 1
    if(diminished):
      intervalVector[2] -= 1
  if(augmented):
    intervalVector[2] += 1

  finalVector = []

  for i in intervalVector:
    finalVector.append(i + root)

  resp = chord.Chord(finalVector)
  
  if(bass):
    newBass = pitch.Pitch(chordParts[1] + str(resp.bass().octave - 1))
    oldBass = pitch.Pitch(chordParts[1] + str(resp.bass().octave))
    chordPitches = list(resp.pitches)
    chordPitches.append(newBass)
    for i in chordPitches:
      if(i.nameWithOctave == oldBass.nameWithOctave):
        chordPitches.remove(i)
    resp.pitches = tuple(chordPitches)

  return resp

def decodificarCifra(string):
  cifra = string.split(' ')

  musica = stream.Stream()

  for i in cifra:
    musica.append(chordDecoder(i))
    musica.append(chordDecoder(i))

  return musica
