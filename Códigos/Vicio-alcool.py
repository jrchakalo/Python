import numpy as np
import matplotlib.pyplot as plt
total = np.array((65943))
adulto = np.array((2209))
adolescente = np.array((119))

barWidth = 0.50

x = ['Total x Adulto x Adolescente']

plt.figure(figsize=(10,5))

plt.bar(x, total, color='#6A5ACD', label = '*Total', bottom = adulto + adolescente)
plt.bar(x, adulto, color='#6495ED',  label = 'Adulto', bottom = adolescente)
plt.bar(x, adolescente, color='#00BFFF',  label = 'Adolescente')

plt.xticks(x)
plt.xlabel('Comparação', color='red')
plt.ylabel('Número de Indivíduos(x1000)', color='red')
plt.title('Total de consumidores de bebidas alcoólicas x\n Adultos viciados em alcoól x\n Adolescentes viciados em alcoól - Brasil, 2015')

plt.legend()
plt.show()


