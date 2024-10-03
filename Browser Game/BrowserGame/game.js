let canvas;
let context; 

let fpsInterval = 1000 / 30;
let now;
let then = Date.now();
let request_id;

let entities = [];
let big_entities = [];
let big_entities_2 = [];
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
    hp : 30
};
let coins = [];
let counter = 0;
let bigCounter = 0;
let bigCounter_2 = 0;


let moveLeft = false;
let moveRight = false;
let moveUp = false;
let moveDown = false;
let attack = false;

let entitiesImage = new Image();
let big_entitiesImage = new Image();
let playerImage = new Image();
let coinImage = new Image();
let hpImage = new Image();
let hp_boarderImage = new Image();
let hp_backImage = new Image();

document.addEventListener("DOMContentLoaded", init, false);

function init() {
    canvas = document.querySelector("canvas");
    context = canvas.getContext("2d");

    player.x = canvas.width / 2;
    player.y = canvas.height / 2;

    window.addEventListener("keydown", activate, false);
    window.addEventListener("keyup", deactivate, false);

    playerImage.src = "player.png";
    entitiesImage.src = "entities.png";
    coinImage.src = "coin.png";
    hpImage.src = "hp.png";
    hp_boarderImage.src = "hp_boarder.png";
    hp_backImage.src = "hp_back.png";

    load_assets([
        {"var": entitiesImage, "url" : "entities.png"},
        {"var": big_entitiesImage, "url" : "entities.png"},
        {"var": playerImage, "url" : "player.png"},
        {"var": coinImage, "url" : "coin.png"},
        {"var": hpImage, "url" : "hp.png"},
        {"var": hp_boarderImage, "url" : "hp_boarder.png"},
        {"var": hp_backImage, "url" : "hp_back.png"}
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
        let e = {
            x : randint(0, canvas.width),
            y : randint(0, canvas.height),
            width : 26,
            height : 26,
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
    context.fillText("HP", 3, 35);
    context.drawImage(hp_boarderImage, 50, 0);
    context.drawImage(hp_backImage, 50, 0);
    if (player.hp === 30) {
        context.drawImage(hpImage, 50, 0);
    } else if (player.hp < 30 && player.hp >= 20) {
        context.drawImage(hpImage, 51, 0, 300, 50);
    } else if (player.hp < 20 && player.hp >= 10) {
        context.drawImage(hpImage, 52, 0, 200, 50);
    } else if (player.hp < 10 && player.hp >= 1) {
        context.drawImage(hpImage, 53, 0, 100, 50);
    } else if (player.hp <= 0) {
        context.drawImage(hpImage, 55, 0, 0, 50);
    }
    context.fillText(player.score, 90, 72);
    context.fillText("Score:", 3, 70);

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
                entity.frameX = 1;
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
        context.drawImage(coinImage, coin.x, coin.y, coin.size, coin.size);
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

    if (player.score >= 10 ) {
        if (big_entities.length < 8) {
            let big_entity = {
                x : randint(0, canvas.width),
                y : randint(0, canvas.height),
                width : 26,
                height : 26,
                xChange : randint(-12, 12),
                yChange : randint(-12, 12),
                frameX : 0,
                frameY : 0,
                index : big_entities.length - 1
            };
            big_entities.push(big_entity);
        }

        for (let big_entity of big_entities) {
            while (big_entity.x === player.x && big_entity.y === player.y) {
                big_entity.x = randint(0, canvas.width);
                big_entity.y = randint(0, canvas.height);
            };
            context.drawImage(big_entitiesImage, big_entity.width*big_entity.frameX, big_entity.height*big_entity.frameY, big_entity.width, big_entity.height,
                big_entity.x, big_entity.y, big_entity.width, big_entity.height);
        }

        for (let big_entity of big_entities) {
            if (big_entity.y + big_entity.height > canvas.height){
                big_entity.y = canvas.height - big_entity.height;
                big_entity.yChange = -12;
            } else if (big_entity.y < 0){
                big_entity.y = 0;
                big_entity.yChange = 12;
            } else if (big_entity.x + big_entity.width > canvas.width){
                big_entity.x = canvas.width - big_entity.width;
                big_entity.xChange = -12;
            } else if (big_entity.x < 0){
                big_entity.x = 0;
                big_entity.xChange = 12;
            } 
            
            big_entity.x = big_entity.x + big_entity.xChange;
            big_entity.y = big_entity.y + big_entity.yChange;
        }

        if (bigCounter > 2) {
            for (let big_entity of big_entities) {
                if (big_entity.frameX != 3) {
                    big_entity.frameX += 1;
                } else {
                    big_entity.frameX = 0;
                }
            }
            bigCounter = 0;
        } else {
            bigCounter += 1;
        }
        
        for (let big_entity of big_entities) {
            if (player_dmg_received(big_entity)) {
                player["hp"] = player["hp"] - 3;
                return;
            }
        }
    }

    if (player.score >= 20) {
        if (big_entities_2.length < 10) {
            let big_entity_2 = {
                x : randint(0, canvas.width),
                y : randint(0, canvas.height),
                width : 26,
                height : 26,
                xChange : randint(-12, 12),
                yChange : randint(-12, 12),
                frameX : 0,
                frameY : 0,
                index : big_entities_2.length - 1
            };
            big_entities_2.push(big_entity_2);
        }

        for (let big_entity_2 of big_entities_2) {
            while (big_entity_2.x === player.x && big_entity_2.y === player.y) {
                big_entity_2.x = randint(0, canvas.width);
                big_entity_2.y = randint(0, canvas.height);
            };
            context.drawImage(big_entitiesImage, big_entity_2.width*big_entity_2.frameX, big_entity_2.height*big_entity_2.frameY, big_entity_2.width, big_entity_2.height,
                big_entity_2.x, big_entity_2.y, big_entity_2.width, big_entity_2.height);
        }

        for (let big_entity_2 of big_entities_2) {
            if (big_entity_2.y + big_entity_2.height > canvas.height){
                big_entity_2.y = canvas.height - big_entity_2.height;
                big_entity_2.yChange = -12;
            } else if (big_entity_2.y < 0){
                big_entity_2.y = 0;
                big_entity_2.yChange = 12;
            } else if (big_entity_2.x + big_entity_2.width > canvas.width){
                big_entity_2.x = canvas.width - big_entity_2.width;
                big_entity_2.xChange = -12;
            } else if (big_entity_2.x < 0){
                big_entity_2.x = 0;
                big_entity_2.xChange = 12;
            } 
            
            big_entity_2.x = big_entity_2.x + big_entity_2.xChange;
            big_entity_2.y = big_entity_2.y + big_entity_2.yChange;
        }

        if (bigCounter_2 > 2) {
            for (let big_entity_2 of big_entities_2) {
                if (big_entity_2.frameX != 3) {
                    big_entity_2.frameX += 1;
                } else {
                    big_entity_2.frameX = 0;
                }
            }
            bigCounter_2 = 0;
        } else {
            bigCounter_2 += 1;
        }
        
        for (let big_entity of big_entities) {
            if (player_dmg_received(big_entity)) {
                player["hp"] = player["hp"] - 3;
                return;
            }
        }
    }

    if (player.hp < 0) {
        stop("You are dead! Your score: " + player["score"]);
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

function heal(item) {
    if (!(player.x > item.x + item.size) &&
    !(player.x + player.width < item.x) &&
    !(player.y > coin.y + item.size) &&
    !(player.y + player.height < item.y)) {
        return true;
    } else {
        return false;
    }
}