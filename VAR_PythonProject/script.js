function toggleMenu() {
    const menu = document.querySelector(".menu-links");
    const icon = document.querySelector(".hamburger-icon");
    menu.classList.toggle("open");
    icon.classList.toggle("open");
}

function renderTeam() {
    var selected = document.getElementById("teamOption");
    var imgUrl = "";

    switch (selected.value * 1) {
        case 1: imgUrl = "logos/teams/man-city.png"; break;
        case 2: imgUrl = "logos/teams/man-utd.png"; break;
        case 3: imgUrl = "logos/teams/spurs.png"; break;
        case 4: imgUrl = "logos/teams/liverpool.png"; break;
        case 5: imgUrl = "logos/teams/chelsea.png"; break;
        case 6: imgUrl = "logos/teams/arsenal.png"; break;
        case 7: imgUrl = "logos/teams/burnley.png"; break;
        case 8: imgUrl = "logos/teams/everton.png"; break;
        case 9: imgUrl = "logos/teams/leicester.png"; break;
        case 10: imgUrl = "logos/teams/newcastle.png"; break;
        case 11: imgUrl = "logos/teams/crystal-palace.png"; break;
        case 12: imgUrl = "logos/teams/west-ham.png"; break;
        case 13: imgUrl = "logos/teams/brighton.png"; break;
        case 14: imgUrl = "logos/teams/soton.png"; break;
        default: imgUrl = "logos/premier-league-logo.png"; break;
    }
    
    document.getElementById("myImg").src = imgUrl;
}

function renderGif() {
    var selected = document.getElementById("teamOption");
    var imgUrl = "";

    switch (selected.value * 1) {
        case 1: imgUrl = "GP_2/GP2_man-city.gif"; break;
        case 2: imgUrl = "GP_2/GP2_man-utd.gif"; break;
        case 3: imgUrl = "GP_2/GP2_spurs.gif"; break;
        case 4: imgUrl = "GP_2/GP2_liverpool.gif"; break;
        case 5: imgUrl = "GP_2/GP2_chelsea.gif"; break;
        case 6: imgUrl = "GP_2/GP2_arsenal.gif"; break;
        case 7: imgUrl = "GP_2/GP2_burnley.gif"; break;
        case 8: imgUrl = "GP_2/GP2_everton.gif"; break;
        case 9: imgUrl = "GP_2/GP2_leicester.gif"; break;
        case 10: imgUrl = "GP_2/GP2_newcastle.gif"; break;
        case 11: imgUrl = "GP_2/GP2_crystal-palace.gif"; break;
        case 12: imgUrl = "GP_2/GP2_west-ham.gif"; break;
        case 13: imgUrl = "GP_2/GP2_brighton.gif"; break;
        case 14: imgUrl = "GP_2/GP2_soton.gif"; break;
        default: imgUrl = "logos/pl-stats-logo.jpg";break;
    }
    
    document.getElementById("myImg-gif").src = imgUrl;
}