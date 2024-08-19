import requests
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

####### Municipio do Porto

# Abrir Ficheiro GeoJSON dos municipios de Portugal
# geojson_file = 'portugal_municipios.geojson'

# # Converter o GeoJSON em GeoDataFrame
# MunicipiosPortugal = gpd.read_file(geojson_file)

# # Extrair o municipio do Porto da tabela dos municipios portugueses
# Municipio_Porto = MunicipiosPortugal[MunicipiosPortugal['name_2'] == 'Porto']

# # Exportar o GeoDataFrame Monumentos_Porto_Final para um arquivo GeoJSON
# Municipio_Porto.to_file("Municipio_Porto.geojson", driver="GeoJSON")



####### MONUMENTOS

# url_monumentos = "https://opendata.porto.digital/api/3/action/datastore_search?resource_id=389a446c-8eaf-4406-b9ca-f1637c440de4"
# response_monumentos = requests.get(url_monumentos)
# data_monumentos = response_monumentos.json()

# # # Extrair os nós (nodes) da resposta JSON 
# nodes_monumentos = data_monumentos['result']['records']

# # # # Extrair informações relevantes e converter para GeoDataFrame
# monumentos = []
# for node in nodes_monumentos:
#          a=node['label'].find('value')
#          b=node['label'][a+9:].find("}")
#          c=node['category'].find('value')
#          d=node['category'][a+9:].find("}")
#          e=node['address'].find('WORK')
#          f=node['address'][e+9:].find(";")
#          g=node['description'].find('value')
#          h=node['description'][a+9:].find("}")
#          i=node['address'].find('Porto;Porto;')
#          j=node['address'][a+9:].find("}")
#          monumentos.append({
#              'Nome': node['label'][a+9:a+8+b],
#              'Categoria':node['category'][c+9:c-14+d],
#              'Codigo Postal':node['address'][i+12:i+21+j],
#              'Moradia':node['address'][e+9:e+49+f],
#              'Descriçao':node['description'][g+9:g+49+h],
#              'lat': node['latitude'], 
#              'lon': node['longitude'] 
#              })

# monumentos_df = pd.DataFrame(monumentos)      

# # Criar uma coluna de geometria a partir das coordenadas geodataframe
# monumentos_xy = gpd.GeoDataFrame(monumentos_df, geometry=gpd.points_from_xy(monumentos_df.lon, monumentos_df.lat))

# # Definir o sistema de coordenadas (CRS) para WGS 84 (EPSG:4326) 
# monumentos_xy.set_crs(epsg=4326, inplace=True)

# # Limpar os dados dos Monumentos para obter uma tabela resumida com informaçao mais importante
# Monumentos_Porto_Final = monumentos_xy[["Nome", "Categoria", "Codigo Postal", "Moradia", "Descriçao", "geometry"]]

# Exportar o GeoDataFrame Monumentos_Porto_Final para um arquivo GeoJSON
# Monumentos_Porto_Final.to_file("Monumentos_Porto_Final.geojson", driver="GeoJSON")


# Salvar o resultado do Spatial Join como Shapefile
# Monumentos_Porto_Final_toshp = r'F:\Turismo_Porto\SHP\Monumentos_Porto.shp'
# Monumentos_Porto_Final.to_file(Monumentos_Porto_Final_toshp, driver='ESRI Shapefile')



###### MUSEOS

# url_museos = "https://opendata.porto.digital/api/3/action/datastore_search?resource_id=08824bb1-b9ed-40ee-9b23-2ccebb962a92"
# response_museos = requests.get(url_museos)
# data_museos = response_museos.json()

# # Extrair os nós (nodes) da resposta JSON 
# nodes_museos = data_museos['result']['records']

# # Extrair informações relevantes e converter para GeoDataFrame

# museos = []
# for node in nodes_museos:
#          i=node['label'].find('value')
#          k=node['label'][i+9:].find("}")
#          h=node['category'].find('value')
#          j=node['category'][i+9:].find("}")
#          L=node['address'].find('WORK')
#          M=node['address'][L+9:].find(";")
#          N=node['description'].find('value')
#          S=node['description'][i+9:].find("}")
#          P=node['address'].find('Porto;Porto;')
#          R=node['address'][i+9:].find("}")
         
#          museos.append({
#              'Nome': node['label'][i+9:i+8+k],
#              'Categoria':node['category'][h+9:h+27+j],
#              'Codigo Postal':node['address'][P+12:P+21+R],
#              'Moradia':node['address'][L+9:L+49+M],
#              'Descriçao':node['description'][N+9:N+49+S],
#              'lat': node['latitude'], 
#              'lon': node['longitude'] 
#              })
# museos_df = pd.DataFrame(museos) 

# # Criar uma coluna de geometria a partir das coordenadas geodataframe
# museos_xy = gpd.GeoDataFrame(museos_df, geometry=gpd.points_from_xy(museos_df.lon, museos_df.lat))

# # Definir o sistema de coordenadas (CRS) para WGS 84 (EPSG:4326) 
# museos_xy.set_crs(epsg=4326, inplace=True)

# # Limpar os dados dos Museos para obter uma tabela resumida com informaçao mais importante
# Museos_Final = museos_xy[["Nome", "Categoria", "Codigo Postal", "Moradia", "Descriçao", "geometry"]]

# # Exportar o GeoDataFrame Museos_Final para um arquivo GeoJSON
# Museos_Final.to_file("Museos_Porto_Final.geojson", driver="GeoJSON")


###### TEATROS

url_teatros = "https://opendata.porto.digital/api/3/action/datastore_search?resource_id=d47f5fb5-2e7e-4498-a558-0c3af2d4dae0&q"
response_teatros = requests.get(url_teatros)
data_teatros = response_teatros.json()

# Extrair os nós (nodes) da resposta JSON 
nodes_teatros = data_teatros['result']['records']

# Extrair informações relevantes e converter para GeoDataFrame
teatros = []
for node in nodes_teatros:
    a=node['label'].find('value')
    b=node['label'][a+9:].find("}")
    c=node['category'].find('value')
    d=node['category'][a+9:].find("}")
    e=node['address'].find('WORK')
    g=node['address'][e+9:].find(";")
    h=node['description'].find('value')
    i=node['description'][a+9:].find("}")
    j=node['address'].find('Porto;Porto;')
    k=node['address'][a+9:].find("}")
    
    teatros.append({
        'Nome': node['label'][a+9:a+8+b],
        'Categoria': node['category'][c+9:c-14+d],
        'Codigo Postal':node['address'][j+12:j+21+k],
        'Moradia': node['address'][e+9:e+49+g],
        'Descriçao': node['description'][h+9:h+49+i],
        'lat': node['latitude'],
        'lon': node['longitude']
        })

teatros_df = pd.DataFrame(teatros) 

# Criar uma coluna de geometria a partir das coordenadas geodataframe
teatros_xy = gpd.GeoDataFrame(teatros_df, geometry=gpd.points_from_xy(teatros_df.lon, teatros_df.lat))

# Definir o sistema de coordenadas (CRS) para WGS 84 (EPSG:4326) 
teatros_xy.set_crs(epsg=4326, inplace=True)

# Limpar os dados dos Museos para obter uma tabela resumida com informaçao mais importante
Teatros_Final = teatros_xy[["Nome", "Categoria", "Codigo Postal", "Moradia", "Descriçao", "geometry"]]

# Exportar o GeoDataFrame Teatros_Final para um arquivo GeoJSON
Teatros_Final.to_file("Teatros_Porto_Final.geojson", driver="GeoJSON")


