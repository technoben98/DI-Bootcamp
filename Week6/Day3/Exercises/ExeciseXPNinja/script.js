const mergeWords = (string) => {
  return (nextString) => {
    if (nextString === undefined) {
      return string;
    } else {
      return mergeWords(string + " " + nextString);
    }
  };
};
console.log(mergeWords("There")("is")("no")("spoon.")());
