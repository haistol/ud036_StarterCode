import fresh_tomatoes
import media

#Movie meta-data to be loaded on the page
MOVIES=[{
         "title":"The Man from U.N.C.L.E",
         "boxart":("https://www.freedvdcover.com/wp-content/uploads/freedvd"
                   "cover_the-man-from-u.n.c.l.e.-custom-cover-pips.jpg"),
         "poster":("https://upload.wikimedia.org/wikipedia/en/e/e5/The_Man_"
                   "from_U.N.C.L.E._poster.jpg"),
         "trailer":"https://www.youtube.com/watch?v=w_Ky4KPzKwY"
        },
        {
         "title":"Deadpool",
         "boxart":("https://www.freedvdcover.com/wp-content/uploads/freedvd"
                  "cover_deadpool-2016-r1-custom.jpg"),
         "poster":("https://upload.wikimedia.org/wikipedia/en/4/46/"
                   "Deadpool_poster.jpg"),
         "trailer":"https://www.youtube.com/watch?v=FyKWUTwSYAs"
        },
        {
         "title":"Moana",
         "boxart":("https://www.freedvdcover.com/wp-content/uploads/2016/12/"
                  "2016-12-10_584c6776c758b_moanafront.jpg"),
         "poster":("https://upload.wikimedia.org/wikipedia/en/2/26/Moana_"
                   "Teaser_Poster.jpg"),
         "trailer":"https://www.youtube.com/watch?v=LKFuXETZUsI"
        },
        {
         "title":"Kingsman: The Secret Service",
         "boxart":("https://lh6.googleusercontent.com/-sSxw1gKlSxI/VU2fzPSv3OI"
                  "/AAAAAAAAfaY/mXB918mj7K0/w1600-h1078-p/Kingsman.%2BThe%2B"
                  "Secret%2BService%2B-CoveRdvdGratiS.Com%2BV5.jpg"),
         "poster":("https://upload.wikimedia.org/wikipedia/en/8/8b/Kingsman_"
                   "The_Secret_Service_poster.jpg"),
         "trailer":"https://www.youtube.com/watch?v=kl8F-8tR8to"
        },
        {
         "title":"Inception",
         "boxart":("http://1.bp.blogspot.com/-T-aseaOU1RI/T8iQM-FzAGI/AAAAAAA"
                  "AAI0/MiGvg8ke9RU/s1600/inception-dvd-front-cover.jpg"),
         "poster":("https://upload.wikimedia.org/wikipedia/en/2/2e/Inception"
                   "_%282010%29_theatrical_poster.jpg"),
         "trailer":"https://www.youtube.com/watch?v=d3A3-zSOBT4"
        },
        {
         "title":"Basic",
         "boxart":("http://dvd.box.sk/newsimg/dvdmov/max1360962975-frontback-"
                  "cover.jpg"),
         "poster":("https://upload.wikimedia.org/wikipedia/en/1/1b/"
                   "Basic_movie.jpg"),
         "trailer":"https://www.youtube.com/watch?v=kE7Ue5hjJc0"
         }]
#Load the meta-data on the movie list
movie_list=[]
for movie in MOVIES:
    movie_list+=[media.Movie(movie["title"],
                             movie["boxart"],
                             movie["poster"],
                             movie["trailer"])]
#Open the page to display the movies poster and trailer
fresh_tomatoes.open_movies_page(movie_list)
