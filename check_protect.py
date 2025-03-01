from functions_rezv import *
from tqdm import tqdm
import xarray as xr


polygons = file_to_polygons('All_OPZ_2019_topo.shp')# получение списка полигонов из файла Resrv_ALL.shp
polygon = polygons[0]#записываем в переменную polygon один из списка полигонов


Bbox = poly_to_bbox(polygon)#получение bbox из полигона
chunks = split_bbox(Bbox)[0]#разделение bbox на сетку (получаем список чанков)
columns = split_bbox(Bbox)[1]#получаем список долгот чанков
rows = split_bbox(Bbox)[2]#получаем список широт чанков


data = []# основа матрицы
data_row = []#строка матрицы
gdf = gpd.read_file('All_OPZ_2019_topo.shp')#открываем файл

for i in tqdm(range(len(chunks))):
    chunk = chunks[i]#записываем в chunk один из чанков
    poly = chunk_to_poly(chunk)#приводим к виду полигона
    for index, row in gdf.iterrows():#проходимся по файлу
        value = 0#возвращаемое значение
        if row['geometry'].contains(poly):#если находим заданный чанк в файле меняем value на 1
            value = 1
            break
    data_row.append(value)#добавляем значение в строку матрицы
    if (i+1)%(len(columns))==0 and i!=0:#если строка матрицы завершена: добавляем ее в матрицу и создаем следующую
        data.append(data_row)
        data_row = []

#полученную матрицу переводим в xarray
dataframe = xr.DataArray(data, coords=[rows, columns], dims=['latitude', 'longitude'])
print(dataframe)

