const crypto = require('crypto');

const text = 'Hello World!';

const hash = crypto.createHash('sha256').update(text).digest('hex');

console.log(`Original Text: ${text}`);
console.log(`Hash: ${hash}`);
