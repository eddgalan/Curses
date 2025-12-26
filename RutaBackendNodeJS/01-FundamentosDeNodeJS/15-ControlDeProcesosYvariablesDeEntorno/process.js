console.log(`Process ID (PID): ${process.pid}`);
console.log(`Actual Dir: ${process.cwd()}`);
console.log(`Node Version: ${process.version}`);
console.log(`Platform: ${process.platform}`);
console.log(`Architecture: ${process.arch}`);
console.log(`Execution time: ${process.uptime()} seconds`);

console.log(process.env);
console.log(`Path: ${process.env.PATH}`);
console.log(`User Profile: ${process.env.HOME || process.env.USERPROFILE}`);
console.log(`NODE_ENV: ${process.env.NODE_ENV || 'Undefined'}`);

const memoryUsage = process.memoryUsage();
console.log(`Memory Usage: ${JSON.stringify(memoryUsage)}`);

process.on('exit', (code) => console.log('Process terminated', code));

process.on('SIGINT', () => {
    console.log('SIGINT signal received (Ctrl+C)');
    process.exit();
});

console.log('Write a message and press ENTER or CTRL+C to exit.');
process.stdin.on('data', data => {
    const input = data.toString().trim();
    if (input.toLowerCase() === 'exit') {
        console.log('Exiting...');
        process.exit(0);
    } else {
        console.log(`Message: ${input}`);
        console.log(`Write 'exit' to exit or write another message.`);
    }
});