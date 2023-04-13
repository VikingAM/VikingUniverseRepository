// Hide submenus
	$('#body-row .collapse').collapse('hide'); 

	// Collapse/Expand icon
	$('#collapse-icon').addClass('fa-angle-double-left'); 

	// Collapse click
	// $('[data-toggle=sidebar-colapse]').click(function() {
	//     SidebarCollapse();
	// });

	function SidebarCollapse () {
	    $('.menu-collapsed').toggleClass('d-none');
	    $('.sidebar-submenu').toggleClass('d-none');
	    $('.submenu-icon').toggleClass('d-none');
	    $('#sidebar-container').toggleClass('sidebar-expanded sidebar-collapsed');
	    // Treating d-flex/d-none on separators with title
	    var SeparatorTitle = $('.sidebar-separator-title');
	    if (SeparatorTitle.hasClass('d-flex') ) {
	        SeparatorTitle.removeClass('d-flex');
	        $(".logo_full").hide();
	        $(".logo_small").show();
	        $(".navbar-icons").css("margin-left", "30%");
	    } else {
	        SeparatorTitle.addClass('d-flex');
	        $(".logo_full").show();
	        $(".logo_small").hide();
	        $(".navbar-icons").css("margin-left", "0%");
	    }
	    
	    // Collapse/Expand icon
	    $('#collapse-icon').toggleClass('fa-angle-double-left fa-angle-double-right');
	}



	$(".main-container").hover(function(){
		$('.menu-collapsed').toggleClass('d-none');
	    $('.sidebar-submenu').toggleClass('d-none');
	    $('.submenu-icon').toggleClass('d-none');
	    $('#sidebar-container').toggleClass('sidebar-expanded sidebar-collapsed');
	    // Treating d-flex/d-none on separators with title
	    var SeparatorTitle = $('.sidebar-separator-title');
	    if (SeparatorTitle.hasClass('d-flex') ) {
	       	
	    } else {
	    	console.log("here2");
	        SeparatorTitle.addClass('d-flex');
	        $(".logo_full").hide();
	        $(".logo_small").show();
	        $(".navbar-icons").css("margin-left", "30%");
	    }
	    // Collapse/Expand icon
	    $('#collapse-icon').toggleClass('fa-angle-double-left fa-angle-double-right');
	})

	$(".main-container").mouseout(function(){
		$(".logo_full").show();
        $(".logo_small").hide();
        $(".navbar-icons").css("margin-left", "0%");
	})