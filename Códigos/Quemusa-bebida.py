import numpy as np
import matplotlib.pyplot as plt
total = [101615, 65943, 46036]
adulto = [94664, 61433, 44252]
adol = [6951, 4510, 1784]
vinte5 = np.array((0, 0, 12102))
dez8 = np.array((0, 0, 7832))

barWidth = 0.25

plt.figure(figsize=(10,5))

r1 = np.arange(len(total))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.bar(r1, total, color='#6A5ACD', width=barWidth, label = 'No total')
plt.bar(r2, adulto, color='#6495ED', width=barWidth, label = 'Adultos')
plt.bar(r3, adol, color='#00BFFF', width=barWidth, label = 'Adolescentes')
plt.bar(r2, vinte5, color='gold', width=barWidth, label ='25 a 34 anos')
plt.bar(r2, dez8, color='red', width=barWidth, label ='18 a 24 anos')



plt.xlabel('Época de Consumo', color='red')
plt.xticks([r + barWidth for r in range(len(total))], ['Na vida', 'Doze Meses', 'Trinta Dias'])
plt.ylabel('Número de Indivíduos(x1000)', color='red')
plt.title('Número de indivíduos que consumiram bebidas alcoólicas por época - Brasil, 2015')

plt.legend()
plt.show()


