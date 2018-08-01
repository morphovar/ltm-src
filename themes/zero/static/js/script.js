window.onload = function() {

/*LIST SORTING--------------*/
  var listElements = document.querySelectorAll('#archive ul li');
  var filters = document.getElementsByClassName('filter');

  for (var i = 0; i < filters.length; i++) {
      filters[i].addEventListener('click', sort, false);
  }

  function sort() {
    for (var j = 0; j < filters.length; j++) {
        filters[j].classList.remove('active');
    }
    this.classList.add('active');
    this.classList.toggle('desc');
    this.classList.toggle('asc');

    var type = (this).id;
    console.log(type)
    switch (type) {
      case "title":
          tinysort(listElements,{selector:'.entry-title',order:(this.isAsc=!this.isAsc)?'asc':'desc'});
          break;
      case "date":
          tinysort(listElements,{selector:'time',attr:'datetime',order:(this.isAsc=!this.isAsc)?'asc':'desc'});
          break;
      case "cat":
          tinysort(listElements,{selector:'.category',order:(this.isAsc=!this.isAsc)?'asc':'desc'});
          break;
    }
  }


/*FOOTNOTES--------------*/
  //generate footnote


/*SERVER DATA--------------*/
  // var url = "https://solar.vvvvvvaria.org/api/stats.json" //insert updated URL

  // $.getJSON(url, function(data) {

  //   var stats=[];
  //   $.each(data, function(key, val) {
  //       stats.push( "<li id='" + key + "'>" + key + ": " + val + "</li>" );
  //   });
  //   $( "<ul/>", {
  //       "class": "stats",
  //       html: stats.join( "" )
  //   }).appendTo( ".data" );
  //   //battery level background
  //   var level = data.bat_capacity;
  //   console.log(level);
  //   $('#battery').css('height',level);
  //   //status
  //   var status;
  //   if (data.ac_used=="no"){
  //     status = "It&rsquo;s dark or cloudy"
  //   }else{
  //     status = "The sun is shining"
  //   }
  //   $('#status').html(status);
  //   //uptime
  //   var uptime = data.uptime;
  //   $('#uptime').html(uptime);

  // });

/*CLOCK--------------*/
  // var time;
  // function calcTime(offset) {
  //     d = new Date();
  //     utc = d.getTime() + (d.getTimezoneOffset() * 60000);
  //     localdate = new Date(utc + (3600000*offset));
  //     time = localdate.toLocaleString();
  //     $('#time').html(time);
  // }
  //
  // setInterval(function(){
  //   calcTime(2);
  // },1000);

/*EXTERNAL LINKS--------------*/
  // function externalLinks() {
  //   for(var c = document.getElementsByTagName("a"), a = 0;a < c.length;a++) {
  //     var b = c[a];
  //     b.getAttribute("href") && b.hostname !== location.hostname && (b.target = "_blank")
  //   }
  // }
  // externalLinks();


}
