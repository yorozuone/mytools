# url2element

指定したURLから連続してページタイトルを取得します。

# 設定方法

## Windows の場合

※python が動いていることが前提です。

### (1) chrome をインストールします。

### (2) ChromeDriver を利用可能にします。 

以下のURLから、ChromeDriver をダウロードして、url2ss.py と同じフォルダに ```chromedriver.exe``` を置きます。
http://chromedriver.chromium.org/downloads

### (3) CSV ファイルを作成します

URL を一覧形式で作成します。

```
http://example.com/
http://example.com/page1.html
```

※1行目を見出しにする必要はありません。

### (4) タイトル取得実行

```sample.csv``` で作成した場合。

```
python url2element.py sample.csv
```

こちらを実行ください。CSV の内容に従って、タイトルが出力されます。







