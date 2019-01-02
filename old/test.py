# encoding:utf-8
import arcpy
import os

def print_lyr():
	dir_name = r'D:\python_files\testdata'
	if arcpy.Exists(dir_name):
		arcpy.env.workspace = dir_name
		for mdb_file in arcpy.ListFiles("*.mdb"):
			print mdb_file
		for workspace in arcpy.ListWorkspaces("","filegdb"):
			print(workspace)
			arcpy.env.workspace = os.path.join(dir_name,workspace)
			for dataset in arcpy.ListDatasets("H*"):
				print(dataset)
				for lyr in arcpy.ListFeatureClasses(feature_dataset = dataset):
					lyr_info = arcpy.Describe(lyr)
					print(lyr_info.shapeType)
					if arcpy.Exists(lyr):
						print("OK")
					vld_fld = arcpy.ValidateFieldName("BJECTID",lyr)
					print(vld_fld)
					for field in arcpy.ListFields(lyr):
						print("{0} {1} {2}".format(field.name, field.type, field.length))
					for index in arcpy.ListIndexes(lyr):
						print("{0} {1} {2}".format(index.name, index.isAscending, index.isUnique))
					for field1 in index.fields:
						print(field1.name)

	else:
		print("workspace not exists")

if __name__ == "__main__":
	print_lyr()
