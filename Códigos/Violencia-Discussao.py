import numpy as np
import matplotlib.pyplot as plt
total = [4448, 565]
adulto = [4022, 462]
adol = [426, 103]
barra = [12133, 2421312, 33245]
dez8 = np.array((0, 170))
vinte5 = np.array((1239, 0))

barWidth = 0.25

plt.figure(figsize=(10,5))

r1 = np.arange(len(total))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.bar(r1, total, color='#6A5ACD', width=barWidth, label = 'No total')
plt.bar(r2, adulto, color='#6495ED', width=barWidth, label = 'Adultos')
plt.bar(r3, adol, color='#00BFFF', width=barWidth, label = 'Adolescentes')
plt.bar(r2, dez8, color='red', width=barWidth, label = '18 a 24 anos')
plt.bar(r2, vinte5, color='gold', width=barWidth, label = '25 a 34 anos')

plt.xlabel('Tipo de Influência', color='red')
plt.xticks([r + barWidth for r in range(len(total))], ['Sobre a influência de alcoól', 'Sobre a influência de drogas'])
plt.ylabel('Número de Indivíduos(x1000)', color='red')
plt.title('Número de indivíduos que afirmam ter entrado em discussões por tipo de influência - Brasil, 2015')

plt.legend()
plt.show()


