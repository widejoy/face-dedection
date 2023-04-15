import face_recognition
from PIL import Image,ImageDraw
image_1 = face_recognition.load_image_file('./faces/faces.webp')
image_1_loc = face_recognition.face_locations(image_1)
for i in range(0,len(image_1_loc)):

 top = image_1_loc[i][0]
 right = image_1_loc[i][1]
 bottom = image_1_loc[i][2]
 left = image_1_loc[i][3]

 image_1_biden = image_1[top:bottom , left:right]
 image_1_joe = Image.fromarray(image_1_biden) 
 image_1_joe.show()
