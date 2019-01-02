#encoding: utf-8


import arcpy
arcpy.env.workspace = r'D:/test/新建文件地理数据库.gdb/TraDataset'
ss = arcpy.ListFeatureClasses()
for i in ss:
    if i == "V_LRDL":
        ff = arcpy.da.UpdateCursor(i,["EC","ECP"])
        for f in ff:
            a=len(f[0])
            b=len(f[1])
            if a < 2:
                f[0]="/"
                ff.updateRow(f)
            if b < 2:
                f[1]="-"
                ff.updateRow(f)
    if i=="UV_LRDL":
        ff=arcpy.da.UpdateCursor(i,["EC","ECP"])
        for f in ff:
            a=len(f[0])
            b=len(f[1])
            if a>1:
                continue
            else:
                f[0]="/"
                ff.updateRow(f)
            if b>1:
                continue
            else:
                f[1]="-"
                ff.updateRow(f)
    else:
        ff=arcpy.da.UpdateCursor(i,["EC"])
        for f in ff:
            a=len(f[0])
            if a>1:
                continue
            else:
                f[0]="/"
                ff.updateRow(f)
print "JC17_530525.gdb"
