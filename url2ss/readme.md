# url2ss

指定したURLから連続してスクリーンショットを取得します。

# 設定方法

## Windows の場合

※python が動いていることが前提です。

### (1) chrome をインストールします。

### (2) ChromeDriver を利用可能にします。 

以下のURLから、ChromeDriver をダウロードして、url2ss.py と同じフォルダに ```chromedriver.exe``` を置きます。
http://chromedriver.chromium.org/downloads

### (3) CSV ファイルを作成します

(ファイル名),(URL) の形式で作成します。

```
0010, http://example.com/
0020, http://example.com/page1.html
```

※1行目を見出しにする必要はありません。

### (4) キャプチャー実行

```sample.csv``` で作成した場合。

```
python url2ss.py sample.csv
```

こちらを実行ください。url2ss.py のあるフォルダの配下に、```年月日日時秒``` 形式のフォルダが作成され、その中にキャプチャが画像が用意されています。




