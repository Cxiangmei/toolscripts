#encoding:utf-8

import arcpy

gdb = arcpy.GetParameterAsText(0)
lyr_names = ["UV_LVLL","UV_LCTL"]
for lyr_name in lyr_names:
    workspace = r'\TraDataset'+"\\" + lyr_name
    if lyr_name == "UV_LCTL":
        update_cursor = arcpy.da.UpdateCursor(workspace, ["OBJECTID","EC"])
        for fea in update_cursor:
            if fea[1] is None:
                arcpy.AddMessage(str(lyr_name + " OBJECTID " + fea[0]) + " is None ")
            elif fea[1] == "/" or fea[1][0] == "E" or fea[1][0] == "M" or fea[1][0] == "C" or fea[1][0] == "L" or fea[1][0] == "U" or fea[1][0] == "T":
                continue
            else:
                arcpy.AddMessage(lyr_name + " OBJECTID " + str(fea[0] + " is Error"))

    if lyr_name == "UV_LVLL":
        update_cursor = arcpy.da.UpdateCursor(workspace,["OBJECTID","EC"])
        for fea in update_cursor:
            if fea[1] is None:
                arcpy.AddMessage(lyr_name + " OBJECTID " + str(fea[0]) + " is None")
            elif fea[1] == "/" or fea[1][0] == "R":
                continue
            else:
                arcpy.AddMessage(lyr_name + " OBJECTID " + str(fea[0]) + " is Error")