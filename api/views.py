from django.http import JsonResponse
from plagiarism import fetchresults

def api(request):
	if request.method == "POST":
		language = request.POST.get('lang')
		code = request.POST.get('code')
		return JsonResponse(plagiarism.fetchresults(language, code))