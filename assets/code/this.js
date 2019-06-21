function log() {
  console.log(this.x);
}
function Who(x) {
  this.x = x;
}
Who.prototype.log = log;
Who.prototype.logF = function(){console.log(this.x);};
Who.prototype.logF2 = function(){log();};
Who.prototype.logCall = function(who){log.call(who);};
x = 1;
me = new Who(2);
logMe = me.log;
you = new Who(3);

// Try guessing what will be printed
console.log(this.x);            // 1
log();                          // 1
logMe();                        // 1
me.log();                       // 2
me.logF();                      // 2
me.logF2();                     // 1
me.logCall(you);                // 3
