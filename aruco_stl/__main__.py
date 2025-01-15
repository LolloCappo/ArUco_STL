from aruco import create_aruco_marker
from stl_utils import marker_to_stl
import cv2

##############################################
ID = 7
filename = 'marker_7.stl'
dictionary = cv2.aruco.DICT_ARUCO_ORIGINAL
thickness = 1
size = 20

##############################################

# Create an ArUco marker
aruco_dict = cv2.aruco.getPredefinedDictionary(dictionary)
marker = create_aruco_marker(aruco_dict, marker_id=ID, marker_size=size)
# Convert the marker to STL
marker_to_stl(marker, filename, thickness=thickness)