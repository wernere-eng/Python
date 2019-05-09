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
    import numpy as np    
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
    print('numpy: {}' .format(np.numpy.__version__))
    print('cv2: {}'.format(cv2.__version__))
    print('matplotlib: {}'.format(plt.__version__))
#end print versions
#########################################
    
#########################################
# Load and show single image
img = cv2.imread('watch.jpg' , 0)   

#draw shapes
cv2.line(img,(0,0),(150,150) ,(255,255,255),15)
cv2.rectangle(img,(15,25),(200,150),(0,0,255),15)
cv2.circle(img,(100,63), 55, (0,255,0), -1)

#write some text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Tuts!',(0,130), font, 1, (200,255,155), 2, cv2.LINE_AA)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# END Load and show single image
#########################################


#########################################
#load video feed from camera

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()









