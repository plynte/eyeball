var Lock = function () {

    return {
        //main function to initiate the module
        init: function () {

             $.backstretch([
		        "static/images/bg/1.jpg",
		        "static/images/bg/2.jpg",
		        "static/images/bg/3.jpg",
		        "static/images/bg/4.jpg"
		        ], {
		          fade: 1000,
		          duration: 8000
		      });
        }

    };

}();