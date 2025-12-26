const http = require('http');
const fs = require('fs');
const path = require('path');

const server = http.createServer((request, response) => {
    if (request.url === '/video') {
        const videoPath = path.join(__dirname, 'video.mp4');
        // Get file information
        const stat = fs.statSync(videoPath);

        // Set headers
        response.writeHead(200, {
            'Content-Type': 'video/mp4',
            'Content-Length': stat.size
        });

        // Stream video (Read Stream)
        const readStream = fs.createReadStream(videoPath);      // Buffer

        // Count chunks
        let chunkCounter = 0;

        // Event for each chunk
        readStream.on('data', (chunk) => {
            chunkCounter++;
            console.log(`Chunk ${chunkCounter}: Size ${chunk.length} bytes`);
        });

        // Pipe video to response
        readStream.pipe(response);
    } else {
        response.writeHead(404, {"Content-Type": "text/html"});
        response.end('<h1>Not Found</h1>');
    }
});

server.listen(3000, '127.0.0.1', () => console.log('Server running on port 3000'));
// Run in terminal 'node --watch server-video.js' to start server
// Download video: https://download.blender.org/peach/bigbuckbunny_movies/