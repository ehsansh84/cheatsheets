# Examples of ffmpeg by Ehsan Shirzadi

### Scale video, specify width and auto scale height:
```
ffmpeg -i input.mp4 -vf scale=320:-1 output.mp4
```

### Convert to x265:
```
ffmpeg -i input.mp4 -vcodec libx265 out.mp4
```

### Suitalbe convert for Telegram:
```
ffmpeg -i input.mp4 -vf scale=-1:720 -vcodec libx265 output.mp4
```

### Extract from 0 to 60 seconds:
```
ffmpeg -i source-file.foo -ss 0 -t 60 first-1-min.m4v
```
### Put watermark on a video x:y:
```
ffmpeg -i input.mp4 -i watermark.png -filter_complex "overlay=100:300" output.mp4
```
### Put watermark on a video bottom right:
```
ffmpeg -i input.mp4 -i watermark.png -filter_complex "overlay=main_w-overlay_w:main_h-overlay_h" output.mp4
# or
ffmpeg -i input.mp4 -i watermark.png -filter_complex "overlay=W-w:H-h" output.mp4
```
### Extract audio from video:
```
ffmpeg -i input_video.mp4 -vn -acodec libmp3lame -q:a 0 output_audio.mp3
```
### Add cover to mp3:
```
ffmpeg -i input_audio.mp3 -i cover_image.jpg -map 0 -map 1 -c copy -id3v2_version 3 -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" output_audio_with_cover.mp3
```
Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
