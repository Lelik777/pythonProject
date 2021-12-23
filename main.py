a = int(input('Введите ваш рост: '))
x = int(input('Введите ваш вес: '))
b = input('Введите ваш пол (М/Ж): ')

if b == 'М':
  weight = a * 0.712 - 58
  print(weight)
  print('Ваш вес должен быть скорректирован на ' + str(weight - x) + ' кг')
elif b == 'Ж':
 weight = a * 0.624 - 48.9
 print(weight)
 print('Ваш вес должен быть скорректирован на ' + str(weight - x) + ' кг')
else:
 print('FALSE')

