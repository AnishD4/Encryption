// script.js


const data = [
    ["fvmzobgqba", "REVOLUTION", "OCTAL+ROT13"],
    ["DISCOVERY", "DISCOVERY", "CHARCODE"],
    ["434S4R56454R54494S4R", "CONVENTION", "HEXADECIMAL+ROT13"],
    ["434f4e464944454e4345", "CONFIDENCE", "BINARY+CHARCODE"],
    ["EH0LDCNWCIV4J3Q=", "INTERACTIVE", "ROT47+BASE64"],
    ["TRANSCRIBE", "TRANSCRIBE", "CHARCODE"],
    ["HAPCVARFF", "HAPPINESS", "ROT13"],
    ["SU5WSVNJQKXF", "INVISIBLE", "BASE64"],
    ["--. . -. . .-. .- - .. --- -.", "GENERATION", "MORSE"],
    ["``_ `_` `a_ `a_ ``` ``e `_d `ab `ab``", "HAPPINESS", "OCTAL+ROT47"],
    ["526B3956546B524256456C5054673D3D", "FOUNDATION", "BASE64+HEXADECIMAL"],
    ["113 122 103 125 107 123 103 117 112 065 107 105 066 122 062 132", "TECHNOLOGY", "BASE32+OCTAL"],
    ["QPRZV#~&}S", "BACKGROUND", "ROT47"],
    ["01000110 01001111 01010010 01001101 01001001 01000100 01000001 01000010 01001100 01000101", "FORMIDABLE", "BINARY+ATBASH"],
    ["KEYUURSRKZJEUVTLNRKVOUJ5HU======", "CREATIVITY", "BASE64+BASE32"],
    ["``` ``E ``E ``F `AE `_` `AC ``` ``F ``E", "INNOVATION", "OCTAL+ROT47"],
    ["3730203739203832203737203733203638203635203636203736203639", "FORMIDABLE", "CHARCODE+HEXADECIMAL"],
    ["FGEHPGHER", "STRUCTURE", "ROT13"],
    ["414348494556454D454E54", "ACHIEVEMENT", "HEXADECIMAL"],
    ["49 50 51 32 49 48 53 32 49 49 54 32 49 50 51 32 49 48 49 32 49 50 52 32 49 49 49 32 49 49 55 32 49 49 54", "SENSATION", "OCTAL+CHARCODE"],
    ["GEYDEIBRGAYSAMJQGMQDCMJTEAYTANZAGEZDEIBRGE3SAMJSGUQDCMJWEAYTANA=", "BACKGROUND", "OCTAL+BASE32"],
    ["LIGHTNING", "114 111 107 110 124 116 111 116 107", "OCTAL"],
    ["01001010 01010110 01000001 01010101 00110100 01010011 01001011 01010001 01001011 01010110 01000111 01000101 01000011 01010110 01000011 01000110", "MANIPULATE", "BASE32+BINARY"],
    ["_`____`` _`__```` _`__``_` _`_`____ _`_____` _`_`__`_ _`__`__` _`_`__`` _`__```` _`__```_", "COMPARISON", "BINARY+ROT47"],
    ["MECHANISM", "MECHANISM", "CHARCODE"],
    ["-- .- -. .. .--. ..- .-.. .- - .", "MANIPULATE", "MORSE"],
    ["73 78 72 85 50 85 67 66 75 74 69 86 71 84 50 79", "COMPARISON", "BASE32+CHARCODE"],
    ["01000111 01000101 01001110 01000001 01000110 01010000 01000101 01010110 01001111 01010010", "TRANSCRIBE", "ROT13+BINARY"],
    ["106 117 125 116 104 101 124 111 117 116", "FOUNDATION", "OCTAL"],
    ["111 116 116 117 126 101 124 111 117 116", "INNOVATION", "OCTAL"],
    ["FROPRGZYLV", "FORMIDABLE", "ATBASH"],
    ["{X|X%P%X~}", "LIMITATION", "ROT47"],
    ["00110110 00110111 00100000 00110111 00110010 00100000 00110110 00111001 00100000 00110111 00110111 00100000 00110111 00110011 00100000 00111000 00110011 00100000 00111000 00110100 00100000 00111000 00110010 00100000 00111000 00111001", "CHEMISTRY", "CHARCODE+BINARY"],
    ["3031303030313030203031303031303031203031303130303130203031303030313031203031303030303131203031303130313030203031303031303031203031303031313131203031303031313130", "DIRECTION", "BINARY+HEXADECIMAL"],
    ["544543484E4F4C4F4759", "TECHNOLOGY", "HEXADECIMAL"],
    ["434F4E464944454E4345", "CONFIDENCE", "HEXADECIMAL"],
    ["GAYTAMBRGEYDAIBQGEYDAMJQGAYSAMBRGAYDCMJQGEQDAMJQGAYTAMBREAYDCMBRGAYTAMBAGAYTAMBQGAYDCIBQGEYDCMBRGAYCAMBRGAYDCMBQGEQDAMJQGAYTCMJREAYDCMBQGEYTCMA=", "LIMITATION", "BINARY+BASE32"],
    ["IRCUMSKOJFKEST2O", "DEFINITION", "BASE32"],
    ["126 117 103 101 102 125 114 101 122 131", "VOCABULARY", "OCTAL+ROT13"],
    ["066 065 040 067 066 040 067 061 040 067 071 040 070 062 040 067 063 040 070 064 040 067 062 040 067 067", "ALGORITHM", "CHARCODE+OCTAL"],
    ["ACHIEVEMENT", "ACHIEVEMENT", "ROT13"],
    ["103 117 116 106 111 104 105 116 103 105", "CONFIDENCE", "OCTAL"],
    ["ZNAVCHYNGR", "MANIPULATE", "ROT13"],
    ["C6C7C6C6CDCBDCCHC7C6", "CONNECTION", "HEXADECIMAL+ROT47"],
    ["Q09NUEFSSVNPTg==", "COMPARISON", "BASE64"],
    ["123 124 122 125 103 124 125 122 105", "STRUCTURE", "OCTAL"],
    ["01000010 01000001 01000011 01001011 01000111 01010010 01001111 01010101 01001110 01000100", "BACKGROUND", "BINARY"],
    [".- .-- .- .-. . -. . ... ...", "AWARENESS", "MORSE"],
    ["01000001 01010111 01000001 01010010 01000101 01001110 01000101 01010011 01010011", "AWARENESS", "BINARY"],
    ["WVURMRGRLM", "DEFINITION", "ATBASH"]
];
let num = 0;
let tries = 5;

