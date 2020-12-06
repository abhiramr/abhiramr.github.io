---
layout: post
title: What I Learnt from 6 hours of tinkering with FFmpeg
tags: [media, editing, video, audio]
---

### What is FFmpeg?

In their own words, FFmpeg is "A complete, cross-platform solution to record, convert and stream audio and video."


I've been recording <a href="http://bangalore.python.org.in/" style="color:blue">Bangpypers</a> videos for the last few months and I haven't really had access to a proper solution to edit videos and audio that I could have got for free/ low-cost. A good friend of mine, Vinay Keerthi, (who incidentally presented the webinar under discussion) told me to chuck GUI based fronts for editing them and told me to try FFmpeg, the CLI tool directly, which these tools probably use in the background anyway. 

So I gave it a shot. 
And while it isn't very hard to break into, there are a lot of things that aren't very straight-forward. But it's definitely a treat to use and it gives you a sense of satisfaction when things work. 

#### My case-study's solution : 

So I've mentioned above about videos recorded for Bangpypers. This particular case today was for editing one such video. 

Basically, I had a 40 minute webinar that I needed to cut up to replace a part of the video with an image, and then stitch these sections with another video, also a part of the webinar but recorded separately. This second half also needed to have some part of the video trimmed and the rest have the video be replaced with the Bangpypers Logo. 

There were a lot of experiments I did in the process. 

For now, here's a working set of steps: 

- Split the first video from [0,time_a] and [time_a,time_b] resulting in videos say -  video_1_a.mp4, video_1_b.mp4
- Overlay the video in video_1_a with the desired png = bangpypers.png.
- Once the overlayed video is available, stitch video_1_a_overlay.mp4 to video_1_b.mp4. = video_1_final.mp4
    - In this step, there were issues because the image used was a 900*900 png but the video in question was of a higher resolution. So the obvious remedy was to scale the image and stitch it up. But I took some time to get to this resolution and found ways to stitch it directly just fine but the resultant was obviously very messed up. So the entire set of steps had to be repeated. 

- For the second video, treat it similarly as in the video_1_a.mp4. Let's call this video_2.mp4
- Trim the video from [time_a,end]
- Overlay the trimmed video with the desired png = bangpypers.png.
- Stitch video_1_final.mp4 to video_2_final.mp4

---- 

#### Commands for steps above: 

*Video 1*

`ffmpeg -ss 00:01:01 -i Webinar_Full_Part1.mp4 -t 00:05:19 -c copy video_1_a.mp4`

`ffmpeg -ss 00:06:21 -i Webinar_Full_Part1.mp4 -t 00:33:50 -c copy video_1_b.mp4`

`ffmpeg -i video_1_a.mp4 -i bangpypers.png -filter_complex "[1][0]scale2ref[i][v];[v][i]overlay" -c:a copy video_1_a.mp4`

`ffmpeg -i video_1_a.mp4 -i video_1_b.mp4 -filter_complex "[0:v] [0:a] [1:v] [1:a] concat=n=2:v=1:a=1 [v] [a]" -map "[v]" -map "[a]" video_1_processed.mp4`

*Video 2*

`ffmpeg -ss 00:03:23 -i Webinar_Full_Part2.mp4 -t 00:09:08 -c copy video_2.mp4`

`ffmpeg -i video_2.mp4 -i bangpypers.png -filter_complex "[1][0]scale2ref[i][v];[v][i]overlay" -c:a copy video_2.mp4`

`ffmpeg -i video_2.mp4 -vf scale=1920:1080,setsar=1:1 video_2_processed.mp4`

*Final*

`ffmpeg -i video_1_processed.mp4 -i video_2_processed.mp4 -filter_complex "[0:v] [0:a] [1:v] [1:a] concat=n=2:v=1:a=1 [v] [a]" -map "[v]" -map "[a]" Webinar_video_processed.mp4`

The net result of this learning can be viewed at our Bangpypers Channel - 
<a href="https://www.youtube.com/watch?v=xickNijifOs" style="color:blue">https://www.youtube.com/watch?v=xickNijifOs</a>

#### Explanation/ Legend of params used - 

- `ss`: Start time as hh:mm:ss
- `t` : Duration for which to clip
- `v` : Video
- `a` : Audio
- `[0:v] [0:a] [1:v] [1:a] concat=n=2:v=1:a=1 [v] [a]` : Concatenating 2 videos (n=2) where both `v` and `a` exist. Hence `v=1`,`a=1`
- The last parameter in each of the commands is the output video. 

