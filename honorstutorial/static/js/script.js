function myFunction() {
    var x = document.getElementById("navlinks_id");
    var y = document.getElementById("navContainer");
    var menuIcon = document.getElementById("menuIcon");
    if (x.className === "navlinks") {
      x.className += " responsive";
      menuIcon.innerHTML= "&#10005"
    } else {
      x.className = "navlinks";
      menuIcon.innerHTML= "&#9776;"
    }
  }



  ('.topnav a').click(function(){   
    $(this).addClass('active');
    $(this).siblings().removeClass('active');
   });