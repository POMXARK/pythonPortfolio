import random
#from voise import voice
#voice() # раскоментировать ,чтобы посмотреть имеющиеся голоса (голосовой движок)


def set_voise():
    voise_name = open('voise.txt') # открыть файл
    voise_name = voise_name.read() # прочитать
    #print(voise_name)
    return voise_name



speakers = ['aidar', 'baya', 'kseniya', 'irina', 'ruslan', 'natasha',
            'thorsten', 'tux', 'gilles', 'lj', 'dilyara']




    # voise_name = opt_1["Голос"] # Попробовать установить предпочтительный голос
def set_opt():
    try:
        opt = open('opt.txt')  # открыть файл
        opt = opt.read()  # прочитать
        with open(opt) as f:
            options = f.read().splitlines()
    except FileNotFoundError:
        options = []
    try:
        opt_1 = {#'Голос': voise_name,
             'Минималья скорость' : options[3],
             'Максимальная скорость': options[4],
             'Минимальная громкость': options[6],
            'Максимальная громкость': options[7],
            'Время повтора': options[9],
            'X': options[11],
            'Y' : options[12],
            'отсуп с краев экрана по ширине' : options[14],
            'высота' : options[16],
        'h1':options[19],
        's1': options[21],
        'v1': options[23],
        'h2': options[25],
        's2': options[27],
        'v2': options[29],
        'rgb1':options[31],
        'rgb2':options[32],
        'rgb3':options[33],
            'mb_h1': options[36],
            'mb_s1': options[38],
            'mb_v1': options[40],
            'mb_h2': options[42],
            'mb_s2': options[44],
            'mb_v2': options[46]}
    except IndexError:
        opt_1 = {#'Голос': voise_name,
             'Минималья скорость' : 0,
             'Максимальная скорость': 0,
             'Минимальная громкость': 0,
            'Максимальная громкость': 0,
            'Время повтора': 0,
            'X': 0,
            'Y' : 0,
            'отсуп с краев экрана по ширине' : 0,
            'высота' : 0,
        'h1':0,
        's1': 0,
        'v1': 0,
        'h2': 0,
        's2': 0,
        'v2': 0,
        'rgb1':0,
        'rgb2':0,
        'rgb3':0,
    'mb_h1': 0,
    'mb_s1': 0,
    'mb_v1': 0,
    'mb_h2': 0,
    'mb_s2': 0,
    'mb_v2': 0,}

    #print('Голос ' ,opt_1["Голос"])


    #print('ФАЙЛ НАСТРОЕК :', options)

    #print('options',opt_1)

    ### БЛОК НАСТРОЕК ###




    #print('voise_name :',voise_name)

    #print('OPT :',options[3],options[4])

    #random_rate = random.uniform(float(opt_1['Минималья скорость']),float(opt_1['Максимальная скорость'])) # Скорость произношения
    #if voise_name ==  opt_1["Голос"]:
    #random_rate *= random_rate
    #print('OPT :', options[6], options[7])
    #vol = random.uniform(float(opt_1['Минимальная громкость']),float(opt_1['Максимальная громкость'])) # Громкость голоса
    #print('OPT :', options[9])
    #timer = int(opt_1['Время повтора']) # время повтора реплики
    return opt_1
    ### БЛОК НАСТРОЕК ###

#print(set_opt()['Время повтора'])