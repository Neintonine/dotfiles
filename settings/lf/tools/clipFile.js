const { spawn } = require('child_process');
const { isText } = require('istextorbinary');
const fs = require("fs");
const ncp = require('copy-paste');

if (process.argv.length < 3) {
    console.error('Missing File');
    process.exit();
}

const file = process.argv[2];
console.log(process.argv);

async function runFile2Clip() {
    await new Promise((resolve, reject) => {
        const clipProcess = spawn(__dirname + '\\file2clip', [file]);

        clipProcess.on('close', resolve);
        clipProcess.on('error', reject);
    });
    console.log('Copied as file');
}


if (process.argv.length === 4 && process.argv[3] === '--always-as-file') {
    console.log('clip as file');
    runFile2Clip();
} else {
    const buffer = fs.readFileSync(file);
    if (isText(null, buffer)) {
        ncp.copy(buffer);
        console.log('Copied as text');
    }
    else {
        runFile2Clip();
    }

}
