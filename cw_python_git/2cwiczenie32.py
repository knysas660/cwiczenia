#zwr�� wycinek od pierwszego znaku do pierwszej kropki.Dwa sposoby

x='D�ugo na szturm i szaniec pogl�da� w milczeniu.Na koniec rzek�: \
"Stracona".'

# 1 spos�b w postaci dzielenia na kropkach ,pobranie pierwszej cz�ci i dodania
# kropki w konkatencji

y=x.split('.')


print(y[0]+'.')

# 2 spos�b w postaci pobrania wycinka �a�cucha

print(x[:47])

