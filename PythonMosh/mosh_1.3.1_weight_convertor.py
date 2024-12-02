# CONVERTOR 1
# Uloží váhu uživatele(v librách) a převede na float
print('-------CONVERTOR 1---------')
weight_pnd = float(input('Zadejte Vaši váhu (v librách)'))


# Převede váhu uživatele na kilogramy
weight_kg = weight_pnd * 0.45359237


# Vypíše váhu v kilogramech
print(weight_kg)
print('--------------------------')




# CONVERTOR 2
# Zeptá zda budeme převádět z liber nebo z kilogramů
print('-------CONVERTOR 2---------')

jednotky = input('Pro převod z kg na libry napište "pnd", v opačném případě napište "kg": ')


# Uloží váhu uživatele a převede na float
vaha = int(input('Zadejte váhu: '))


# Převede váhu uživatele do požadované jednotky
vysledek = 0
if jednotky == 'pnd':
    vysledek = vaha * 2.20462262

if jednotky == 'kg':
    vysledek = vaha * 0.45359237


# Napíše výsledek
if jednotky == 'pnd':
    print(vaha, ' kilogramů je ', vysledek, ' liber')

if jednotky == 'kg':
    print(vaha, ' liber je ', vysledek, ' kilogramů')