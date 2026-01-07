#I. Jenny's secret message
function greet(name){
  if(name === "Johnny")
    return "Hello, my love!";
  return "Hello, " + name + "!";
}

#-----------------------------------------------------------------
#II. Find The Distance Between Two Points
function distance(x1, y1, x2, y2){
  return Math.round(Math.hypot(x2 - x1, y2 - y1) * 100) / 100;
}

#You have passed all of the tests!
#But I got an error on the site: "You cannot submit your solution at the moment because the kata is not published."

#-----------------------------------------------------------------
#III. No yelling!
def filter_words(st):
    return " ".join(st.split()).lower().capitalize()

#-----------------------------------------------------------------
#IV. Convert a Number to a String
function numberToString(num) {
  return String(num);
}

#-----------------------------------------------------------------
#V. Reversing Words in a String
function reverse(string){
  return string.trim().split(" ").reverse().join(" ");
}

#-----------------------------------------------------------------
#VI. Reverse List Order
function reverseList(list) {
  return list.reverse();
}

#-----------------------------------------------------------------
#VII. Multiples of 3 or 5
function solution(number){
  if(number < 0) return 0;
  let sum = 0;
  for(let i = 0; i < number; i++){
    if(i % 3 === 0 || i % 5 === 0) sum += i;
  }
  return sum;
}

#-----------------------------------------------------------------
#VIII. Will you make it?
const zeroFuel = (distanceToPump, mpg, fuelLeft) => {
  return mpg * fuelLeft >= distanceToPump;
};

#-----------------------------------------------------------------
#IX. Are You Playing Banjo?
function areYouPlayingBanjo(name) {
  if(name[0].toLowerCase() === "r")
    return name + " plays banjo";
  return name + " does not play banjo";
}

#-----------------------------------------------------------------
#X. Convert boolean values to strings 'Yes' or 'No’
function boolToWord(bool){
  return bool ? "Yes" : "No";
}

#-----------------------------------------------------------------
#XI. Counting sheep
def count_sheeps(sheep):
    return sum(1 for s in sheep if s is True)

#-----------------------------------------------------------------
#XII. Is this my tail?
def correct_tail(body, tail):
    return body.endswith(tail)



