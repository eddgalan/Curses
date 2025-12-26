console.log('Current Time: ', new Date().toLocaleTimeString());

const timeOut = setTimeout(() => {
    console.log('After 2 seconds');
    console.log('Current Time: ', new Date().toLocaleTimeString());
}, 2000);

setImmediate(() => {
    console.log('After next iteration of the event loop');
    console.log('Current Time: ', new Date().toLocaleTimeString());
});

const intervalId = setInterval(() => {
    console.log('Every 3 seconds');
}, 3000);

setTimeout(() => {
    console.log('Canceling interval after 10 seconds');
    clearInterval(intervalId);
}, 10000);

const timeOutId = setTimeout(() => {
    console.log('This message will never be displayed');
},10000);

clearTimeout(timeOutId);

console.log('End of script', new Date().toLocaleTimeString());
