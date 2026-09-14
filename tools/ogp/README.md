# 共有サムネイル (OGP 画像) の生成元

`img/ogp-v4.png` (1200x630) の生成元です。URL を Slack・LINE・Facebook などに貼ったときにカードに出る画像です。

## 作り直し方

リポジトリの直下で実行します。フォントは Google Fonts から読むので、ネットにつながっている必要があります。

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu \
  --hide-scrollbars --force-device-scale-factor=1 --window-size=1200,630 \
  --virtual-time-budget=8000 --allow-file-access-from-files \
  --screenshot="$PWD/img/ogp-v5.png" "file://$PWD/tools/ogp/ogp.html"
```

## 差し替えるとき

1. 画像は新しい名前 (`ogp-v5.png` など) で出します。同じ名前で上書きすると、SNS 側が古い画像を持ち続けます
2. 全 HTML の `og:image` と `twitter:image`、`index.html` の構造化データの `logo` を新しい名前に揃えます。漏れは `grep -rn 'ogp-v' --include='*.html' .` で確かめます
3. push した後、Facebook と Messenger は Sharing Debugger (https://developers.facebook.com/tools/debug/) で再スクレイピングします。LINE は Page Poker (https://poker.line.naver.jp/) で更新します

## 文言

トップ `index.html` の `.hero-statement__call` の文をそのまま使っています。トップのその文が変わったら、ここも合わせます。
