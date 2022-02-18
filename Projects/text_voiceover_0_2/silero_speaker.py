
import pytesseract
import show_img as s
from options import  set_voise
from torch import device as torch_device,package,set_num_threads
from simpleaudio import WaveObject, stop_all


def say_silero():
    stop_all()  # остановить любой звук
    device = torch_device('cpu')
    set_num_threads(16)
    local_file = 'model_multi.pt'

    img = s.cv.imread("tesseract_mask.png")

    example_speakers = set_voise()
    sample_rate = 16000
    model = package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)
    print('silero mod :', example_speakers)

    config = r'--oem 3  --psm 4 tessedit_char_whitelist=абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    text = pytesseract.image_to_string(img, config=config, lang='rus')

    old_text = text

    try:
        audio_paths = model.save_wav(texts=text,
                                     speakers=example_speakers,
                                     sample_rate=sample_rate)

    except IndexError:
        return False
    audio_paths = model.save_wav(texts=text,
                                 speakers=example_speakers,
                                 sample_rate=sample_rate)

    wave_obj = WaveObject.from_wave_file('test_000.wav')
    play_obj = wave_obj.play()
    play_obj.wait_done()