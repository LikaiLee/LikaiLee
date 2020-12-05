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
    return `{ ${progressBar} }`
}

const readme = `
<h2 align="center"><strong><img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="35px"> Hi, fellow <𝚌𝚘𝚍𝚎𝚛𝚜 /> !</strong></h2>
<p align="center">
  This is Likai Lee from Hangzhou, China 🇨🇳. I have experience in web depvelopment.  Passionated about technology, communities, and everything in-between 🌎.
</p>

<h2 align="center"><strong>😜 Here's a Joke for you</strong></h2>
<p align="center">
  <img src="https://readme-jokes.vercel.app/api" alt="Jokes Card" />
</p>

⏳ Year progress ${progressBarOfThisYear} ${(progressOfThisYear * 100).toFixed(2)} %

---

⏰ Updated on ${new Date().toUTCString()}

![Progress Bar CI](https://github.com/liununu/liununu/workflows/Progress%20Bar%20CI/badge.svg)
`

console.log(readme)