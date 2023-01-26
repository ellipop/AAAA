import cv2
import os 

path = "Images/"
images = []


for files in os.listdir(path):
    name, extention = os.path.splitext(files)
    if extention in ['.jpg', '.png', 'jpeg', '.gif', '.jfif']:
        file_name = path+"/"+files
        print(file_name)
        images.append(file_name)

count = len(images)
frame = cv2.imread(images[0])
w,h,layers = frame.shape
size = (w,h)

out = cv2.VideoWriter('frens.avi', cv2.VideoWriter_fourcc(*'XVID'),  0.8, size)

for i in range(0, count):
    frame = cv2.imread(images[i])
    out.write(frame)

print("AAAAAAAAAAAAAAAAAA")
out.release()
