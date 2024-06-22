
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



# from flask import Flask, Response
# import cv2
# import time
# import logging

# app = Flask(__name__)

# def generate_frames():
#     # ビデオキャプチャの初期化
#     capture = cv2.VideoCapture(0)
#     capture.set(3, 640)  # 幅
#     capture.set(4, 360)  # 高さ
#     flag = 0

#     # カスケードファイルの読み込み
#     face_cascade = cv2.CascadeClassifier('./src/haarcascade_frontalface_default.xml')
#     smile_cascade = cv2.CascadeClassifier('./src/haarcascade_smile.xml')
#     logging.info(face_cascade)

#     start_time = time.time()
#     smile_start_time = None

#     while True:
#         ret, img = capture.read()
#         if not ret:
#             break

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
#                 flag = 1
#                 break
#         else:
#             smile_start_time = None

#         # フレームをバイト列に変換してストリーミング
#         ret, buffer = cv2.imencode('.jpg', img)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#         # 経過時間のチェック
#         if time.time() - start_time > 10:
#             print("time end")

#             break

#     capture.release()
#     cv2.destroyAllWindows()
#     # print("Exit")
#     print(flag)
#     return flag

# @app.route('/')
# def index():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import cv2
import numpy as np
import base64
import os
import logging

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# ログの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# XMLファイルのパスを設定
current_dir = os.path.dirname(os.path.abspath(__file__))
face_cascade_path = os.path.join(current_dir, 'src/haarcascade_frontalface_default.xml')
smile_cascade_path = os.path.join(current_dir, 'src/haarcascade_smile.xml')

logger.info(f"現在のディレクトリ: {current_dir}")
logger.info(f"顔検出XMLファイルパス: {face_cascade_path}")
logger.info(f"笑顔検出XMLファイルパス: {smile_cascade_path}")

# ファイルの存在確認
if os.path.exists(face_cascade_path):
    logger.info("顔検出XMLファイルが見つかりました。")
else:
    logger.error("顔検出XMLファイルが見つかりません。")

if os.path.exists(smile_cascade_path):
    logger.info("笑顔検出XMLファイルが見つかりました。")
else:
    logger.error("笑顔検出XMLファイルが見つかりません。")

# カスケード分類器の読み込み
try:
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    smile_cascade = cv2.CascadeClassifier(smile_cascade_path)
    logger.info("カスケード分類器が正常に読み込まれました。")
except Exception as e:
    logger.error(f"カスケード分類器の読み込み中にエラーが発生しました: {str(e)}")

@app.route('/process_image', methods=['POST'])
def process_image():
    logger.info("画像処理リクエストを受信しました。")
    
    # リクエストからBase64エンコードされた画像を取得
    image_data = request.json['image']
    
    # Base64デコード
    image_bytes = base64.b64decode(image_data)
    
    # NumPy配列に変換
    nparr = np.frombuffer(image_bytes, np.uint8)
    
    # 画像をデコード
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    logger.info(f"受信した画像のサイズ: {img.shape}")
    
    # グレースケールに変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 顔検出
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    logger.info(f"検出された顔の数: {len(faces)}")
    
    smile_detected = False
    for (x, y, w, h) in faces:
        cv2.circle(img, (int(x + w / 2), int(y + h / 2)), int(w / 2), (255, 0, 0), 2)
        
        roi_gray = gray[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.2, minNeighbors=10, minSize=(20, 20))
        
        if len(smiles) > 0:
            smile_detected = True
            logger.info("笑顔が検出されました。")
            for (sx, sy, sw, sh) in smiles:
                cv2.circle(img, (int(x + sx + sw / 2), int(y + sy + sh / 2)), int(sw / 2), (0, 0, 255), 2)
    
    # 処理結果の画像をBase64エンコード
    _, buffer = cv2.imencode('.jpg', img)
    processed_image = base64.b64encode(buffer).decode('utf-8')
    
    logger.info("画像処理が完了しました。")
    
    return jsonify({
        'processed_image': processed_image,
        'smile_detected': smile_detected
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
