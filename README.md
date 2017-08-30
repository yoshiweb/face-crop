# Python + OpenCV で 顔を切り抜いて画像を保存

## 環境

- Python 3.6.1
- OpenCV 3.3

## 事前準備

```
$ pip install opencv-python
$ curl -O https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
```

img_orgディレクトリに画像をたくさん格納



## 画像から顔を切り抜く

```
$ python face_crop.py
```

img_faceディレクトリに切り抜かれた画像が生成される


