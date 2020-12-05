const thisYear = new Date().getFullYear()
const startTimeOfThisYear = new Date(`${thisYear}-01-01T00:00:00+00:00`).getTime()
const endTimeOfThisYear = new Date(`${thisYear}-12-31T23:59:59+00:00`).getTime()
const progressOfThisYear = (Date.now() - startTimeOfThisYear) / (endTimeOfThisYear - startTimeOfThisYear)
const progressBarOfThisYear = generateProgressBar()

function generateProgressBar() {
    const progressBarCapacity = 30
    const passedProgressBarIndex = parseInt(progressOfThisYear * progressBarCapacity)
    const progressBar = Array(progressBarCapacity)
        .fill('▁')
        .map((value, index) => index < passedProgressBarIndex ? '█' : value)
        .join('')
    return `${progressBar}`
}

const readme = `
![](https://raw.githubusercontent.com/LikaiLee/likailee.github.io/img/20200818102030.png)
<h2 align="center"><strong><img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="35px"> Hi, fellow <𝚌𝚘𝚍𝚎𝚛𝚜 /> !</strong></h2>
<p>
  This is <strong>Likai Lee</strong> from Hangzhou, China 🇨🇳. I have experience in web depvelopment.  Passionated about technology, communities, and everything in-between 🌎.
</p>

<h2 align="center"><strong>⏳  Year progress @2020</strong></h2>
<p align="center" style="color: orange">
    ${progressBarOfThisYear}<b style="color: #000">${(progressOfThisYear * 100).toFixed(2)}%</b>
</p>

<h2 align="center"><strong>😜 Here's a Joke for you</strong></h2>
<p align="center">
  <img src="https://readme-jokes.vercel.app/api?theme=vue" alt="Jokes Card" />
</p>

---

<p align="right">⏰ Updated on Sat, 05 Dec 2020 10:39:09 GMT</p>

<p align="right">![Build README](https://github.com/LikaiLee/LikaiLee/workflows/Build%20README/badge.svg)</p>
![bottom.png](https://raw.githubusercontent.com/LikaiLee/likailee.github.io/img/20200818102046.png)
`

console.log(readme)