from django.db import models



class Result(models.Model):
	title = models.CharField(max_length=140)  #the name of their personality e.g. Arhitect
	
	description = models.TextField() #short description of their personality and what kind of content they like

	typeImg = models.URLField(blank=True, null=True, default="https://openclipart.org/image/2400px/svg_to_png/250864/Chess-Pieces-Lineup.png")

	movies_name1 = models.CharField(max_length=160, default="name")  #name of the movie/book/song/tv-show
	movies_link1 = models.URLField(default="https://www.amazon.com")      #our affiliate link to that movie/book/song/tv-show on Amazon,iTunes, etc...
	movies_name2 = models.CharField(max_length=160, default="name")
	movies_link2 = models.URLField(default="https://www.amazon.com")
	movies_name3 = models.CharField(max_length=160, default="name")
	movies_link3 = models.URLField(default="https://www.amazon.com")
	movies_name4 = models.CharField(max_length=160, default="name")
	movies_link4 = models.URLField(default="https://www.amazon.com")
	movies_name5 = models.CharField(max_length=160, default="name")
	movies_link5 = models.URLField(default="https://www.amazon.com")
	
	
	books_name1 = models.CharField(max_length=160, default="name")
	books_link1 = models.URLField(default="https://www.amazon.com")
	books_name2 = models.CharField(max_length=160, default="name")
	books_link2 = models.URLField(default="https://www.amazon.com")
	books_name3 = models.CharField(max_length=160, default="name")
	books_link3 = models.URLField(default="https://www.amazon.com")
	books_name4 = models.CharField(max_length=160, default="name")
	books_link4 = models.URLField(default="https://www.amazon.com")
	books_name5 = models.CharField(max_length=160, default="name")
	books_link5 = models.URLField(default="https://www.amazon.com")
	
	songs_name1 = models.CharField(max_length=160, default="name")
	songs_link1 = models.URLField(default="https://www.amazon.com")
	songs_name2 = models.CharField(max_length=160, default="name")
	songs_link2 = models.URLField(default="https://www.amazon.com")
	songs_name3 = models.CharField(max_length=160, default="name")
	songs_link3 = models.URLField(default="https://www.amazon.com")
	songs_name4 = models.CharField(max_length=160, default="name")
	songs_link4 = models.URLField(default="https://www.amazon.com")
	songs_name5 = models.CharField(max_length=160, default="name")
	songs_link5 = models.URLField(default="https://www.amazon.com")
	
	series_name1 = models.CharField(max_length=160, default="name")
	series_link1 = models.URLField(default="https://www.amazon.com")
	series_name2 = models.CharField(max_length=160, default="name")
	series_link2 = models.URLField(default="https://www.amazon.com")
	series_name3 = models.CharField(max_length=160, default="name")
	series_link3 = models.URLField(default="https://www.amazon.com")
	series_name4 = models.CharField(max_length=160, default="name")
	series_link4 = models.URLField(default="https://www.amazon.com")
	series_name5 = models.CharField(max_length=160, default="name")
	series_link5 = models.URLField(default="https://www.amazon.com")



	@models.permalink
	def get_absolute_url(self):
		return ('general:res', (), {'id': self.id, })   #sets up the id-based url
    

	def __str__(self):
		return self.title