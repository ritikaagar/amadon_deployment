from django.shortcuts import render, redirect, HttpResponse

def index(request):
	item_list = [{'name': 'Shirt' , 'price': 19.99}, {'name': 'Sweatshirt' , 'price': 29.99}, {'name': 'Jeans' , 'price': 14.99}, {'name': 'Skirt' , 'price': 19.99}]

	context = {
	'items' : item_list
	}

	try:
		request.session["total_price"]
	except:
		request.session["total_price"] = 0

	try:
		request.session["total_items"]
	except:
		request.session["total_items"] = 0

	return render(request, 'amadon_app/index.html', context)

def process(request):
	request.session["result_price"] = float(request.POST.get('price')) * float(request.POST.get('quantity'))

	request.session["total_price"] += float(request.session["result_price"])

	request.session["total_items"] += int(request.POST.get('quantity'))

	return redirect('/results')

def pageload(request):
	return render(request,'amadon_app/results.html')

def clear(request):
	request.session.clear()
	return redirect('/')