----

#### Chronicled some more of the commands here - 

- <a href="https://docs.google.com/document/d/1sax37PO6DMFKCS5iwnl7dboaSnpLRl-YXiY3uyiWhXo/edit?usp=sharing" style="color:blue">https://docs.google.com/document/d/1sax37PO6DMFKCS5iwnl7dboaSnpLRl-YXiY3uyiWhXo/edit?usp=sharing</a>

----


#### Links referred
- <a href="https://ffmpeg.org/ffmpeg.html#SEC8" style="color:blue">https://ffmpeg.org/ffmpeg.html#SEC8</a>
- <a href="https://trac.ffmpeg.org/wiki/Scaling" style="color:blue">https://trac.ffmpeg.org/wiki/Scaling</a>
- <a href="https://itsfoss.com/ffmpeg/" style="color:blue">https://itsfoss.com/ffmpeg/</a>
- <a href="https://stackoverflow.com/questions/37327163/ffmpeg-input-link-in1v0-parameters-size-640x640-sar-169-do-not-match-the#" style="color:blue">https://stackoverflow.com/questions/37327163/ffmpeg-input-link-in1v0-parameters-size-640x640-sar-169</a>
- <a href="https://stackoverflow.com/questions/38753739/ffmpeg-overlay-a-png-image-on-a-video-with-custom-transparency" style="color:blue">https://stackoverflow.com/questions/38753739/</a>
- <a href="https://stackoverflow.com/questions/7333232/how-to-concatenate-two-mp4-files-using-ffmpeg" style="color:blue">https://stackoverflow.com/questions/7333232/how-to-concatenate-two-mp4-files-using-ffmpeg</a>
- <a href="https://stackoverflow.com/questions/40480153/how-to-overlay-place-an-image-on-a-video-in-ffmpeg" style="color:blue">https://stackoverflow.com/questions/40480153/how-to-overlay-place-an-image-on-a-video-in-ffmpeg</a>
- <a href="https://stackoverflow.com/questions/19425674/ffmpeg-concat-and-scale-simultaneously" style="color:blue">https://stackoverflow.com/questions/19425674/ffmpeg-concat-and-scale-simultaneously</a>
- <a href="https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg" style="color:blue">https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg</a>
- <a href="https://superuser.com/questions/855276/join-2-video-file-by-command-or-code" style="color:blue">https://superuser.com/questions/855276/join-2-video-file-by-command-or-code</a>
- <a href="https://superuser.com/questions/722247/how-can-i-remove-multiple-segments-from-a-video-keeping-the-audio-using-ffmpeg" style="color:blue">https://superuser.com/questions/722247/how-can-i-remove-multiple-segments-from-a-video-keeping-the-audio-using-ffmpeg</a>
- <a href="https://superuser.com/questions/268985/remove-audio-from-video-file-with-ffmpeg" style="color:blue">https://superuser.com/questions/268985/remove-audio-from-video-file-with-ffmpeg</a>
- <a href="https://video.stackexchange.com/questions/20430/how-to-concatenate-multiple-videos-with-ffmpeg?newreg=9c40f3f240a24b30a72120c8cb6f4d76" style="color:blue">https://video.stackexchange.com/questions/20430/how-to-concatenate-multiple-videos-with-ffmpeg?newreg=9c40f3f240a24b30a72120c8cb6f4d76</a>
- <a href="https://video.stackexchange.com/questions/15468/non-monotonous-dts-on-concat-ffmpeg" style="color:blue">https://video.stackexchange.com/questions/15468/non-monotonous-dts-on-concat-ffmpeg</a>

----

#### Bloopers

I made a lot of mistakes in trying other stuff but learnt quite a bit in the process. Here's a glimpse of the commands tried -

![ffmpeg](../img/tech/ffmpeg_bloopers.png)

I hope this helps you if you're looking for help with FFMpeg. Feel free to mail/<a href="https://twitter.com/abhicantdraw" style="color:blue">tweet at</a>  me if you have any issues!

#### About Bangpypers

Bangpypers is one of Bangalore's largest Python User Groups. We conduct Meetups where we have talks and workshops on topics related to Python. Feel free to reach out to mail me in case you want to talk at any of our upcoming sessions. We conduct one every month. More details regarding meetups at <a href="https://www.meetup.com/Bangpypers/" style="color:blue">https://www.meetup.com/Bangpypers/</a>. We're also on <a href="https://twitter.com/__bangpypers__" style="color:blue">Twitter<a>!