const fs = require('fs');
const path = require('path');

async function transcription(audioFilePath, apikey) {
    try {
        if (!fs.existsSync(audioFilePath)) {
            throw new Error('File not found');
        }

        const audioFile = fs.readFileSync(audioFilePath);
        const formData = new FormData();
        const blob = new Blob([audioFile], { type: 'audio/wav' });

        formData.append('file', blob, path.basename(audioFilePath));
        formData.append('model', 'whisper-1');

        const response = await fetch('https://api.openai.com/v1/audio/transcriptions', {
            method: 'POST',
            headers: {
                Authorization: `Bearer ${apikey}`,
            },
            body: formData
        });

        if(!response.ok) {
            const errorData = await response.json();
            throw new Error(`API Error: ${JSON.stringify(errorData) }`);
        }

        const data = await response.json();
        const transcription = data.text;

        const outputFilePath = path.join(
            path.dirname(audioFilePath),
            `${path.basename(audioFilePath, path.extname(audioFilePath))}_transcription.txt`
        );

        fs.writeFileSync(outputFilePath, transcription);
        console.log(`Transcription saved to ${outputFilePath}`);
        return transcription;
    } catch (error) {
        console.error(`Error transcribing audio: ${error.message}`);
        throw error;
    }
}

const audioPath = './audio.mp3';
const apikey = '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';

transcription(audioPath, apikey)
    .then(transcription => {
        console.log('Successful transcription.');
        console.log(transcription);
    })
    .catch(error => {
            console.error('Error transcribing audio:', error);
    });
