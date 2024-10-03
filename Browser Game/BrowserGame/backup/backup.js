// BACKUP MADE ON 2023 APRIL 6TH 16:43


let canvas;
let context; 

let fpsInterval = 1000 / 30;
let now;
let then = Date.now();
let request_id;

let entities = [];
let player = {
    x : 0,
    y : 0,
    width : 12,
    height : 18,
    frameX : 0,
    frameY : 0,
    xChange : 0,
    yChange : 0,
    range : 150,
    score : 0,
    hp : 10
};
let coins = [];


let moveLeft = false;
let moveRight = false;
let moveUp = false;
let moveDown = false;
let attack = false;

let playerImage = new Image();
let backgroundImage = new Image();

// let floor;

let tilesPerRow = 6;
let tileSize = 16;

let background = [
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
]

document.addEventListener("DOMContentLoaded", init, false);

function init() {
    canvas = document.querySelector("canvas");
    context = canvas.getContext("2d");

    player.x = canvas.width / 2;
    player.y = canvas.height / 2;

    window.addEventListener("keydown", activate, false);
    window.addEventListener("keyup", deactivate, false);

    draw();
    // load_assets([
    //     {"var": playerImage, "url" : "insertImg.png"},
    //     {"var" : backgroundImage, "url" : "insertImg.png"}
    // ], draw);
}

function draw() {
    request_id = window.requestAnimationFrame(draw);
    let now = Date.now();
    let elapsed = now - then;
    if (elapsed <= fpsInterval) {
        return;
    }
    then = now - (elapsed % fpsInterval);

    if (entities.length < 5) {
        let e = {
            x : randint(0, canvas.width),
            y : randint(0, canvas.height),
            xChange : randint(-8, 8),
            yChange : randint(-8, 8),
            index : entities.length - 1
        };
        entities.push(e)
    }
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = "cyan";
    context.fillRect(player.x, player.y, player.width, player.height);

    context.font = "30px serif";
    context.fillStyle = "pink";
    context.fillText(player.hp, 50, 30);
    context.fillText("HP:", 3, 30);
    context.fillText(player.score, 90, 60);
    context.fillText("Score:", 3, 60);

    context.fillStyle = "red";
    for (let e of entities) {
        while (e.x === player.x && e.y === player.y) {
            e.x = randint(0, canvas.width);
            e.y = randint(0, canvas.height);
        };
        context.fillRect(e.x, e.y, 12, 18);
    }

    context.fillStyle = "yellow";
    if (coins.length < 5) {
        let coin = {
            x : randint(0, canvas.width),
            y : randint(0, canvas.height)
        };
        coins.push(coin);
    }
    for (let coin of coins) {
        while (coin.x === player.x && coin.y === player.y || coin.x === entities.x && coin.y === entities.y) {
            coin.x = randint(0, canvas.width);
            coin.y = randint(0, canvas.height);
        };
        context.fillRect(coin.x, coin.y, 15, 15)
    }
    
    for (let e of entities) {
        if (e.y + 18 > canvas.height){
            e.y = canvas.height - 18;
            e.yChange = -7;
        } else if (e.y < 0){
            e.y = 0;
            e.yChange = 7;
        } else if (e.x + 12 > canvas.width){
            e.x = canvas.width - 12;
            e.xChange = -7;
        } else if (e.x < 0){
            e.x = 0;
            e.xChange = 7;
        } 
        
        e.x = e.x + e.xChange;
        e.y = e.y + e.yChange;
    }


//    for (let r = 0; r < 20; r+= 1) {
//         for (let c = 0; c < 32; c += 1) {
//             let tile = background[r][c];
//             if (tile >= 0) {
//                 let tileRow = Math.floor(tile / tilesPerRow);
//                 let tileCol = Math.floor(tile % tilesPerRow);
//                 context.drawImage(backgroundImage,
//                     tileCol * tileSize, tileRow * tileSize, tileSize, tileSize,
//                     c * tileSize, r * tileSize, tileSize, tileSize);
//             }
//         }
//     }

//     context.drawImage(playerImage,
//         player.width * player.frameX, player.height * player.frameY, player.width, player.height,
//         player.x, player.y, player.width, player.height);
    
    // if ((moveLeft || moveRight) &&
    // !( moveRight && moveLeft) && ! player.in_air) {
    //     player.frameX = (player.frameX + 1) % 6;
    // }

    if (moveLeft) {
        if (player.x < 0) {
            moveLeft = false;
        } else {
            // player.xChange = player.xChange - 1;
            // player.frameY = 3;
            player.x = player.x - 7;
        }
    }
    if (moveRight) {
        if (player.x + player.width > canvas.width) {
            moveRight = false;
        } else {
            // player.xChange = player.xChange + 1;
            // player.frameY = 1;
            player.x = player.x + 7;
        }   
    }
    if (moveUp) {
        if (player.y < 0) {
            moveUp = false;
        } else {
            // player.yChange = player.yChange - 1;
            player.y = player.y - 7;
        }
    }
    if (moveDown) {
        if (player.y + player.height > canvas.height) {
            moveDown = false;
        } else {
            // player.yChange = player.yChange + 1;
            player.y = player.y + 7;
        }
    }


    for (let e of entities) {
        if (player_dmg_received(e)) {
            player["hp"] = player["hp"] - 1;
            if (player["hp"] === 0) {
                stop("Game Over");
            }
            return;
        }
    }


    for (let coin of coins) {
        if (coin_collect(coin)) {
            coinIndex = coins.indexOf(coin);
            coins.splice(coinIndex, 1);
            player["score"] = player["score"] + 1;
        }
    }

    // player.x = player.x + player.xChange;
    // player.y = player.y + player.yChange;

    // player.yChange = player.yChange + 1.5;
    // player.xChange = player.xChange * 0.8;
    // player.yChange = player.yChange * 0.8;

    // if (player.y + player.height > floor) {
    //     player.in_air = false;
    //     player.y = floor - player.height;
    //     player.yChange = 0;
    // }

}


