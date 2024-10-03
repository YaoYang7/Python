let canvas;
let context; 

let fpsInterval = 1000 / 30;
let now;
let then = Date.now();
let request_id;

let entities = [];
let big_entities = [];
let player = {
    x : 0,
    y : 0,
    width : 32,
    height : 32,
    frameX : 0,
    frameY : 0,
    xChange : 0,
    yChange : 0,
    score : 0,
    hp : 10
};
let coins = [];
let counter = 0;


let moveLeft = false;
let moveRight = false;
let moveUp = false;
let moveDown = false;
let attack = false;

let entitiesImage = new Image();
let playerImage = new Image();


let tilesPerRow = 6;
let tileSize = 16;

document.addEventListener("DOMContentLoaded", init, false);

function init() {
    canvas = document.querySelector("canvas");
    context = canvas.getContext("2d");

    player.x = canvas.width / 2;
    player.y = canvas.height / 2;

    window.addEventListener("keydown", activate, false);
    window.addEventListener("keyup", deactivate, false);

    entitiesImage.src = "entities.png";

    load_assets([
        {"var": entitiesImage, "url" : "entities.png"},
        {"var": playerImage, "url" : "player.png"}
    ], draw);
}

function draw() {
    request_id = window.requestAnimationFrame(draw);
    let now = Date.now();
    let elapsed = now - then;
    if (elapsed <= fpsInterval) {
        return;
    }
    then = now - (elapsed % fpsInterval);

    if (entities.length < 8) {
        // image size = 24 x 24
        let e = {
            x : randint(0, canvas.width),
            y : randint(0, canvas.height),
            width : 24,
            height : 24,
            xChange : randint(-8, 8),
            yChange : randint(-8, 8),
            frameX : 0,
            frameY : 1.5,
            index : entities.length - 1
        };
        entities.push(e)
    }
    context.clearRect(0, 0, canvas.width, canvas.height);
    // image size = 48 x 48
    context.fillStyle = "cyan";
    context.drawImage(playerImage, player.width*player.frameX, player.height*player.frameY, player.width, player.height,
        player.x, player.y, player.width, player.height);

    context.font = "30px serif";
    context.fillStyle = "pink";
    context.fillText(player.hp, 50, 30);
    context.fillText("HP:", 3, 30);
    context.fillText(player.score, 90, 60);
    context.fillText("Score:", 3, 60);

    context.fillStyle = "red";
    for (let entity of entities) {
        while (entity.x === player.x && entity.y === player.y) {
            entity.x = randint(0, canvas.width);
            entity.y = randint(0, canvas.height);
        };
        context.drawImage(entitiesImage, entity.width*entity.frameX, entity.height*entity.frameY, entity.width, entity.height,
            entity.x, entity.y, entity.width, entity.height);
    }
    if (counter > 2) {
        for (let entity of entities) {
            if (entity.frameX === 0) {
                entity.frameX = 1.2;
            } else {
                entity.frameX = 0;
            }
        }
        counter = 0;
    } else {
        counter += 1;
    }


    context.fillStyle = "yellow";
    if (coins.length < 5) {
        let coin = {
            x : randint(0, canvas.width),
            y : randint(0, canvas.height),
            size : 16
        };
        coins.push(coin);
    }
    for (let coin of coins) {
        while (coin.x === player.x && coin.y === player.y || coin.x === entities.x && coin.y === entities.y) {
            coin.x = randint(0, canvas.width);
            coin.y = randint(0, canvas.height);
        };
        context.fillRect(coin.x, coin.y, coin.size, coin.size);
    }
    
    for (let entity of entities) {
        if (entity.y + entity.height > canvas.height){
            entity.y = canvas.height - entity.height;
            entity.yChange = -7;
        } else if (entity.y < 0){
            entity.y = 0;
            entity.yChange = 7;
        } else if (entity.x + entity.width > canvas.width){
            entity.x = canvas.width - entity.width;
            entity.xChange = -7;
        } else if (entity.x < 0){
            entity.x = 0;
            entity.xChange = 7;
        } 
        
        entity.x = entity.x + entity.xChange;
        entity.y = entity.y + entity.yChange;
    }

    if (moveLeft) {
        if (player.x < 0) {
            moveLeft = false;
        } else {
            player.x = player.x - 7;
            player.frameY = 1;

            if (player.frameX === 2) {
                player.frameX = 0;
            } else {
                player.frameX += 1;
            }
        }
    }
    if (moveRight) {
        if (player.x + player.width > canvas.width) {
            moveRight = false;
        } else {
            player.x = player.x + 7;
            player.frameY = 2;
            if (player.frameX === 2) {
                player.frameX = 0;
            } else {
                player.frameX += 1;
            }
        }   
    }
    if (moveUp) {
        if (player.y < 0) {
            moveUp = false;
        } else {
            player.y = player.y - 7;
            player.frameY = 3;
            if (player.frameX === 2) {
                player.frameX = 0;
            } else {
                player.frameX += 1;
            }
        }
    }
    if (moveDown) {
        if (player.y + player.height > canvas.height) {
            moveDown = false;
        } else {
            player.y = player.y + 7;
            player.frameY = 0;
            if (player.frameX === 2) {
                player.frameX = 0;
            } else {
                player.frameX += 1;
            }
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
            let coinIndex;
            coinIndex = coins.indexOf(coin);
            coins.splice(coinIndex, 1);
            player["score"] = player["score"] + 1;
        }
    }
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

function player_dmg_received(entities) {
    if (player.x + player.width < entities.x ||
        entities.x + entities.width < player.x || 
        player.y > entities.y + entities.height || 
        entities.y > player.y + player.height) {
        return false;
    } else {
        return true;
    }
}


function coin_collect(coin) {
    if (!(player.x > coin.x + coin.size) &&
    !(player.x + player.width < coin.x) &&
    !(player.y > coin.y + coin.size) &&
    !(player.y + player.height < coin.y)) {
        return true;
    } else {
        return false;
    }
}

function stop(outcome) {
    window.removeEventListener("keydown", activate, false);
    window.removeEventListener("keyup", deactivate, false);
    window.cancelAnimationFrame(request_id);
    let outcome_element = document.querySelector("#outcome");
    outcome_element.innerHTML = outcome;
}