import numpy as np
import matplotlib.pyplot as plt
dirigindo = [11500, 604]
envolvido = [1060, 47]
maior = np.array((3774, 0))

barWidth = 0.40

plt.figure(figsize=(10,5))

r1 = np.arange(len(dirigindo))
r2 = [x + barWidth for x in r1]

plt.bar(r1, dirigindo, color='#6A5ACD', width=barWidth, label = 'Alcool')
plt.bar(r2, envolvido, color='#6495ED', width=barWidth, label = 'Maconha')
plt.bar(r1, maior, color='gold', width=barWidth, label = '25 a 34 anos')

plt.xlabel('Comparação', color='red')
plt.xticks([r + barWidth for r in range(len(dirigindo))], ['Dirigindo', 'Envolvido em acidente'])
plt.ylabel('Número de Indivíduos(x1000)', color='red')
plt.title('Número de indivíduos que dirigiram ou\n se envolveram em acidentes Embregados X Drogados- Brasil, 2015')

plt.legend()
plt.show()

