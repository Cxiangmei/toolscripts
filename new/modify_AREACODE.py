#encoding:utf-8

import arcpy

database = arcpy.GetParameterAsText(0)
list_dataset = ["HydDataset","LcrDataset","TraDataset"]
if database is not None:
    area_code = database[database.rindex("_") + 1 : database.rindex(".")]
    area_code_name = "AREACODE"
    for dataset in list_dataset:
        workspace = database + "\\" + dataset
        arcpy.env.workspace = workspace
        list_lyr = arcpy.ListFeatureClasses()
        if list_lyr is None:
            continue
        for lyr in list_lyr:
            list_field = arcpy.ListFields(lyr)
            # if area_code_name not in list_field:
            #     continue
            arcpy.ValidateFieldName(area_code_name)
            list_fea = arcpy.da.UpdateCursor(lyr,[area_code_name])
            if list_fea is None:
                continue
            try:
                for fea in list_fea:
                    if fea[0] is None:
                        fea[0] = area_code
                    elif fea[0] != area_code:
                        fea[0] = area_code
                    list_fea.updateRow(fea)
            except:
                continue
