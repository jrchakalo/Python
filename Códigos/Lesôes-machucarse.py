import numpy as np
import matplotlib.pyplot as plt
total = [2059, 230]
adulto = [1961, 230]
adol = [98, 0]

barWidth = 0.25

plt.figure(figsize=(10,5))

r1 = np.arange(len(total))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.bar(r1, total, color='#6A5ACD', width=barWidth, label = 'No total')
plt.bar(r2, adulto, color='#6495ED', width=barWidth, label = 'Adultos')
plt.bar(r3, adol, color='#00BFFF', width=barWidth, label = 'Adolescentes')

plt.xlabel('Tipo de Influência', color='red')
plt.xticks([r + barWidth for r in range(len(total))], ['Sobre a influência de alcoól', 'Sobre a influência de drogas'])
plt.ylabel('Número de Indivíduos(x1000)', color='red')
plt.title('Número de indivíduos que afirmam ter se machucado por tipo de influência - Brasil, 2015')

plt.legend()
plt.show()


