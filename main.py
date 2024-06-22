
# from flask import Flask, jsonify, request
# import cv2
# import time
# import numpy as np

# app = Flask(__name__)

# # ビデオキャプチャの設定
# capture = cv2.VideoCapture(0)
# capture.set(3, 640)  # 幅
# capture.set(4, 360)  # 高さ

# # カスケードファイルの読み込み
# face_cascade = cv2.CascadeClassifier('./src/haarcascade_frontalface_default.xml')
# smile_cascade = cv2.CascadeClassifier('./src/haarcascade_smile.xml')

# # 開始時間の記録
# start_time = time.time()

# # 笑顔が検出されている開始時間
# smile_start_time = None

# # ルートエンドポイントの設定
# @app.route('/')
# def index():
#     return "Welcome to Smile Detection API"

# # ビデオストリームエンドポイントの設定
# @app.route('/video_feed')
# def video_feed():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# # フレーム生成の関数
# def generate_frames():
#     while True:
#         ret, frame = capture.read()
#         if not ret:
#             break
#         else:
#             frame = cv2.flip(frame, 1)  # 鏡表示にする
#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#             faces = face_cascade.detectMultiScale(gray, 1.1, 5)
#             smile_detected = False
#             for (x, y, w, h) in faces:
#                 cv2.circle(frame, (int(x + w / 2), int(y + h / 2)), int(w / 2), (255, 0, 0), 2)  # 青色の円

#                 roi_gray = gray[y:y + h, x:x + w]  # 顔領域を切り出し
#                 smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.2, minNeighbors=10, minSize=(20, 20))  # 笑顔識別
#                 if len(smiles) > 0:
#                     smile_detected = True
#                     for (sx, sy, sw, sh) in smiles:
#                         cv2.circle(frame, (int(x + sx + sw / 2), int(y + sy + sh / 2)), int(sw / 2), (0, 0, 255), 2)  # 赤色の円

#             if smile_detected:
#                 if smile_start_time is None:
#                     smile_start_time = time.time()
#                 elif time.time() - smile_start_time >= 2:
#                     yield frame
#                     break
#             else:
#                 smile_start_time = None

#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# # 終了処理
# def cleanup():
#     capture.release()
#     cv2.destroyAllWindows()

# # サーバー起動
# if __name__ == '__main__':
#     app.run(debug=True)

# # プログラム終了時のクリーンアップ
# import atexit
# atexit.register(cleanup)
# from dotenv import load_dotenv
# import os
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def detect():
#     """Example Hallo World route."""
#     name = os.environ.get("NAME", "WORLD")
#     return f"Hello {name}!"

# load_dotenv()
# # port = os.getenv('LOCAL')
# port = os.getenv('LOCAL', '5000')

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=int(port))
    # app.run(debug=True,host="0.0.0.0", port=int(os.environ.get("PORT", )))

# from dotenv import load_dotenv
# import os
# from flask import Flask, request, jsonify
# import cv2
# import time

# app = Flask(__name__)

# @app.route("/", methods=["GET"])
# def detect():
# # # # ビデオキャプチャの設定
#     capture = cv2.VideoCapture(0)
#     capture.set(3, 640)  # 幅
#     capture.set(4, 360)  # 高さ

#     # # # カスケードファイルの読み込み
#     face_cascade = cv2.CascadeClassifier('./src/haarcascade_frontalface_default.xml')
#     smile_cascade = cv2.CascadeClassifier('./src/haarcascade_smile.xml')

#     # # # 開始時間の記録
#     start_time = time.time()

#     # # # 笑顔が検出されている開始時間
#     smile_start_time = None

#     while True:
#         ret, img = capture.read()
#         img = cv2.flip(img, 1)  # 鏡表示にする
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#         faces = face_cascade.detectMultiScale(gray, 1.1, 5)
#         smile_detected = False
#         for (x, y, w, h) in faces:
#             cv2.circle(img, (int(x + w / 2), int(y + h / 2)), int(w / 2), (255, 0, 0), 2)  # 青色の円

#             roi_gray = gray[y:y + h, x:x + w]  # 顔領域を切り出し
#             smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.2, minNeighbors=10, minSize=(20, 20))  # 笑顔識別
#             if len(smiles) > 0:
#                 smile_detected = True
#                 for (sx, sy, sw, sh) in smiles:
#                     cv2.circle(img, (int(x + sx + sw / 2), int(y + sy + sh / 2)), int(sw / 2), (0, 0, 255), 2)  # 赤色の円

#         if smile_detected:
#             if smile_start_time is None:
#                 smile_start_time = time.time()
#             elif time.time() - smile_start_time >= 2:
#                 print("smile detected")
#                 break
#         else:
#             smile_start_time = None

#         cv2.imshow('img', img)

#         # 経過時間のチェック
#         if time.time() - start_time > 10:
#             print("time end")
#             break

#         # キー操作
#         key = cv2.waitKey(5)
#         if key == 27:  # escキーで終了
#             break
#     capture.release()
#     cv2.destroyAllWindows()
#     print("Exit")

# load_dotenv()
# port = os.getenv('LOCAL', '5000')

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=int(port))

from dotenv import load_dotenv
import os
from flask import Flask, Response
import cv2
import time

app = Flask(__name__)

def generate_frames():
    # ビデオキャプチャの初期化
    capture = cv2.VideoCapture(0)
    capture.set(3, 640)  # 幅
    capture.set(4, 360)  # 高さ

    # カスケードファイルの読み込み
    face_cascade = cv2.CascadeClassifier('./src/haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier('./src/haarcascade_smile.xml')

    start_time = time.time()
    smile_start_time = None

    while True:
        ret, img = capture.read()
        if not ret:
            break

        img = cv2.flip(img, 1)  # 鏡表示にする
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        smile_detected = False
        for (x, y, w, h) in faces:
            cv2.circle(img, (int(x + w / 2), int(y + h / 2)), int(w / 2), (255, 0, 0), 2)  # 青色の円

            roi_gray = gray[y:y + h, x:x + w]  # 顔領域を切り出し
            smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.2, minNeighbors=10, minSize=(20, 20))  # 笑顔識別
            if len(smiles) > 0:
                smile_detected = True
                for (sx, sy, sw, sh) in smiles:
                    cv2.circle(img, (int(x + sx + sw / 2), int(y + sy + sh / 2)), int(sw / 2), (0, 0, 255), 2)  # 赤色の円

        if smile_detected:
            if smile_start_time is None:
                smile_start_time = time.time()
            elif time.time() - smile_start_time >= 2:
                print("smile detected")
                break
        else:
            smile_start_time = None

        # フレームをバイト列に変換してストリーミング
        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        # 経過時間のチェック
        if time.time() - start_time > 10:
            print("time end")
            break

    capture.release()
    cv2.destroyAllWindows()
    print("Exit")

@app.route('/')
def index():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    load_dotenv()
    port = int(os.getenv('LOCAL', '5000'))
    app.run(debug=True, host='0.0.0.0', port=port)
