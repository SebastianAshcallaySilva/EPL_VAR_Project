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
        case 1: imgUrl = "project/logos/teams/man-city.png"; break;
        case 2: imgUrl = "project/logos/teams/man-utd.png"; break;
        case 3: imgUrl = "project/logos/teams/spurs.png"; break;
        case 4: imgUrl = "project/logos/teams/liverpool.png"; break;
        case 5: imgUrl = "project/logos/teams/chelsea.png"; break;
        case 6: imgUrl = "project/logos/teams/arsenal.png"; break;
        case 7: imgUrl = "project/logos/teams/burnley.png"; break;
        case 8: imgUrl = "project/logos/teams/everton.png"; break;
        case 9: imgUrl = "project/logos/teams/leicester.png"; break;
        case 10: imgUrl = "project/logos/teams/newcastle.png"; break;
        case 11: imgUrl = "project/logos/teams/crystal-palace.png"; break;
        case 12: imgUrl = "project/logos/teams/west-ham.png"; break;
        case 13: imgUrl = "project/logos/teams/brighton.png"; break;
        case 14: imgUrl = "project/logos/teams/soton.png"; break;
        default: imgUrl = "project/logos/premier-league-logo.png"; break;
    }
    
    document.getElementById("myImg").src = imgUrl;
}

function renderGif() {
    var selected = document.getElementById("teamOption");
    var imgUrl = "";

    switch (selected.value * 1) {
        case 1: imgUrl = "project/GP_2/GP2_man-city.gif"; break;
        case 2: imgUrl = "project/GP_2/GP2_man-utd.gif"; break;
        case 3: imgUrl = "project/GP_2/GP2_spurs.gif"; break;
        case 4: imgUrl = "project/GP_2/GP2_liverpool.gif"; break;
        case 5: imgUrl = "project/GP_2/GP2_chelsea.gif"; break;
        case 6: imgUrl = "project/GP_2/GP2_arsenal.gif"; break;
        case 7: imgUrl = "project/GP_2/GP2_burnley.gif"; break;
        case 8: imgUrl = "project/GP_2/GP2_everton.gif"; break;
        case 9: imgUrl = "project/GP_2/GP2_leicester.gif"; break;
        case 10: imgUrl = "project/GP_2/GP2_newcastle.gif"; break;
        case 11: imgUrl = "project/GP_2/GP2_crystal-palace.gif"; break;
        case 12: imgUrl = "project/GP_2/GP2_west-ham.gif"; break;
        case 13: imgUrl = "project/GP_2/GP2_brighton.gif"; break;
        case 14: imgUrl = "project/GP_2/GP2_soton.gif"; break;
        default: imgUrl = "project/logos/pl-stats-logo.jpg";break;
    }
    
    document.getElementById("myImg-gif").src = imgUrl;
}

function renderPng() {
    var selected = document.getElementById("seasonOption");
    var pngUrl = "";

    switch (selected.value * 1) {
        case 1: pngUrl = "project/GP_3/GP3_2019_20.png"; break;
        case 2: pngUrl = "project/GP_3/GP3_2020_21.png"; break;
        case 3: pngUrl = "project/GP_3/GP3_2021_22.png"; break;
        default: pngUrl = "project/logos/pl-stats-logo.jpg";break;
    }

    document.getElementById("myPng").src = pngUrl;
}

function show_gp1() {
    var seasonSelected = document.getElementById("seasons")
    var blankDiv = document.getElementById("blank-div")
    var div1 = document.getElementById("gp1-2019-20")
    var div2 = document.getElementById("gp1-2020-21")
    var div3 = document.getElementById("gp1-2021-22")
    
    if (seasonSelected.value == 0) {
        blankDiv.style.visibility = "visible";
        div1.style.visibility = "hidden";
        div2.style.visibility = "hidden";
        div3.style.visibility = "hidden";
    } else if (seasonSelected.value == 1) {
        blankDiv.style.visibility = "hidden";
        div1.style.visibility = "visible";
        div2.style.visibility = "hidden";
        div3.style.visibility = "hidden";
    } else if (seasonSelected.value == 2) {
        blankDiv.style.visibility = "hidden";
        div1.style.visibility = "hidden";
        div2.style.visibility = "visible";
        div3.style.visibility = "hidden";
    } else if (seasonSelected.value == 3) {
        blankDiv.style.visibility = "hidden";
        div1.style.visibility = "hidden";
        div2.style.visibility = "hidden";
        div3.style.visibility = "visible";
    }
}