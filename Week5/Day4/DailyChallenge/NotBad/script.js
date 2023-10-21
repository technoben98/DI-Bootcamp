// let sentence = 'This dinner is not that bad ! You cook well'
// let sentence = 'This movie is not so bad !'
let sentence = 'This dinner is bad !'
sentence = sentence.split(" ")
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");
if (wordNot !=-1 && wordBad != -1){
    if (wordNot < wordBad){
    sentence.splice(wordNot, wordBad-wordNot +1, "good")
    console.log(sentence.join(" "))
} 
}else{
    console.log(sentence.join(" "))
}