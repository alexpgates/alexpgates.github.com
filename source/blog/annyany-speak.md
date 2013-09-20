Title: "Hello world! ... Hello&nbsp;world!" with annyang.js &amp;&nbsp;speak.js
Date: 2013-09-19
Summary: Combining annyang.js and speak.js to build a web site that listens to what you say and repeats it back to you.
Slug: annyang-js-and-speak-js
Tags: Javascript

[Hobbs](http://velvetcache.org) sent me a link to [annyang.js](https://www.talater.com/annyang/) by [Tal Ater](https://github.com/TalAter) because he thought it'd be right up my alley. (He's right! It is! And it's not just for the [Arrested Development reference](https://twitter.com/talater/status/380059244017356800)!)

### annyang.js

[Annyang](https://www.talater.com/annyang/) is "a tiny javascript library that lets your users control your site with voice commands." It can do a lot for weighing in less than 1k. Annyang uses browser-based WebSpeech APIs and your computers microphone to translate speech-to-text and respond according to your commands. Annyang handles some pretty complex commands using variables, wildcards, optional ignoring, etc. There's a lot of great possibilities with annyang, and when I have some extra time I plan on using it to control a set of [Hue lights](https://www.meethue.com).

I don't have a lot of extra play time at the moment, but I wanted to quickly throw something together to try annyang. 

### speak.js

[Speak.js](https://github.com/kripken/speak.js/), by [Alon Zakai](https://github.com/kripken) is a javascript port of the eSpeak speech synthesizer. Speak.js enables text-to-speech in the browser using JavaScript and HTML5.

### Putting them together

Combining annyang.js and speak.js seemed like fun, so I created <a href="http://webjam.org/speak/" target="_blank">a little demo</a>. Annyang.js listens to what you say, and speak.js repeats it back to you.

	<html>
	  <head>
	    <script src="speakClient.js"></script>
	    <script src="annyang.min.js"></script>
	  </head>
	  <body>
	    <div id="audio"></div>
	  </body>
	  <script type="text/javascript">
		if (annyang) {
		  	
		  var sayThis = function(repeat) {
		  	speak(repeat);
		  }

		  // Let's define a command.
		  var commands = {
		    '*repeat': sayThis
		  };

	      // Turn on debugging for the console
		  annyang.debug();

		  // Initialize annyang with our commands
		  annyang.init(commands);

		  // Start listening.
		  annyang.start();
		}
	  </script>
	</html>

In the above example, we begin by checking to see if annyang will work in this browser. If so, we define a function called `sayThis ` that takes the output from our wildcard variable in annyong called `*repeat` and uses the speak.js function `speak()` to output a .wav file to `<div id="audio"></div>`.

<a href="http://webjam.org/speak/" target="_blank">Try the demo &raquo;</a>