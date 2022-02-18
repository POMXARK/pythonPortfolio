from silero_speaker import say_silero
from options import  set_voise ,speakers
from voise import find_voice_noy_silero
from Say import say



def choice_of_voice_engine():
    no_silero = find_voice_noy_silero()
    voise = set_voise()

    for speaker in no_silero:
        if voise == speaker:
            say()

    for silero_speaker in speakers:
        if voise == silero_speaker:
            say_silero()
