print('الة حاسبة ')
a = int(input('ادخل رقم اولي: '))
x = input('ادخل العملية (+ - / *): ')
b = int(input('ادخل رقمي ثاني: '))

print('العملية هي:')

if x == '+':
    print(f"{a} + {b} = {a + b}")
elif x == '-':
    print(f"{a} - {b} = {a - b}")
elif x == '/':
    if b == 0:
        print('غير مسموح بالقسمة على صفر 🚫')
    else:
        print(f"{a} / {b} = {a / b}")
elif x == '*':
    print(f"{a} * {b} = {a * b}")
else:
    print('عملية غير صحيحة ❌')
