import media
import fresh_tomatoes

# Jurassic World:
movies = []
jurassic_world = media.Movie("Jurassic World",
                             "https://upload.wikimedia.org/wikipedia/zh/3/34/Jurassic_World_Fallen_Kingdom_Poster.jpg",  # noqa
                             "https://www.youtube.com/watch?v=Sjur_kVGwAM")  # noqa
movies.append(jurassic_world)


# Ocean's 8
oceans_8 = media.Movie("Ocean's 8",
                       "https://upload.wikimedia.org/wikipedia/zh/a/ae/Ocean%27s_8_Poster.jpg",  # noqa
                       "https://www.youtube.com/watch?v=n5LoVcVsiSQ")  # noqa
movies.append(oceans_8)


# Deadpool 2
deadpool_2 = media.Movie("Deadpool 2",
                         "https://upload.wikimedia.org/wikipedia/zh/c/cf/Deadpool_2_poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=-IJz4mijCzU")  # noqa
movies.append(deadpool_2)


# Tomb Raider
tomb_raider = media.Movie("Tomb Raider",
                          "https://upload.wikimedia.org/wikipedia/zh/thumb/5/5f/Tomb_Raider_official_teaser_poster.jpg/220px-Tomb_Raider_official_teaser_poster.jpg",  # noqa
                          "https://www.youtube.com/watch?v=Um7bH-lNAfs")  # noqa
movies.append(tomb_raider)


# Red Sparrow
red_sparrow = media.Movie("Red Sparrow",
                          "https://upload.wikimedia.org/wikipedia/zh/2/2a/Red_Sparrow_Poster.jpg",  # noqa
                          "https://www.youtube.com/watch?v=EOLSarkmOxo")  # noqa
movies.append(red_sparrow)


# The Post
the_post = media.Movie("The Post",
                       "https://upload.wikimedia.org/wikipedia/zh/f/f2/The_Post_Poster.jpg",  # noqa
                       "https://www.youtube.com/watch?v=P49iVsdItkM")  # noqa
movies.append(the_post)


# Open the webpage
fresh_tomatoes.open_movies_page(movies)
