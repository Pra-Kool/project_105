import os
import cv2

path = 'Images/'
Images = []
count = len(Images)
frame = cv2.imread(images[0])
size = (widht, height)

# print(size)

for Images in os.listdir(path):
    name, ext = os.path.splitext(Images)

if ext in ['.gif', '.png', 'jpg', '.jpeg', '.jfif']:
    file_name = path+'/'+file

# print(file_name)
.append('1.jpg')
.append('2.jpg')
.append('3.jpg')
.append('4.jpg')
.append('5.jpg')
.append('6.jpg')
.append('7.jpg')
.append('8.jpg')
.append('9.jpg')
.append('10.jpg')

height = int(Images.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)

width = int(Images.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)

fps = int(Images.get(cv2.CAP_PROP_FPS))
print(fps)
out = cv2.VideoWriter('Video2.mp4', cv2.VideoWriter_fourcc(*'DIVX'),0.8,(width,height))

for i in range(0, count-1):
    cv2.imread()
    out.write()

print('Done')