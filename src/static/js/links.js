$('#uni-link').click(function(e) {
    e.preventDefault();
    var menu_items = document.querySelectorAll('#menu-universe.mainmenu > a.mainmenu__item');
    for (i = 0; i < menu_items.length; i++) {
        menu_items[i].style.opacity = 0;
    }

    // all menus are set to d-none
    $(".mainmenu").addClass("d-none");

    // the uni-menu
    $('#menu-universe').removeClass('d-none');
    
    // Main links animation.
    TweenMax.staggerTo(menu_items, 0.9, {
        ease: Quint.easeOut,
        startAt: {y: '50%', opacity: 0},
        y:"0%", 
        opacity:1
    }, 0.1);
});

$('#comm-link').click(function(e) {
    e.preventDefault();
    var menu_items = document.querySelectorAll('#menu-group.mainmenu > a.mainmenu__item');
    for (i = 0; i < menu_items.length; i++) {
        menu_items[i].style.opacity = 0;
    }

    // all menus are set to d-none
    $(".mainmenu").addClass("d-none");

    // the uni-menu
    $('#menu-group').removeClass('d-none');
    
    // Main links animation.
    TweenMax.staggerTo(menu_items, 0.9, {
        ease: Quint.easeOut,
        startAt: {y: '50%', opacity: 0},
        y:"0%", 
        opacity:1
    }, 0.1);
});

$('#story-link').click(function(e) {
    e.preventDefault();
    var menu_items = document.querySelectorAll('#menu-group.mainmenu > a.mainmenu__item');
    for (i = 0; i < menu_items.length; i++) {
        menu_items[i].style.opacity = 0;
    }

    // all menus are set to d-none
    $(".mainmenu").addClass("d-none");

    // the uni-menu
    $('#menu-story').removeClass('d-none');
    
    // Main links animation.
    TweenMax.staggerTo(menu_items, 0.9, {
        ease: Quint.easeOut,
        startAt: {y: '50%', opacity: 0},
        y:"0%", 
        opacity:1
    }, 0.1);
});


