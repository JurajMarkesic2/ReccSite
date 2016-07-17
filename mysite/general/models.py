from django.db import models

class Result(models.Model):
	title = models.CharField(max_length=140)  #the name of their personality e.g. Arhitect
	
	description = models.TextField() #short description of their personality and what kind of content they like

	movies_name1 = models.CharField(max_length=160)  #name of the movie/book/song/tv-show
	movies_link1 = models.URLField(blank=False)      #our affiliate link to that movie/book/song/tv-show on Amazon,iTunes, etc...
	movies_name2 = models.CharField(max_length=160)
	movies_link2 = models.URLField(blank=False)
	movies_name3 = models.CharField(max_length=160)
	movies_link3 = models.URLField(blank=False)
	movies_name4 = models.CharField(max_length=160)
	movies_link4 = models.URLField(blank=False)
	movies_name5 = models.CharField(max_length=160)
	movies_link5 = models.URLField(blank=False)
	
	
	books_name1 = models.CharField(max_length=160)
	books_link1 = models.URLField(blank=False)
	books_name2 = models.CharField(max_length=160)
	books_link2 = models.URLField(blank=False)
	books_name3 = models.CharField(max_length=160)
	books_link3 = models.URLField(blank=False)
	books_name4 = models.CharField(max_length=160)
	books_link4 = models.URLField(blank=False)
	books_name5 = models.CharField(max_length=160)
	books_link5 = models.URLField(blank=False)
	
	songs_name1 = models.CharField(max_length=160)
	songs_link1 = models.URLField(blank=False)
	songs_name2 = models.CharField(max_length=160)
	songs_link2 = models.URLField(blank=False)
	songs_name3 = models.CharField(max_length=160)
	songs_link3 = models.URLField(blank=False)
	songs_name4 = models.CharField(max_length=160)
	songs_link4 = models.URLField(blank=False)
	songs_name5 = models.CharField(max_length=160)
	songs_link5 = models.URLField(blank=False)
	
	series_name1 = models.CharField(max_length=160)
	series_link1 = models.URLField(blank=False)
	series_name2 = models.CharField(max_length=160)
	series_link2 = models.URLField(blank=False)
	series_name3 = models.CharField(max_length=160)
	series_link3 = models.URLField(blank=False)
	series_name4 = models.CharField(max_length=160)
	series_link4 = models.URLField(blank=False)
	series_name5 = models.CharField(max_length=160)
	series_link5 = models.URLField(blank=False)



	#@models.permalink
    #def get_absolute_url(self):
      #  return ('general:res', (), {'id': self.id, })   #sets up the id-based url
        

	def __str__(self):
		return self.title