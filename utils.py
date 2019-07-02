# utility functions
from pyresample.geometry import AreaDefinition

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script

def createResArea(area_ID:str,description:str,proj_id:str,proj_short:str,lon_0:int,lat_0:int,width:int,height:int,llC:int,urC:int):

    '''
    A function that let's you define an area object used to resample with satpy. 

    parameters:
    ---------------------
    areaID: String with a precise title of the defined area. 
    description: String with a more elborative description of the definend area   

    proj_id: String with the long name of the desired projection.

    proj_short: String with the short name of the desired projection.  

    lon_0: longitude value of the center of the position (integer) 

    lat_0: latitude value of the center of the position (integer)
    
    width/height: Number of pixels in height and width (integer)  

    llC: X and Y coordinate of the lower-left-Corner of the pixel (x and y must have equal values)   

    urC: X and Y coordinate of the upper-right-Corner of the pixel (")
    '''

    proj_dict = {"proj":proj_short,"lon_0":str(lon_0),"lat_0":str(lat_0)}
    llx = llC
    lly = llC
    urx = urC
    ury = urC
    area_extent = (llx,lly,urx,ury)
    area_def = AreaDefinition(area_ID, proj_id, description, proj_dict, width, height, area_extent)
    return(area_def)