from aruco import create_aruco_marker
from stl_utils import marker_to_stl
import cv2

##############################################
ID = 0
dictionary = cv2.aruco.DICT_ARUCO_ORIGINAL
thck = 1
filename = 'marker_0.stl'
##############################################

# Create an ArUco marker
aruco_dict = cv2.aruco.getPredefinedDictionary(dictionary)
marker = create_aruco_marker(aruco_dict, marker_id=ID)
# Convert the marker to STL
marker_to_stl(marker, filename, thickness=thck)