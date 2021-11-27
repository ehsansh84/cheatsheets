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

Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com