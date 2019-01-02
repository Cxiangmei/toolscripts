#encoding:utf-8

import arcpy as arc

file_name = arc.GetParameterAsText(0)
arc.env.workspace = file_name + r'\TraDataset'
fclist = arc.ListFeatureClasses()
for fc in fclist:
    if fc == "V_LRDL":
        update_cusor = arc.da.UpdateCursor(fc, ["EC", "ECP"])
        for fea in update_cusor:
            if fea[0] is None or len(fea[0]) < 2:
                fea[0] = "/"
                update_cusor.updateRow(fea)

            if fea[1] is None or len(fea[1]) < 2:
                fea[1] = "-"
                update_cusor.updateRow(fea)



        # if fc == "UV_LRDL":
        #     update_cusor = arc.da.UpdateCursor(fc,["EC","ECP"])
        #     for fea in update_cusor:
        #         attr_EC = len(fea[0])
        #         attr_ECP = len(fea[1])
        #         if attr_EC > 1:
        #             continue
        #         else:
        #             fea[0] = "/"
        #             update_cusor.updateRow(fea)
        #         if attr_ECP > 1:
        #             continue
        #         else:
        #             fea[1] = "-"
        #             update_cusor.updateRow(fea)
        # else:
        #     update_cusor = arc.da.UpdateCursor(fc,["EC"])
        #     for fea in update_cusor:
        #         attr_EC = len(fea[0])
        #         if attr_EC > 1:
        #             continue
        #         else:
        #             fea[0]="/"
        #             update_cusor.updateRow(fea)

