# ベースイメージとして公式のPythonイメージを使用
FROM python:3.9-slim

# 作業ディレクトリの作成
WORKDIR /python

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    python3-opencv \
    && /bin/rm -rf /var/lib/apt/lists/*

# アプリケーションの依存関係をインストール
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# アプリケーションコードをコンテナ内にコピー
COPY . .

# ポートの設定
EXPOSE 5000

# コンテナ起動時に実行されるコマンド
CMD ["python", "detect.py"]
