const os = require('os');

function showSystemInfo() {
    console.log(`Operate System: ${os.type()}`);
    console.log(`Platform: ${os.platform()}`);
    console.log(`Architecture: ${os.arch()}`);
    console.log(`Release: ${os.release()}`);
    console.log(`Memory: ${os.totalmem()}`);
    console.log("Free Memory:", os.freemem());
    console.log("CPUs: ", os.cpus().length);
    console.log("Principal Dir: ", os.homedir());
    console.log("Hostname: ", os.hostname());
}

showSystemInfo();
