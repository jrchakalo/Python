import numpy as np
import matplotlib.pyplot as plt
alcool = [2209, 119]
maconha = [426, 12]

barWidth = 0.40

plt.figure(figsize=(10,5))

r1 = np.arange(len(alcool))
r2 = [x + barWidth for x in r1]

plt.bar(r1, alcool, color='#6A5ACD', width=barWidth, label = 'Alcoól')
plt.bar(r2, maconha, color='#6495ED', width=barWidth, label = 'Maconha')

plt.xlabel('Categoria', color='red')
plt.xticks([r + barWidth for r in range(len(alcool))], ['Adultos Viciados', 'Adolescente Viciados'])
plt.ylabel('Número de Indivíduos(x1000)', color='red')
plt.title('Número de indivíduos viciados bebidas alcoólicas X Número de indivíduos\n viciados maconha(inclui skank e haxixe) por categoria - Brasil, 2015')

plt.legend()
plt.show()


