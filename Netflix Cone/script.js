let movies = [
    
    {
        name : "Avengers Endgame",
        poster : "https://images-cdn.ubuy.co.in/634ffe4b05d16a708944a5ec-avengers-endgame-movie-poster-2-sided.jpg",
        rating : 8.7,
        link : "https://www.youtube.com/watch?v=79uhQ85n0YU&themeRefresh=1"
    },
    
    {
        name : "Lagaan",
        poster : "https://m.media-amazon.com/images/M/MV5BNDYxNWUzZmYtOGQxMC00MTdkLTkxOTctYzkyOGIwNWQxZjhmXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg",
        rating : 9.1
    },

    
    {
        name : "Oppenheimer",
        poster : "https://m.media-amazon.com/images/I/81218n6JFgL._AC_UF1000,1000_QL80_.jpg",
        rating : 9.2
    },

    {
        name : "Moonlight",
        poster : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2-edx78UxtIXLTR9B7uy_zn3MpxHdy2kFdw&s",
        rating : 7.2
    },

    {
        name : "Bohemian Rhapsody",
        poster : "https://m.media-amazon.com/images/I/91Of83+qeoL.jpg",
        rating : 6.5
    },

    {
        name : "The Avengers",
        poster : "https://m.media-amazon.com/images/M/MV5BNDYxNjQyMjAtNTdiOS00NGYwLWFmNTAtNThmYjU5ZGI2YTI1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
        rating : 7.6
    },

    {
        name : "Maleficent",
        poster : "https://lumiere-a.akamaihd.net/v1/images/p_maleficent_19736_89c0d9e7.jpeg",
        rating : 6.4
    },

    {
        name : "John Wick",
        poster : "https://rukminim2.flixcart.com/image/850/1000/k0lbdzk0/poster/4/w/g/medium-john-wick-poster-for-room-office-13-inch-x-19-inch-rolled-original-imafkc6fd8mc6jga.jpeg?q=20&crop=false",
        rating : 7.9
    },

]


function searchMovie(){
    // console.log("Button working");
    let movieName = document.getElementById("search").value; // value property works only with input fields, select text, dropdown, etc... only text... it can't access images, div, etc
    // console.log(movieName);
    if(movieName!=""){
        let result = movies.filter(function(movie){
            return movie.name.toUpperCase().includes(movieName.toUpperCase());
        })
        // console.log(result);
        displayMovies(result);
    }
    else{
        displayMovies(movies);
    }

}


// let movie = document.createElement("div");
// movie.classList.add("one");   
// classList is a property which helps you to add/remove classes from an element
//we can also add multiple classes to an element




function displayMovies(data){


    document.getElementById("movies").innerHTML="";

    //A BIT LONG METHOD
    // let movieDIV = document.createElement("div");
    // movieDIV.classList.add("movie");
    // // console.log(movie); ---> a div will be printed in console

    //  let overlayDIV = document.createElement("div");  // ---> this equivalent to <div class="overlay"><\div>
    //  overlayDIV.classList.add("overlay");

    //  movieDIV.appendChild(overlayDIV); // --> makes overlayDIV inside the movieDIV (movieDIV will be parent, overlayDIV will be child)

    //  console.log(movieDIV)

    //EASY METHOD
    let htmlString = ` `;

    for (let i=0; i<data.length;i++){

        htmlString = htmlString + 
        `
        <a href="${data[i].link}">
        <div class="movie">
            <div class="overlay">

                <div class="video">
                
                </div>

                <div class="details">
                    <h1>${data[i].name}</h1>
                    <h2>IMDB : ${data[i].rating}</h2>
                    <p>Rami Malek . Jhon Jacobs . Emma Stone</p>
                </div>

            </div>
            <img src="${data[i].poster}" alt="" class="poster">
        </div>
        </a>
        `;

    }

    console.log(htmlString);

    document.getElementById("movies").innerHTML = htmlString;

    //BUT EASIER METHOD IS SLOWER... BETTER USE LONGER METHOD

}

displayMovies(movies);