const http = require('http');

const server = http.createServer((request, response) => {
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.end('Hello World! From Node.js');
});

server.listen(3000, '127.0.0.1', () => console.log('Server running on port 3000'));

// Se puede levantar el servidor con 'node --watch server.js'
