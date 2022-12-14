var x = 2
var y = 3
var total = x + y
var breakline = "<br/>"
document.write(total)
document.write(breakline)
document.write(typeof "John")
document.write(breakline)

if (total == 5){
    document.write("Total is equal to 5")
    document.write(breakline)
}


var grade = 'A';
document.write("<h1>Entering switch block</h1><br />");
switch (grade) {
    case 'A': document.write("Good job<br />");
    break;

    case 'B': document.write("Pretty good<br />");
    break;

    case 'C': document.write("Passed<br />");
    break;

    case 'D': document.write("Not so good<br />");
    break;

    case 'F': document.write("Failed<br />");
    break;

    default:  document.write("Unknown grade<br />")
}
document.write("<h1>Exiting switch block</h1>");
document.write(breakline)

var count = 0;
document.write("<h1>Starting Loop </h1>");

while (count < 10) {
    document.write("Current Count : " + count + "<br />");
    count++;
}

document.write("<h1>Loop stopped!</h1>");
document.write(breakline)

count = 0
document.write("<h1>Starting Loop" + "</h1><br />");

for(count = 0; count < 10; count++) {
    document.write("Current Count : " + count );
    document.write("<br />");
}         
document.write("<h1>Loop stopped!</h1>");