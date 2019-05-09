######################################
# setup variable for the application  
v_print_ver = 0
v_print_conf = 1
v_print_debug_msg = 1 
v_print_data_analysis = 1
# End setup variable for the application 
#########################################

#########################################
# Print config 
if v_print_conf == 1:
        print("\nVariable configuration parameters ")
        print('v_print_ver: {}' .format(v_print_ver))
        print('v_print_conf: {}' .format(v_print_conf))
        print('v_print_debug_msg: {}' .format(v_print_debug_msg))
        
#END Print config 
######################################
        
# Load libraries
try:
    if v_print_debug_msg == 1 :
        print('Msg: Import libraries')
    import sys
    import numpy    
    import matplotlib as plt
    import cv2
except ImportError:
    print('Error: Failed to load mudules')

# end import libraries 
#########################################
    
#########################################
#Print versions
if v_print_ver == 1 :
    print("\nVersions of all librries used in this application ")
    print('Python: {}'.format(sys.version))
    print('numpy: {}' .format(numpy.__version__))
    print('cv2: {}'.format(cv2.__version__))
    print('matplotlib: {}'.format(plt.__version__))
#end print versions
#########################################
    
img = cv2.imread('watch.jpg' , cv2.IMREAD_COLOR)

px = img[55,55]

img[55,55] = [255,255,255]

px = img[55,55]
print(px)

px = img[100:150,100:150]
print(px)

print(img.shape)
print(img.size)
print(img.dtype)

watch_face = img[37:111,107:194]
img[0:74,0:87] = watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()





