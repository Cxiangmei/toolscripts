# encoding:utf-8

import arcpy
import os

file_dir = arcpy.GetParameterAsText(0)
for root, databases, dirs in os.walk(file_dir):
	for database in databases:
		if database is not None:
			area_code = database[database.rindex("_") + 1:database.rindex(".")]
			file_name = database[:database.rindex(".")]
			file_name = os.path.join(root, file_name) + ".txt"
			database = os.path.join(root, database)
			check_file = open(file_name, "a+")
			check_file.writelines( "\n" + database + "\n")
			check_file.close()
			list_dataset = ["HydDataset", "LcrDataset", "TraDataset"]
			area_code_name = "FEATID"
			for dataset in list_dataset:
				check_file = open(file_name, "a+")
				check_file.writelines(" " + dataset + "\n")
				check_file.close()
				workspace = database + "\\" + dataset
				arcpy.env.workspace = workspace
				list_lyr = arcpy.ListFeatureClasses()
				if list_lyr is None:
					continue
				for lyr in list_lyr:
					check_file = open(file_name, "a+")
					check_file.writelines("     " + lyr + "\n")
					check_file.close()
					list_fea = arcpy.da.SearchCursor(lyr, ["OBJECTID", area_code_name])
					if list_fea is None:
						continue
					try:
						for fea in list_fea:
							txt_content = ""
							if fea[1] is None:
								txt_content = "       OBJECTID " + str(fea[0]) + " is None" + "\n"
							else:
								str_FEATID = str(fea[1])
								if len(str_FEATID) < 7:
									txt_content = "       OBJECTID " + str(fea[0]) + " FEATID = " + str_FEATID+ "\n"
								else:
									featid_6 = str_FEATID[0, 5]
									if featid_6 != area_code:
										txt_content = "       OBJECTID " + str(fea[0]) + " FEATID = " + str_FEATID+ "\n"
							if txt_content != "":
								check_file = open(file_name, "a+")
								check_file.writelines(txt_content)
								check_file.close()
					except:
						continue

