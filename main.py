import face_recognition
from PIL import Image,ImageDraw
image_1 = face_recognition.load_image_file('./faces/faces.webp')
image_1_loc = face_recognition.face_locations(image_1)
image_1_pil = Image.fromarray(image_1)
for i in range(0,len(image_1_loc)):

 top = image_1_loc[i][0]
 right = image_1_loc[i][1]
 bottom = image_1_loc[i][2]
 left = image_1_loc[i][3]

 draw = ImageDraw.Draw(image_1_pil)
 draw.rectangle((left,top,right,bottom),outline=(250,7,0))
print("the total no of faces are ",len(image_1_loc)," and they are")

image_1_pil.show()