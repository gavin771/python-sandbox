import media
import ui


toy_story = media.Movie(
  "Toy Story",
  "Toys come to life",
  "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
  "https://www.youtube.com/watch?v=KYz2wyBy3kc"
  )

avatar = media.Movie(
  "Avatar",
  "A marine on an alien planet",
  "http://www.impawards.com/2009/posters/avatar.jpg",
  "https://www.youtube.com/watch?v=6ziBFh3V1aM"
  )

hearts_beat_loud = media.Movie(
  "Hearts Beat Loud",
  "A single father has to nvigate the waters of a teenage daughter on her way to college",
  "https://m.media-amazon.com/images/M/MV5BMjA2MTM2MjcxNV5BMl5BanBnXkFtZTgwMzI3ODgyNTM@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
  "https://www.youtube.com/watch?v=4Zh0iHWn30o"
  )
movies=[toy_story,avatar,hearts_beat_loud]

ui.open_movies_page(movies)