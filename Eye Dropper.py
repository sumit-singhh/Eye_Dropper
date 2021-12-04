import cv2
import numpy as np
cmyk_scale = 100
r = g = b = x_pos = y_pos = 0

path = r'Test.jpeg'     #change image form here
user_img = cv2.imread(path)

default_img = np.zeros((200, 400, 3), np.uint8)     #values are displayed in this window

def rgb_to_hex(rgb):    
    hex_val ='%02x%02x%02x' % rgb
    return hex_val

def rgb_to_cmyk(r,g,b):
    if (r == 0) and (g == 0) and (b == 0):
        return 0, 0, 0, cmyk_scale
    else:
        k = 1 - (max(r,g,b)/255)
        c = (1 - r/255 - k)/(1 - k)
        m = (1 - g/255 - k)/(1 - k)
        y = (1 - b/255 - k)/(1 - k)
        return round(c*cmyk_scale,0),round(m*cmyk_scale,0),round(y*cmyk_scale,0),round(k*cmyk_scale,0)

def draw_function(event, x, y, null_0, null_1):
    if event == cv2.EVENT_MOUSEMOVE:    #takes the movement of mouse/cursor as input
        global b, g, r, x_pos, y_pos
        x_pos = x
        y_pos = y
        b, g, r = user_img[y, x]
    
cv2.namedWindow('EYE DROPPER')  #merges all windows
cv2.setMouseCallback('EYE DROPPER', draw_function)  

while True: #infinite loop till image is displayed
    cv2.imshow('EYE DROPPER', user_img)

    if r>150 and g>150 and b>150:
        cv2.putText(default_img, f"RGB: {r,g,b}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0), thickness=2)
        cv2.putText(default_img, f"HEX: #{rgb_to_hex((r,g,b))}", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0), thickness=2)
        cv2.putText(default_img, f"CMYK: {rgb_to_cmyk(r,g,b)}", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0), thickness=2)
    else:    
        cv2.putText(default_img, f"RGB: {r,g,b}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), thickness=2)
        cv2.putText(default_img, f"HEX: #{rgb_to_hex((r,g,b))}", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), thickness=2)
        cv2.putText(default_img, f"CMYK: {rgb_to_cmyk(r,g,b)}", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), thickness=2)
    
    cv2.imshow('COLOUR VALUE', default_img)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

    default_img[:] = [b, g, r]

cv2.destroyAllWindows()
