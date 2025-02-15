import geopandas as gpd
from shapely.geometry import Point,Polygon
import numpy as np

def file_to_polygons(file_name:str):#возвращает список полигонов из файла
    gdf = gpd.read_file(file_name)
    polygons = []
    for index, row in gdf.iterrows():
        polygons.append(row['geometry'])
    return polygons

def poly_to_bbox(polygon) -> tuple:
    """
        принимает polygon
        возвращает bbox(прямоугольник описанный около polygon)
    """
    max_lat = 0
    max_lon = 0
    min_lon = float('inf')
    min_lat = float('inf')
    iters = polygon.exterior.coords
    for lon,lat in iters:
        if lon < min_lon:
            min_lon = lon
        if lon > max_lon:
            max_lon = lon
        if lat < min_lat:
            min_lat = lat
        if lat > max_lat:
            max_lat = lat
    return (min_lon, min_lat, max_lon, max_lat)


def chunk_to_poly(chunkk:list):#возвращает chunk в виде полигона
    """
        chunk изначально имеет вид [min_lon, min_lat, max_lon, max_lat] - списка сторон прямоугольника
        функция переводит в [(lon, lat), (lon, lat), (lon, lat), (lon, lat)] - список точек(вершин) прямоугольника
    """
    min_lon, min_lat, max_lon, max_lat = chunkk[0], chunkk[1], chunkk[2], chunkk[3]
    polygon = Polygon([(min_lon, min_lat), (max_lon, min_lat), (max_lon, max_lat), (min_lon, max_lat)])
    return polygon


def split_bbox(bbox, max_size=2500, resolution=10):
    """
    Разделяет bounding box (bbox) на более мелкие чанки

    Параметры:
    ----------
    bbox : list или tuple из 4 элементов
        [минимальная долгота, минимальная широта, максимальная долгота, максимальная широта].
    max_size : int
        Максимальный размер (в пикселях) по одной оси для одной «плитки».
    resolution : int
        Пространственное разрешение в метрах. По умолчанию 10 м.

    Возвращает:
    -----------
    chunks : list
        Список подпоследовательностей bbox вида [[min_lon, min_lat, max_lon, max_lat], ...].
    lon_splits[:-1]:
        Список долгот всех чанков
    lat_splits[:-1]:
        Список широт всех чанков
    """
    min_lon, min_lat, max_lon, max_lat = bbox

    # Определяем шаги разбиения по долготе и широте
    lon_step = (max_lon - min_lon) / (max_size / resolution)
    lat_step = (max_lat - min_lat) / (max_size / resolution)

    # Создаём последовательности разбиения
    lon_splits = list(np.arange(min_lon, max_lon, lon_step))
    lon_splits.append(max_lon)
    lat_splits = list(np.arange(min_lat, max_lat, lat_step))
    lat_splits.append(max_lat)
    chunks = []
    # Проходимся по всем полученным диапазонам и формируем списки координат
    for i in range(len(lat_splits) - 1):
        for j in range(len(lon_splits) - 1):
            chunks.append([
                lon_splits[j],
                lat_splits[i],
                lon_splits[j + 1],
                lat_splits[i + 1]
            ])
    return chunks,lon_splits[:-1],lat_splits[:-1]


