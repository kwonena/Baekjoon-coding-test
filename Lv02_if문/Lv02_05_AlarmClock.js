let hour = 0;
let minute = 30;
let chang;

if(minute > 45) {
    chang = minute - 45;
    console.log(`${hour} hour ${chang} minute`);
} else {
    if(hour <= 0) {
        hour += 24;
    }
    hour -= 1;
    minute += 60;
    chang = minute - 45;
    console.log(`${hour} hour ${chang} minute`);
}

