import sqlite3
import json
import gmplot

latitude=[]
longitude=[]
address=[]

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()


cur.execute('SELECT * FROM Locations')

for row in cur :
    data = str(row[1].decode())
    
    try:
        js = json.loads(str(data))
    except:
        continue

    if not('status' in js and js['status'] == 'OK') :
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue
    where = js['results'][0]['formatted_address']
    where = where.replace("'", "")
    
    if len(latitude)==0:
        cur_latitude = lat
        cur_longitude= lng
        gmap3 = gmplot.GoogleMapPlotter(cur_latitude, 
                                cur_longitude,12) 
    latitude.append(lat)
    longitude.append(lng)
    address.append(where)
cur.close()
print(latitude,longitude,address)

gmap3.scatter( latitude, longitude, 'red',
                              size = 40, marker = True)
    
gmap3.draw( "C:\\Users\\rajab\\Desktop\\map_1.html" )
print("Open map_1.html")