function randint(min, max) {
    return Math.round(Math.random() * (max - min)) + min;
}

function activate(event) {
    let key = event.key;
    if (key === "ArrowLeft") {
        moveLeft = true;
    } else if (key === "ArrowUp") {
        moveUp = true;
    } else if (key === "ArrowRight") {
        moveRight = true;
    } else if (key === "ArrowDown") {
        moveDown = true;
    } else if (key === "a") {
        attack = true;
    }
}

function deactivate(event) {
    let key = event.key;
    if (key === "ArrowLeft") {
        moveLeft = false;
    } else if (key === "ArrowUp") {
        moveUp = false;
    } else if (key === "ArrowRight") {
        moveRight = false;
    } else if (key === "ArrowDown") {
        moveDown = false;
    } else if (key === "a") {
        attack = false;
    }
}

function load_assets(assets, callback) {
    let num_assets = assets.length;
    let loaded = function() {
        console.log("loaded");
        num_assets = num_assets - 1;
        if (num_assets === 0) {
            callback();
        }
    };
    for (let asset of assets) {
        let element = asset.var;
        if (element instanceof HTMLImageElement ) {
            console.log("img")
            element.addEventListener("load", loaded, false);
        }
        else if (element instanceof HTMLAudioElement ) {
            console.log("audio");
            element.addEventListener("canplaythrough", loaded, false);
        }
        element.src = asset.url
    }
}

function player_dmg_received(enemies) {
    if (player.x + player.width < enemies.x || enemies.x + 12 < player.x || player.y > enemies.y + 18 || 
        enemies.y > player.y + player.height) {
        return false;
    } else {
        return true;
    }
}

function coin_collect(coin) {
    if (player.x + player.width < coin.x || coin.x + 15 < player.x || player.y > coin.y + 15 || 
        coin.y > player.y + player.height) {
        return false;
    } else {
        return true;
    }
}

function stop(outcome) {
    window.removeEventListener("keydown", activate, false);
    window.removeEventListener("keyup", deactivate, false);
    window.cancelAnimationFrame(request_id);
    let outcome_element = document.querySelector("#outcome");
    outcome_element.innerHTML = outcome;
}