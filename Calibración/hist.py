import matplotlib.pyplot as plot
import seaborn as sb
import pandas as pd

cam = '10'
errores = pd.read_json('errors'+cam+'_vect.json')
print(errores.describe())
 


sb.displot(errores.astype('float'), color='#F2AB6D',bins=100, kde=True) #creamos el gráfico en Seaborn

#configuramos en Matplotlib
plot.xlabel("Error de reproyección")
plot.ylabel("Frecuencia")
plot.title('Histograma del error de reproyección - Camara N°1')
plot.subplots_adjust(left=None, bottom=0.1, right=None, top=0.9, wspace=None, hspace=None)
plot.savefig('HIST_CAM'+cam+'.png')
plot.show()

