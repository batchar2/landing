particlesJS.load('home', '/static/landing_page/js/particles.json', function() {
  console.log('callback - particles.js config loaded');
});

$(document).ready(function() {
	$('.plan-button a').on('click', function () {
		var plan = $(this).data("plan");
		$('#type-plan').attr("value", plan);
		$('#message').text('>>> Selected plan: ' + plan + '\r\n' + 'Hello! ');

	})
	$('.slider').slick({
	    slidesToShow: 1,
	    slidesToScroll: 1,
	    dots: true,
	    infinite: true,
	    cssEase: 'linear'
	});

	$('.slidersecond').slick({
	    slidesToShow: 1,
	    slidesToScroll: 1,
	    dots: true,
	    infinite: true,
	    cssEase: 'linear'
	});
	$('.slider__item').zoom();




	$('#mail-form').on('submit', function(e) {
        const response = grecaptcha.getResponse();
        if(response.length == 0) {
            //reCaptcha not verified
            alert("please verify you are humann!");
            e.preventDefault();
            return false;
        }

        console.log('response111>>>>', response)
        // yes

		function isEmail(v) {
  			var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  			return regex.test(v);
		}

		var name = $('#name').val();
		var email = $('#email').val();
		var message = $('#message').val();
		var plan = $('#type-plan').val() || ' ';
		console.log(name)
		console.log(email)
		console.log(message)

        // if (message.length )

		if (name.length && email.length && message.length && isEmail(email)) {
			$('#name').css({'border': ''});
			$('#email').css({'border': ''});
			$('#message').css({'border': ''});

            $('#contact-form-id').html('<div style="margin-left: auto; margin-right:auto;"> <img width=64 src="/static/landing_page/img/loader.gif"/> </div>');

			$.get('mail',
				{
					'name': name,
					'plan': plan,
					'email': email,
					'message': message,
				}
			).done(function() {
    			$('#contact-form-id').html('<h2 style="color:blue;">Thank you! We will contact you as soon as possible.</h2>');
  			})
  			.fail(function() {
    			$('#contact-form-id').html('<h2 style="color:red;">Excuse me, I think there\'s been a mistake.</h2>');
  			});
		} else {
			if (!name.length) {
				$('#name').css({'border': '1px solid red'});
			}
			if (!email.length || !isEmail(email)) {
				$('#email').css({'border': '1px solid red'});
			}
			if (!message.length) {
				$('#message').css({'border': '1px solid red'});
			}
		}
		e.preventDefault();
		return false;
	});


})
