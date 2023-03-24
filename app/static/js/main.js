var text = "We the team of LUMEN are extremely glad to inform you that, We have started working on our departmental annual magazine PHYONICS 2023, which showcases the academic and literacy achievements of students from our department along with that we provide the opportunity for students to express themselves and sharpen their creative skills through their writeups or articles .";
var i = 0;
var speed = 15;

    function type() {
      if (i < text.length) {
        document.getElementById("text").innerHTML += text.charAt(i);
        i++;
        setTimeout(type, speed);
      }
    }

    type();