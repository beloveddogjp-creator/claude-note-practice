# 黒画面・無音の候補を見つける練習

FFmpegとffprobeの導入済み環境が必要です。自作のsynthetic-qc-8s.mp4は640×360、25fps、8秒です。2〜3秒に黒画面、4〜5秒付近に無音があります。6秒付近には短い黒画面と無音もあります。実案件・人物素材は含みません。

このffmpegフォルダのターミナルで実行します。

```sh
ffmpeg -version
ffprobe -version
ffprobe -v error -show_entries stream=index,codec_type,channels:format=duration -of default=noprint_wrappers=1 synthetic-qc-8s.mp4
ffmpeg -hide_banner -nostdin -nostats -i synthetic-qc-8s.mp4 -map 0:v:0 -an -vf "blackdetect=d=0.2:pic_th=0.98:pix_th=0.10" -f null -
ffmpeg -hide_banner -nostdin -nostats -i synthetic-qc-8s.mp4 -map 0:a:0 -vn -af "silencedetect=n=-50dB:d=0.5" -f null -
```

macOS 26.6.2、FFmpeg 9.0.2の今回の結果は、黒画面2〜3秒、無音4.010875〜5.013271秒です。入力のSHA-256は処理前後で一致しました。全環境で同じ小数秒になる保証はありません。短い区間はこの最低時間では一覧に出ません。演出と不具合の区別、字幕・同期・声だけの欠落、全編の視聴は別に確認します。

公式: https://ffmpeg.org/ffmpeg-filters.html#blackdetect
公式: https://ffmpeg.org/ffmpeg-filters.html#silencedetect
