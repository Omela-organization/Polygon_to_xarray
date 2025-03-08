# functions_rezv.py
- Модуль с функциями:
## file_to_polygons - Возвращает список полигонов из файла file_name.
## poly_to_bbox - Для заданного polygon возвращает описанный прямоугольник bbox.
## chunk_to_poly - Превращяет bbox ([min_lon, min_lat, max_lon, max_lat]) в полигон ([(lon, lat), (lon, lat), (lon, lat), (lon, lat)]).
## split_bbox - Разделяет bounding box (bbox) на более мелкие чанки.
# check_rezv, check_protect, check_lesnichestva 
- Скрипты выгрузки соответсвующих xarray.
переменные:
## polygons - Список полигонов.
## polygon - Выбранный полигон.
## Bbox - Описаный около polygon прямоугольник.
## chunks - Список чанков(частей) Bbox.
## columns - Список долгот чанков.
## rows - Список широт чанков.
