URL = window.URL || window.webkitURL;

const PERSONAL_URL = "http://127.0.0.1:5000/"

let gumStream;
let rec;
let input;

let AudioContext = window.AudioContext || window.webkitAudioContext;
let audioContext

let recordButton = document.getElementById("start");
let stopButton = document.querySelector('#stop');
let pauseButton = document.querySelector('#pause');
let nextButton = document.querySelector('#next');

recordButton.addEventListener("click", startRecording);
stopButton.addEventListener("click", stopRecording);
pauseButton.addEventListener("click", pauseRecording);
nextButton.addEventListener("click", getQuestion)



function startRecording() {
    console.log("recordButton clicked");

    let constraints = { audio: true, video: false }

    recordButton.disabled = true;
    stopButton.disabled = false;
    pauseButton.disabled = false

    navigator.mediaDevices.getUserMedia(constraints).then(function (stream) {
        console.log("getUserMedia() success, stream created, initializing Recorder.js ...");
        audioContext = new AudioContext();
        gumStream = stream;
        input = audioContext.createMediaStreamSource(stream);
        rec = new Recorder(input, { numChannels: 1 })
        rec.record()
        console.log("Recording started");

    }).catch(function (err) {
        recordButton.disabled = false;
        stopButton.disabled = true;
        pauseButton.disabled = true
    });
}

function pauseRecording() {
    console.log("pauseButton clicked rec.recording=", rec.recording);
    if (rec.recording) {
        //pause
        rec.stop();
        pauseButton.innerHTML = "GO!";
    } else {
        //resume
        rec.record()
        pauseButton.innerHTML = "Пауза";

    }
}
function stopRecording() {
    console.log("stopButton clicked");

    stopButton.disabled = true;
    recordButton.disabled = false;
    pauseButton.disabled = true;

    pauseButton.innerHTML = "Пауза";
    rec.stop();

    gumStream.getAudioTracks()[0].stop();
    rec.exportWAV(createDownloadLink);
    // getData()
}

async function createDownloadLink(blob) {
    let xhr = new XMLHttpRequest();
    xhr.onload = function (e) {
        if (this.readyState === 4) {
            console.log("Server returned: ", e.target.responseText);
        }
    };

    let fd = new FormData();
    fd.append('voice', blob);

    await fetch(PERSONAL_URL, {
        method: "POST",
        body: fd
    });
    let [myAnswer, rightAnswer, score] = ['Мой ответ', 'Правильный ответ', '8'];
    document.querySelector('.my-answer').innerHTML = myAnswer;
    document.querySelector('.right-answer').innerHTML = rightAnswer;
    document.querySelector('.result__box-score > h1').innerHTML = `${score}/10`;

}

async function getQuestion() {
    //     let response = await fetch(PERSONAL_URL, {
    //         method: "POST",
    //         body: fd
    //     });
    //     let commits =  await response.json();

    //     console.log(commits)
    let [tempIndex, tempIssue] = ['2', 'Передаточная функция'];
    document.querySelector('.quest').innerHTML = `Вопрос ${tempIndex}: Дайте определение: ${tempIssue}`;



}