function updateTryCounter() {
    document.getElementById('tryCounter').innerText = 'Tries: ' + tries;
}

function newProblem() {
    num = Math.floor(Math.random() * data.length);
    document.getElementById('EncryptedText').innerText = data[num][0];
    document.getElementById('answerInput').value = '';
    document.getElementById('result').innerText = '';
    document.getElementById('hint').innerText = '';
    tries = 5;
    updateTryCounter();
}

function checkAnswer() {
    const userInput = document.getElementById('answerInput').value.trim();
    if (tries <= 0) {
        document.getElementById('result').innerText = `No more tries left! The Answer was:${data[num][1]} .Here a new Problem `;
        setTimeout(newProblem, 1200);

    } else if (userInput === data[num][1]) {
        document.getElementById('result').innerText = 'Correct! Next challenge...';
        setTimeout(newProblem, 1200);
    } else {
        document.getElementById('result').innerText = 'Try again!';
        tries--;
        updateTryCounter();
    }
}

function showHint() {
    document.getElementById('hint').innerText = 'Hint: ' + data[num][2];
}

document.addEventListener('DOMContentLoaded', () => {
    newProblem();
    document.getElementById('checkBtn').onclick = checkAnswer;
    document.getElementById('hintBtn').onclick = showHint;
    document.getElementById('answerInput').addEventListener('keydown', function(e) {
        if (e.key === 'Enter') checkAnswer();
    });
});




