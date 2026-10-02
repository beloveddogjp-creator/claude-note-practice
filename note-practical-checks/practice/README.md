# 目標と出力を比べる練習

card.mdを複製して使います。source-4s.mp4は自作の合成4秒映像です。FFmpegとffprobeが導入済みなら、このフォルダで冒頭1秒を別名へ切り出せます。-nは既存ファイルを上書きしない指定です。

```sh
ffmpeg -hide_banner -nostdin -n -i source-4s.mp4 -t 1 -an -c:v libx264 practice-1s.mp4
ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=width,height,r_frame_rate,nb_read_frames:format=duration -of json practice-1s.mp4
```

今回のmacOS/FFmpeg 9.0.2では640×360、25/1、25フレーム、1.000000秒を確認しました。2秒にした出力は50フレームです。アプリが別なら、同じ数字のコマンドを転用せず、そのアプリで確認できる目標を一つ決めます。人の記憶や翌日の再現、15分での完了は検証していません。
