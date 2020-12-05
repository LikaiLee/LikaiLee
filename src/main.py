# -*- coding: utf-8 -*-
import datetime

def get_past_percentage(cur_year, now):
	start_of_year = datetime.datetime(cur_year, 1, 1)
	end_of_year = datetime.datetime(cur_year + 1, 1, 1)
	return (now - start_of_year).total_seconds() / (end_of_year - start_of_year).total_seconds()


def gen_progress_bar(capacity, percent):
	bar = int(capacity * percent)
	return ['░' if i > bar else '█' for i in range(capacity)]


BAR_CAPACITY = 50
FORMATTER = '%a, %d %b %Y %H:%M:%S (GMT)'
cur_year = datetime.datetime.now().year
now = datetime.datetime.now()
percent = get_past_percentage(cur_year, now)
progress_bar = ''.join(gen_progress_bar(BAR_CAPACITY, percent))
update_time = now.strftime(FORMATTER) 

read_me = f'''
![](https://raw.githubusercontent.com/LikaiLee/likailee.github.io/img/20200818102030.png)

<h2 align="center"><strong><img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="35px"> Hi, fellow <𝚌𝚘𝚍𝚎𝚛𝚜 /> !</strong></h2>
<p>
  This is <strong>Likai Lee</strong> from Hangzhou, China 🇨🇳. I have experience in web depvelopment.  Passionated about technology, communities, and everything in-between 🌎.
</p>

<h2 align="center"><strong>⏳ Year progress @{cur_year}</strong></h2>
<p align="center">
    {progress_bar}&nbsp;&nbsp;<b>{round(percent * 100, 2)}%</b>
</p>

<h2 align="center"><strong>😜 Here's a Joke for you</strong></h2>
<p align="center">
  <img src="https://readme-jokes.vercel.app/api?theme=vue" alt="Jokes Card" />
</p>

---

<a href="https://github.com/LikaiLee"><img src="https://github.com/LikaiLee/LikaiLee/workflows/Build%20README/badge.svg" alt="Build README" align="left" /></a><br />
<p align="left">⏰ Updated at {update_time}</p>

![bottom.png](https://raw.githubusercontent.com/LikaiLee/likailee.github.io/img/20200818102046.png)
'''
print(read_me)
