from django.http import HttpResponse
import json
import requests
def mi_vista(request):
    #api_key = 'TU_API_KEY_DE_TMDB'
    #movie_id = 'ID_DE_LA_PELICULA'
    url = f'https://api.themoviedb.org/3/movie/popular?api_key=8c84367d103d5239463d287812d5bafc'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        #response_data = {
         #   'titulo': data['title'],
          #  'sinopsis': data['overview'],
           # 'fecha_estreno': data['release_date'],
            #'calificacion': data['vote_average'],
            #'poster':data['poster']
        #}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        # Maneja el error aquí
        return HttpResponse('Error al obtener los datos', status=response.status_code)