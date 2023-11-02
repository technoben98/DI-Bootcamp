function validateLetters(event) {
  const keyCode = event.keyCode || event.which;
  const key = String.fromCharCode(keyCode);
  const letterRegex = /^[A-Za-z]+$/;

  if (!letterRegex.test(key)) {
    event.preventDefault();
    return false;
  }
}
