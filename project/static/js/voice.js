navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
        const mediaRecorder = new MediaRecorder(stream);

        document.querySelector('#start').addEventListener('click', function () {
            mediaRecorder.start();
        });
        let audioChunks = [];
        mediaRecorder.addEventListener("dataavailable", function (event) {
            audioChunks.push(event.data);
        });

        document.querySelector('#stop').addEventListener('click', function () {
            mediaRecorder.stop();
        });

        mediaRecorder.addEventListener("stop", function () {
            const audioBlob = new Blob(audioChunks, {
                type: 'audio/wav'
                
            });

            fetch("http://127.0.0.1:5000/", {
                method: "post",
                body: audioBlob
              });

            
           
        });
        
      
    });