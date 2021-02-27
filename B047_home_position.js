const line = lines[0].split("");

const lefthandkey = ["q","w","e","r","t","a","s","d","f","g","z","x","c","v","b"];
const righthandkey = ["y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m"];
const keyboard = [["q","w","e","r","t","y", "u", "i", "o", "p"],
                ["a","s","d","f","g","h", "j", "k", "l"],
                ["z","x","c","v","b","n", "m"]];
let [hand, key, count] = ["", "", 0];

for (let i = 0; i < line.length; i++) {

    //alphabets of adjacent keys
    let adjacentkey = []
    for (let j = 0; j < 3; j++){
        for (let z = 0; z < keyboard[j].length; z++){
            if (keyboard[j][z] === line[i]){
                adjacentkey.push(keyboard[j][z]);
                if (j+1 < 3 && z < keyboard[j+1].length){
                    adjacentkey.push(keyboard[j+1][z]);
                }
                if (j-1 > -1 && z < keyboard[j-1].length){
                    adjacentkey.push(keyboard[j-1][z]);
                }
                if (z+1 < keyboard[j].length){
                    adjacentkey.push(keyboard[j][z+1]);
                }
                if (z-1 > -1){
                    adjacentkey.push(keyboard[j][z-1]);
                }
            }
        }
    }

    //initialization
    if (hand === "") {
        if (lefthandkey.indexOf(line[i]) > -1) {
            hand = "left";
        } else if (righthandkey.indexOf(line[i]) > -1) {
            hand = "right";
        }
    }

    if (hand === "left") {
        //count if alphabet on right hand key
        if (righthandkey.indexOf(line[i]) > -1) {
            count++;
        }

        //update hand value
        if (adjacentkey.includes(line[i+1])){
            ; //if next key is adjacent, then hand would not change
        } else if (righthandkey.indexOf(line[i+1]) > -1){
            hand = "right";
        }

    } else if (hand === "right") {
        if (lefthandkey.indexOf(line[i]) > -1) {
            count++;
        }

        if (adjacentkey.includes(line[i+1])){
            ;
        } else if (lefthandkey.indexOf(line[i+1]) > -1){
            hand = "left";
        }
    }
}
console.log(count);
