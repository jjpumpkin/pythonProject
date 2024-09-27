# ocr관련 라이브러리
# pip install easyOCR
# 이미지 편집 관련 라이브러리
# pip install opencv-python
import easyocr
import cv2
from networkx import center

from python_base.Day2_Formattion import height

src= cv2.imread('./car.JPG')
gray =cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
cv2.imwrite('car_gray.jpg' ,gray)

blur =cv2.medianBlur(src, 25)
cv2.imwrite('car_blur.jpg',blur)
# 이미지 크기
height, width, _=src.shape
print(height,width)
# 중앙 100x100 자르기
crop_width =250
crop_height =200

center_x ,center_y =width // 2, height // 2

# 자를 영역의 시작 및 끝 좌표 계산
x_start = center_x -(crop_width // 2)
x_end = center_x +(crop_width // 2)

y_start = center_y -(crop_height // 2)
y_end = center_y + (crop_height // 2)
# 이미지 자르기
cropped = src[y_start:y_end, x_start:x_end]
cv2.imwrite('cropped_car.jpg', cropped)

reader = easyocr.Reader(['en','ko'],gpu=False)
results =reader.readtext('./cropped_car.JPG')
for result in results:
  if result[2] >0.4:
      print(result[1])