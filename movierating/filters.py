import django_filters
from movierating.models import Movie, Genre

class MovieFilter(django_filters.FilterSet):
	movie_title = django_filters.CharFilter(
		field_name = 'movie_title',
		label = 'Movie Title',
		lookup_expr = 'icontains'
	)
	imdbid = django_filters.NumberFilter(
		field_name = 'imdbid',
		label = 'IMDBid',
		lookup_expr = 'icontains'
	)

	tmdbid = django_filters.NumberFilter(
		field_name = 'tmdbid',
		label = 'TMDBId',
		lookup_expr = 'icontains'
	)


	genre = django_filters.ModelChoiceFilter(
		field_name='genre',
		label='Genre',
		queryset=Genre.objects.all().order_by('genre_name'),
		lookup_expr='exact'
	)


	class Meta:
		model = Movie
		# form = SearchForm
		# fields [] is required, even if empty.
		fields = []