# functions_rezv.py
- Модуль с функциями:
## file_to_polygons - Возвращает список полигонов из файла file_name. 
## poly_to_bbox - Для заданного polygon возвращает описанный прямоугольник bbox.
## chunk_to_poly - Превращяет bbox ([min_lon, min_lat, max_lon, max_lat]) в полигон ([(lon, lat), (lon, lat), (lon, lat), (lon, lat)]).
## split_bbox - Разделяет bounding box (bbox) на более мелкие чанки.
# check_rezv, check_protect, check_lesnichestva 
- Скрипты выгрузки соответсвующих xarray.
### Преобразование полигона:
## polygons - Список полигонов. type: list 
## polygon - Выбранный полигон. type: Polygon
## Bbox - Описаный около polygon прямоугольник. type: list
## chunks - Список чанков(частей) Bbox. type:list
## columns - Список долгот чанков. type:list
## rows - Список широт чанков. type:list
### Итерирование
## data - Матрица. type: list
## data_row - Строка матрицы. type: list
## gdf - class 'module'
## poly - Polygon
### Выгрузка
## dataframe - <class 'xarray.core.dataarray.DataArray'> 

