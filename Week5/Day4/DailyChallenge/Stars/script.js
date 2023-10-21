let star = "*";
let stars = ""
for (let i = 0; i < 6; i++){
    stars+= " " + star
    console.log(stars)
}

for (let i = 0; i < 6; i++){
    let starsQuantity = i + 1
    let stars = ""
    for (let j = 0; j < starsQuantity; j++){
        stars = stars + " *"
    }
    console.log(stars)
}