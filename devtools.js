/*
 * Usage instructions:
 *
 * 1. Open the site https://www.landingtutorial.com/ in a browser
 * 2. Open the developer tools pane, using CTRL-SHIFT-I (chromium) or CTRL-SHIFT-C (firefox). Alternatively find it in the settings.
 * 3. Head to the console tab (you should be able to type here)
 * 4. Paste in the code below, changing the configuration settings as desired
 * 5. Hit enter and copy the output to the plotter.py file
 *
 */


/* Start of configuration settings */
let diagSteps = 10; // 1 call / step
let straightSteps = 4; // 4 calls / step
let circleSteps = 20; // 2 calls / step
/* End of configuration settings */



let min = 10;
let max = 8180;
let yScalar = max / Math.sin(Math.PI * (4/3) * 0.25);

let tuples = [];
let compiledTuples = [];

for(let i = 0.0; i < 1.0; i += 1.0/diagSteps) {
    let x = Math.max(min, Math.min(max, Math.sin(Math.PI * (i * 4/3)) * yScalar));
    let y = Math.max(min, Math.min(max, Math.sin(Math.PI * ((i - 0.25) * 4/3)) * yScalar));

    // uses their weird scaling code
    tuples.push([Math.round(500 * ((  x  ) - 4096) / 8192 + 250), Math.round(500 * ((  y  ) - 4096) / 8192 + 250)])
}

for(let i = 0.0; i < 1.0; i += 1.0/diagSteps) {
    compiledTuples[Math.round(i / (1.0 / diagSteps))] = tuples[Math.round(i / (1.0 / diagSteps))].concat(tuples[((diagSteps / 2 + Math.round(i / (1.0 / diagSteps))) % tuples.length)])
}


for(let i = 0; i < straightSteps; i++) {
    compiledTuples.push([1, Math.round((499 / straightSteps) * i), 499, Math.round((499 / straightSteps) * i)]);
    compiledTuples.push([499, Math.round((499 / straightSteps) * i), 1, Math.round((499 / straightSteps) * i)]);
    compiledTuples.push([Math.round((499 / straightSteps) * i), 1, Math.round((499 / straightSteps) * i), 499]);
    compiledTuples.push([Math.round((499 / straightSteps) * i), 499, Math.round((500 / straightSteps) * i), 1]);
}

let angle = 2 * Math.PI / circleSteps
for(let i = 0; i < circleSteps; i++) {
    let x = Math.max(499, Math.round(Math.random() * 100) + Math.round(250 * Math.sin(i * angle)) + 250);
    let y = Math.max(499, Math.round(Math.random() * 100) + Math.round(250 * Math.cos(i * angle)) + 250);

    let nx = Math.round(250 * Math.sin((i % (circleSteps - 1)) * angle)) + 250;
    let ny = Math.round(250 * Math.cos((i % (circleSteps - 1)) * angle)) + 250;

    compiledTuples.push([x, y, nx, ny]);
    compiledTuples.push([nx, ny, x, y]);
}


console.log(compiledTuples.join("-"));
