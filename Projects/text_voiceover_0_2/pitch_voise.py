from pydub import AudioSegment
from pydub.playback import play
import random
import simpleaudio as sa
import os
import Say as s



def pitch_voise():


    try_wav = os.path.getsize("text.wav") # проверка голосового файла

    if try_wav < 50 or s.say() == False:
        #print(try_wav,'Звука НЕТ')
        return False


    sound = AudioSegment.from_file('text.wav', format="wav")

    # сдвинуть высоту тона на половину октавы (скорость увеличится пропорционально)
    octaves = random.uniform(-0.2,-0.1)

    new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))

    # сохраните те же образцы, но скажите компьютеру, что в них следует играть
    # новый, более высокая частота дискретизации. Этот файл похож на бурундука, но имеет странную частоту дискретизации.
    hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

    # теперь мы просто преобразуем его в обычную частоту дискретизации (44,1k - стандартный аудио CD) в
    # убедитесь, что он работает в обычных аудиоплеерах. Кроме потенциально потери качества звука (если
    # вы установили слишком низкое значение - 44,1k вполне достаточно) теперь это должно заметно изменить звучание звука.
    hipitch_sound = hipitch_sound.set_frame_rate(44100)

    #export / save звук изменен.
    hipitch_sound.export("out.wav", format="wav")

    # Play Pitch изменил звук

    #play(hipitch_sound)

    sa.stop_all()
    wave_obj = sa.WaveObject.from_wave_file('out.wav')
    play_obj = wave_obj.play()
    #play_obj.wait_done() # приостанавливает GUI

#pitch_voise()