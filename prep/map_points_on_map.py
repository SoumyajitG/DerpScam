import cartopy
import matplotlib.pyplot as plt

def main():
    
    #define world map with cartopy
    ax = plt.axes(projection=cartopy.crs.PlateCarree())

    ax.add_feature(cartopy.feature.LAND)
    ax.add_feature(cartopy.feature.OCEAN)
    ax.add_feature(cartopy.feature.COASTLINE)
    ax.add_feature(cartopy.feature.BORDERS, linestyle=':')
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    ax.add_feature(cartopy.feature.RIVERS)
    
    #set bounding box for france (WESN)
    ax.set_extent([-5, 9.8, 41, 51.5])
    lat = []
    lon = []	
    data = open('../data/image_names.txt')

    # make a list of longitude,latitude for all data points
    for line in data:
        pt = line.split('_')
        slat,slong = pt[0:2]
        ilat = float(slat)
        ilong = float(slong)
        lat.append(ilat)
	lon.append(ilong)
        #count = count +1
       # if count>100:
        #    break
    plt.plot(lon,lat, 'r.' ,transform=cartopy.crs.PlateCarree())
     
    plt.show()
      # 

if __name__ == '__main__':
    main()
