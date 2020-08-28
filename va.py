#Importando la libreria Pandas
import pandas as pd

#Escribimos las data url para que no ocurra error al encontrar el archivo
DATA_URL = (
    "C:/Users/Calin/Desktop/mlintro-master/mlintro-master/01_cleancode/vinoejemplo/winequality-red.csv"
)
#Se carga la data set en el dataframe
df = pd.read_csv(DATA_URL, sep=';')
#Reemplazamos los espacios por guion bajo para no tener problemas con los nombres
df.columns = df.columns.str.replace(' ', '_')
#head se usa para tener una cierta cantidad de filas y cuando no se especifica se mostraran los primeros 5 datos
df.head(10)

#Cada bloque analiza su respectiva  columna, la primera linea saca la mediana y se almacena en ma
ma = df.alcohol.median()
for i, alcohol in enumerate(df.alcohol):
    if alcohol >= ma:
        df.loc[i, 'alcohol'] = 'alto'
    else:
        df.loc[i, 'alcohol'] = 'bajo'
df.groupby('alcohol').quality.mean()

#Cada bloque analiza su respectiva  columna en este caso , la primera linea saca la mediana y se almacena en ma
mpH = df.pH.median()
for i, pH in enumerate(df.pH):
    if pH >= mpH:
        df.loc[i, 'pH'] = 'alto'
    else:
        df.loc[i, 'pH'] = 'bajo'
df.groupby('pH').quality.mean()

#Cada bloque analiza su respectiva  columna en este caso , la primera linea saca la mediana y se almacena en ma
ma = df.residual_sugar.median()
for i, sugar in enumerate(df.residual_sugar):
    if sugar >= ma:
        df.loc[i, 'residual_sugar'] = 'alto'
    else:
        df.loc[i, 'residual_sugar'] = 'bajo'
df.groupby('residual_sugar').quality.mean()

#Cada bloque analiza su respectiva  columna en este caso , la primera linea saca la mediana y la almacena en ma
mca = df.citric_acid.median()
for i, citric_acid in enumerate(df.citric_acid):
    if citric_acid >= mca:
        df.loc[i, 'citric_acid'] = 'alto'
    else:
        df.loc[i, 'citric_acid'] = 'bajo'
df.groupby('citric_acid').quality.mean()