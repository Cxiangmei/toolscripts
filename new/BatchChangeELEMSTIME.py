# encoding:utf-8

import arcpy
import os

file_dir = arcpy.GetParameterAsText(0)

for root, databases, dirs in os.walk(file_dir):
    for database in databases:
        if database is not None:
            database = os.path.join(root, database)
            list_dataset = ["HydDataset", "LcrDataset", "TraDataset"]
            area_code = arcpy.GetParameterAsText(1)
            area_code_name = "ELEMSTIME"
            for dataset in list_dataset:
                workspace = database + "\\" + dataset
                arcpy.env.workspace = workspace
                list_lyr = arcpy.ListFeatureClasses()
                if list_lyr is None:
                    continue
                for lyr in list_lyr:
                    list_field = arcpy.ListFields(lyr)
                    try:
                        list_fea = arcpy.da.UpdateCursor(lyr, [area_code_name])
                        if list_fea is None:
                            continue
                        for fea in list_fea:
                            fea[0] = area_code
                            list_fea.updateRow(fea)
                    except:
                        continue