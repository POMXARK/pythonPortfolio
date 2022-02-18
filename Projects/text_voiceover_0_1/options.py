import random
import voise as v

#v.voice() # раскоментировать ,чтобы посмотреть имеющиеся голоса (голосовой движок)

with open('options.txt') as f:
    options  = f.read().splitlines()

#print('ФАЙЛ НАСТРОЕК :', options)

print('options',options[1])

### БЛОК НАСТРОЕК ###


voise_name = options[1] # Попробовать установить предпочтительный голос

print('voise_name :',voise_name)

#print('OPT :',options[3],options[4])

random_rate = random.uniform(float(options[3]),float(options[4])) # Скорость произношения
if voise_name == options[1]:
    random_rate *= random_rate
#print('OPT :', options[6], options[7])
vol = random.uniform(float(options[6]),float(options[7])) # Громкость голоса
#print('OPT :', options[9])
timer = int(options[9]) # время повтора реплики

### БЛОК НАСТРОЕК ###