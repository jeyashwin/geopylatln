import pandas as pd
import numpy as np 


def haversine_distance(lat1, lon1, lat2, lon2):
   r = 6371
   phi1 = np.radians(lat1)
   phi2 = np.radians(lat2)
   delta_phi = np.radians(lat2 — lat1)
   delta_lambda = np.radians(lon2 — lon1)
   a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) *   np.sin(delta_lambda / 2)**2
   res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 — a)))
   return np.round(res, 2)

start_lat, start_lon = 40.6976637, -74.1197643

cities = pd.DataFrame(data={
   'City': ['Denver', 'Miami', 'Chicago'],
   'Lat' : [39.7645187, 25.7825453, 41.8339037],
   'Lon' : [-104.9951948, -80.2994985, -87.8720471]
})

distances_km = []
for row in cities.itertuples(index=False):
   distances_km.append(
       haversine_distance(start_lat, start_lon, row.Lat, row.Lon)
   )

cities['DistanceFromNY'] = distances_km