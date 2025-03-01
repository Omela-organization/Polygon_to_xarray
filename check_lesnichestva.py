from dask.dataframe.io.demo import names

from functions_rezv import *
from tqdm import tqdm
import xarray as xr


polygons = file_to_polygons('Lesnichestva PK.shp')# получение списка полигонов из файла Resrv_ALL.shp
for i in polygons:
    print(type(i))
polygon = polygons[1]#записываем в переменную polygon один из списка полигонов


Bbox = poly_to_bbox(polygon)#получение bbox из полигона
chunks = split_bbox(Bbox)[0]#разделение bbox на сетку (получаем список чанков)
columns = split_bbox(Bbox)[1]#получаем список долгот чанков
rows = split_bbox(Bbox)[2]#получаем список широт чанков

names_LV = {}
data = []# основа матрицы
data_row = []#строка матрицы
gdf = gpd.read_file('Lesnichestva PK.shp')#открываем файл
column = gdf.columns.tolist()
for index,row in gdf.iterrows():
    names_LV[row["NAME_LV"]] = index+1
print(names_LV)

for i in tqdm(range(len(chunks))):
    chunk = chunks[i]#записываем в chunk один из чанков
    poly = chunk_to_poly(chunk)#приводим к виду полигона
    for index, row in gdf.iterrows():#проходимся по файлу
        value = 0#возвращаемое значение
        if row['geometry'].contains(poly):#если находим заданный чанк в файле меняем value на 1
            value = names_LV[row['NAME_LV']]
            break
    data_row.append(value)#добавляем значение в строку матрицы
    if (i+1)%(len(columns))==0 and i!=0:#если строка матрицы завершена: добавляем ее в матрицу и создаем следующую
        data.append(data_row)
        data_row = []

#полученную матрицу переводим в xarray
for i in data:
    print(i)
dataframe = xr.DataArray(data, coords=[rows, columns], dims=['latitude', 'longitude'])
print(dataframe)