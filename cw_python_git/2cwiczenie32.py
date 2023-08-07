#zwróæ wycinek od pierwszego znaku do pierwszej kropki.Dwa sposoby

x='D³ugo na szturm i szaniec pogl¹da³ w milczeniu.Na koniec rzek³: \
"Stracona".'

# 1 sposób w postaci dzielenia na kropkach ,pobranie pierwszej czêœci i dodania
# kropki w konkatencji

y=x.split('.')


print(y[0]+'.')

# 2 sposób w postaci pobrania wycinka ³añcucha

print(x[:47])

