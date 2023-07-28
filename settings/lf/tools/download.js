const path = require('path');
const fs = require('fs');
const download = require('download');

if (process.argv.length < 3) {
    console.error('Missing URL');
    process.exit();
}

const URL = process.argv[2];

function getTargetPath(originURL) {
    if (process.argv.length > 3) {
        return path.resolve(process.argv[3]);
    }

    const processDir = process.cwd();
    return path.join(processDir, path.parse(originURL).base);
}

const TARGET_PATH = getTargetPath(URL);

console.log(`Downloading from "${URL}" to "${TARGET_PATH}`);

if (fs.existsSync(TARGET_PATH)) {
    fs.unlink(TARGET_PATH);
}

(async () => {

    const data = await download(URL);
    fs.writeFileSync(TARGET_PATH, data);
    console.log(`Downloaded from "${URL}" to "${TARGET_PATH}`);

})();
