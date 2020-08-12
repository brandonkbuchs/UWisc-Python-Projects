import gdalconst, ogr, os, sys # Import necessary modules

def taskOne(fname):

    driver = ogr.GetDriverByName('ESRI Shapefile') # Get correct driver
    data_source = driver.Open(fname, gdalconst.GA_ReadOnly) # Open file

    # Test if the file is opened.
    if data_source is None:
        print 'Failed to open', fname, '.'
        sys.exit(1)
    else:
        print 'Success opening', fname, '.'

    # Obtain the information about the lines for prosecuting distance
    layer = data_source.GetLayer(0)
    feat = layer.GetNextFeature()
    line = feat.GetGeometryRef()
    num_pts = line.GetPointCount()

    # Calculate total distance of powerlines
    distance = 0
    for i in range(num_pts - 1):
        fi = line.GetPoint(i)
        xi = fi[0]
        yi = fi[1]
        fj = line.GetPoint(i+1)
        xj = fj[0]
        yj = fj[1]
        dij = ((xi - xj) ** 2 + (yi - yj) ** 2) ** 0.5
        distance = dij + distance

    distance = round(distance / 5280,2) #calculate distance in miles
    print 'The total distance of the powerlines is ', distance, 'miles'

    # Prove distance calculation is correct using geom length
    distance_proof = round(line.Length() / 5280,2)
    print 'The total distance of the powerline is ' ,distance_proof, \
    'As obtained from the Length() method.'

    # Close the file
    data_source.Destroy()
def taskTwo(fname):

    driver = ogr.GetDriverByName('ESRI Shapefile') # ESRI Driver

    data_source = driver.Open(fname, gdalconst.GA_ReadOnly) # Open file

    if data_source is None: # Error checking if file can open
        print 'Failed to open', fname, '.'
        sys.exit(1)
    else:
        print 'Success opening', fname, '.'

    layer = data_source.GetLayer(0)
    layer_name = layer.GetName()
    feature_define = layer.GetLayerDefn()
    field_count = feature_define.GetFieldCount() # get field count to establish attributes

    # Print all of the attribute names and types as well as widths and precisions.
    for i in range(0, field_count):
        field_def = feature_define.GetFieldDefn(i)
        fname = field_def.GetNameRef() # Name of attribute field
        ftype = field_def.GetType() # Type
        ftype_string = field_def.GetFieldTypeName(ftype) # Type converted to string

        values = (fname, ftype_string)
        fmt = '%s: %s'
        print fmt % values # Print attribute names and types.
    # Close the file
    data_source.Destroy()

def taskThree(fname1, fname2):
    # Open PowerLine.shp
    driver = ogr.GetDriverByName('ESRI Shapefile') # Driver
    data_source1 = driver.Open(fname1, gdalconst.GA_ReadOnly) # Open file

    if data_source1 is None: # Error checking
        print 'Failed to open', fname1, '.'
        sys.exit(1)
    else:
        print 'Success opening', fname1, '.'

    layer1 = data_source1.GetLayer(0)
    layer_name1 = layer1.GetName()
    feat1 = layer1.GetNextFeature()
    line = feat1.GetGeometryRef()

    # Open Parcels.shp

    data_source2 = driver.Open(fname2, gdalconst.GA_ReadOnly)

    if data_source2 is None: # Error checking
        print 'Failed to open', fname2, '.'
        sys.exit(1)
    else:
        print 'Success opening', fname2, '.'

    # Obtain layer information including field counts
    layer2 = data_source2.GetLayer(0)
    layer_name2 = layer2.GetName()
    feature_define2 = layer2.GetLayerDefn()
    field_count2 = feature_define2.GetFieldCount()


    # Obtain feature count
    feature_count2 = layer2.GetFeatureCount()
    print 'The following parcels cross the proposed powerline construction.'
    n = 0 # For labeling each address
    for i in range(0,feature_count2): # Iterate through all features in the parcels shapefile
        feat = layer2.GetFeature(i)
        poly = feat.GetGeometryRef()
        if line.Crosses(poly) == True: # If the line crosses the polygon
            n += 1
            address = feat.GetField('SITUSADDR') # Obtain the features address
            area = feat.GetField('Area') / 43560 # Get area and square feet to acre conversion

            values = (n, address, area)
            fmt = '%d) Address: %s, Area: %.4f acres' # Print format
            print fmt % values


    # Close the files
    data_source1.Destroy()
    data_source2.Destroy()

def taskFour(fname1, output_file):

    # Set buffer width to 250 feet
    buffer_width = 250 # feet
    # Open the input file
    driver = ogr.GetDriverByName('ESRI Shapefile')

    input_ds = driver.Open(fname1) # Open file
    if input_ds is None:
        print 'Error opening', fname1, '.'
        sys.exit(1)
    else:
        print 'Successfully opened', fname1, '.'

    # Obtain layer information
    input_lyr = input_ds.GetLayer()
    extent = input_lyr.GetExtent()

    # Write to output File, if file exists delete existing file.
    if os.path.exists(output_file):
        os.remove(output_file)
    try:
        output_ds = driver.CreateDataSource(output_file)
    except:
        print 'Could not create output file', output_file
        sys.exit(1)
    SRS = input_lyr.GetSpatialRef() # Set SRS to input file.
    new_lyr = output_ds.CreateLayer('PowerLineBuffer', SRS, geom_type=ogr.wkbPolygon)
    if new_lyr is None:
        print 'Could not create layer for buffer in output DS.'
        sys.exit(1)

    new_lyr_def = new_lyr.GetLayerDefn()

    feature_id = 0
    old_feat = input_lyr.GetNextFeature()
    while old_feat: # Create as long as there is a feature to be obtained from input file.
        geometry = old_feat.GetGeometryRef()
        buffer = geometry.Buffer(buffer_width)
        try:
            new_feat = ogr.Feature(new_lyr_def)
            new_feat.SetGeometry(buffer)
            new_feat.SetFID(feature_id)
            new_lyr.CreateFeature(new_feat)
        except:
            print 'Error adding buffer.'

        new_feat.Destroy()
        old_feat.Destroy()

        old_feat = input_lyr.GetNextFeature()
        feature_id += 1

    print 'Buffered', feature_id, ' input features successfully.'

    # Close all files
    input_ds.Destroy()
    output_ds.Destroy()


# Start Task 1
pline_fname = ''
while pline_fname.endswith('.shp') == False:
    pline_fname = raw_input('Enter full path to Powerline shapefile here.> ')
taskOne(pline_fname)

# Start Task 2
parcel_fname = ''
while parcel_fname.endswith('.shp') == False:
    parcel_fname = raw_input('Enter full path to Parcels shapefile here.> ')
taskTwo(parcel_fname)

# Start Task 3
taskThree(pline_fname, parcel_fname)

# Start Task 4
buffer_fname = ''
while buffer_fname.endswith('.shp') == False:
    buffer_fname = raw_input('Enter the full path to the buffer shapefile you want to create.>')
taskFour(pline_fname, buffer_fname)