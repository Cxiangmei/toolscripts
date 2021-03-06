#encoding:utf-8

import arcpy

lyr_names = ["UV_LVLL","UV_LCTL"]
for lyr_name in lyr_names:
    arcpy.env.workspace = r'D:\test\新建文件地理数据库.gdb\TraDataset'+"\\"+ lyr_name
    workspace = arcpy.env.workspace
    try:
        search_cursor = arcpy.da.SearchCursor(workspace, "EC")
        errors = {}
        cnt_errors = 0
        for fea in search_cursor:
            if fea[0] is None:
                cnt_errors = cnt_errors + 1
            elif len(fea[0]) == 1 or len(fea[0]) == 13:
                continue
            else:
                cnt_errors = cnt_errors + 1
        if cnt_errors > 0:
            print(lyr_name + " contains errors......" + str(cnt_errors))
    except:
        print("no layer " + lyr_name)
    finally:
        print("Hello")

