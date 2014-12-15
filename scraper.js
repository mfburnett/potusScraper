var request = require('request');
var cheerio = require('cheerio');

var counter = 0;
var listofDates = [];

request('http://www.whitehouse.gov/briefing-room/speeches-and-remarks', function (err, response, html) {
	if (err) console.log(err);
	
	else {
		var $ = cheerio.load(html);
		
		var date = $('#content').find('.date-line').each(function(i, v) {
		  listofDates.push(v.children[0].data);
		});

		$('h3').children().each(function(index, value) {
		  var url = ('http://www.whitehouse.gov' + $(this).attr('href'));
	  	  request(url, function(e, r, html) {
		    var $ = cheerio.load(html);
				
		    var occurences = $('#content')
          	       .find('p')
          	       .text()
          	       .toLowerCase()
          	       .match(/ebola/g) || [];
          
		    console.log('Came from: ' + url + '\n' +listofDates[index] + '\n' +occurences.length);
		});
       	     });

    }
});

//Find logical way to get all links in a single category 
			
