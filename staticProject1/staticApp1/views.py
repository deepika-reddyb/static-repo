from django.shortcuts import render

# Create your views here.
def View1(request):
	myName="DEEPIKA REDDY"
	favSinger="JUSTIN BIEBER"
	favAnimal="SIBERIAN HUSKY"
	favSubject="ENGLISH"
	d={'name':myName,'singer':favSinger ,'animal':favAnimal,'subject':favSubject}
	return render(request,'staticApp1/1.html',d)
