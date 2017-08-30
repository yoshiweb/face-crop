import os
import cv2

# ディレクトリ参照
dir_path = 'img_org'

# 切り抜いた画像の保存先ディレクトリ(予めディレクトリを作っておく)
save_path = 'img_face'

# OpenCVのデフォルトの分類器のpath
# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
# をダウンロードしておく
cascade_path = 'haarcascade_frontalface_default.xml'

#カスケード分類器の特徴量を取得する
faceCascade = cv2.CascadeClassifier(cascade_path)

# 顔検知に成功した数
i = 0


# ファイル一覧を取得
dir_files = os.listdir(dir_path)
img_files = [fi for fi in dir_files if os.path.isfile(os.path.join(dir_path, fi))]
# print(img_files)   # ['01.jpg', '02.jpg', '03.jpg']

for file in img_files:

    if(file[-4:] == '.jpg' or file[-4:] == '.png'):     #ファイル名の後ろ4文字を取り出してそれが.jpgなら
        img_path = os.path.join(dir_path, file)

        # 読み込み
        img = cv2.imread(img_path, cv2.IMREAD_COLOR)

        # グレースケール変換（処理が早いらしい）
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 物体認識（顔認識）の実行
        face = faceCascade.detectMultiScale(gray, 1.1, 3)

        # 顔が検知されたら
        if len(face) > 0:
            for rect in face:
                x = rect[0]
                y = rect[1]
                w = rect[2]
                h = rect[3]

                # 切り取り、保存する
                save_file_name = 'face_' + str(i) + '.jpg'
                save_file_path = os.path.join(save_path, save_file_name)
                cv2.imwrite(save_file_path , img[y:y+h, x:x+w])
                
                i += 1
        else:
            print('NoFace:'+img_path)
