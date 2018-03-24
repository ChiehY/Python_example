
from netCDF4 import Dataset
import json
def round100(x):
    return round(x*100)/100


def ncdump(nc_fid, verb=True):
    def print_ncattr(key):
        try:
            #print("\t\ttype:", repr(nc_fid.variables[key].dtype))
            for ncattr in nc_fid.variables[key].ncattrs():
                #print('\t\t%s:' % ncattr, \
                      repr(nc_fid.variables[key].getncattr(ncattr)))
        except KeyError:
            #print("\t\tWARNING: %s does not contain variable attributes" % key)

    # NetCDF global attributes
    nc_attrs = nc_fid.ncattrs()
    if verb:
        #print("NetCDF Global Attributes:")
        for nc_attr in nc_attrs:
            #print('\t%s:' % nc_attr, repr(nc_fid.getncattr(nc_attr)))
    nc_dims = [dim for dim in nc_fid.dimensions]  # list of nc dimensions
    # Dimension shape information.
    if verb:
        #print("NetCDF dimension information:")
        for dim in nc_dims:
            #print("\tName:", dim)
            #print("\t\tsize:", len(nc_fid.dimensions[dim]))
            #print_ncattr(dim)
    # Variable information.
    nc_vars = [var for var in nc_fid.variables]  # list of nc variables
    if verb:
        #print("NetCDF variable information:")
        for var in nc_vars:
            if var not in nc_dims:
                #print('\tName:', var)
                #print("\t\tdimensions:", nc_fid.variables[var].dimensions)
                #print("\t\tsize:", nc_fid.variables[var].size)
                #print_ncattr(var)
    return nc_attrs, nc_dims, nc_vars


def getOJ(rf):
    root = Dataset(rf, "r")
    ncAttrs, ncDims, ncVars = ncdump(root)#, False)

    info = {}
    for PSFC in ncVars:
        if PSFC not in ncDims:
            info['name'] = PSFC
    pscf = root.variables['PSFC'][:]
    lats = root.variables['XLAT'][:]
    lons = root.variables['XLONG'][:]
#   time = root.variables['Times'][:]
    data = root.variables['PSFC'][:]
    dic = {"header":
        {
            "psfc":True,
            "nx":308,
            "ny":234,
            "basicAngle":0,
            "subDivisions":0,
            "lo1":float(lons.min()),
            "la1":float(lats.min()),
            "lo2":float(lons.max()),
            "la2":float(lats.max()),
            "dx":(lats.max()-lats.min())/308,
            "dy":(lons.max()-lons.min())/234,
            "numberPoints":72072,
            "centerName":"PSFC",
            "center":40
        },
        "data":[]
    }
    time_idx = 0
    oj = dic.copy()

    for lat in range(0,234,2):
        for lon in range(0,308,2):
            oj["data"] += [round100(data[time_idx, lat, lon])]
    return oj

oju = getOJ(r"nc_path")
json.dump(oju,open("save_json_path","w"),sort_keys=True, indent=2)