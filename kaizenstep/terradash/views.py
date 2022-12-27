from django.shortcuts import render

# Create your views here.
def terradash(request):
	return render(request, 'terradash/terradash.html', {})
