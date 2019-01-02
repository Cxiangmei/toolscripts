# encoding:utf-8

import arcpy
import os
import random

def modify_point_line_info():
	line_lyr_name = ""
	point_lyr_name = ""
	point_fld = "NUM"
	line_fld_fst = "START"
	line_fld_end = "END"
	database = r'D:\python_files\testfolder\test2.gdb'
	arcpy.env.workspace = database
	for dataset in arcpy.ListDatasets():
		# arcpy.env.workspace = os.path.join(database, dataset)
		point_lyr = arcpy.ListFeatureClasses(point_lyr_name, feature_type="point", feature_dataset=dataset)
		line_lyr = arcpy.ListFeatureClasses(line_lyr_name, feature_type="line", feature_dataset=dataset)
		if point_lyr is None or line_lyr is None:
			return
		points = {}
		with arcpy.da.UpdateCursor(point_lyr[0], ["OBJECTID", point_fld, "SHAPE@"]) as point_cursor:
			if point_cursor is None:
				continue
			nums = []
			for row in point_cursor:
				if row[1]:
					nums.append(row[1])
				else:
					pass
				del row
			max_num = 1
			if nums:
				max_num = max(nums)
			point_cursor.reset()
			for fea in point_cursor:
				if not fea[1]:
					max_num += 1
					# fea[1] = max_num
					# point_cursor.updateRow(fea)
					points[fea[0]] = [max_num, fea[2]]
			del point_cursor

		with arcpy.da.UpdateCursor(line_lyr[0], ["OBJECTID", line_fld_end, line_fld_end, "SHAPE@"]) as line_cursor:
			for point_key in points.keys():
				point_geo = points[point_key][1]
				for line_fea in line_cursor:
					line_geo = line_fea[3]
					spatil_reference = line_geo.spatialReference
					if line_geo.contains(point_geo):
						print("line OBJECTID {0} point OBJECTID {1}".format(str(line_fea[0]), point_key))
						cutter = None
						pnt = point_geo.getPart()
						i = 0
						while i < 5:
							i += 1
							dis_x = random.random()
							dis_y = random.random()
							fea_points = [[pnt.X, pnt.Y],[pnt.X + dis_x, pnt.Y + dis_y]]
							cutter = arcpy.Polyline(arcpy.Array([arcpy.Point(*coords) for coords in fea_points]), spatil_reference)
							if not line_geo.contains(cutter):
								break
							else:
								cutter = None
						if cutter:

							lines = line_geo.cut(cutter)
							#lines = line_geo.cut(cutter)
							j = 0
							for line_cutted in lines:
								print("line {0}".format(str(j)))
								j += 1
						del line_fea
						break
					del line_fea



if __name__ == "__main__":
	modify_point_line_info()
