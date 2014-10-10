from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def base(request):
	template = 'base.html'
	html_code = """<form class="navbar-form navbar-right" role="form">
        <div class="form-group">
          <input type="text" placeholder="Email" class="form-control">
        </div>
        <div class="form-group">
          <input type="password" placeholder="Password" class="form-control">
        </div>
        <button type="submit" class="btn btn-success">Sign in</button>
        
      </form>"""
	

	if request.user.is_authenticated():
		myUser = request.user

	else:
		myUser = ''	
		html_code

	context = {
		'myUser': myUser,
		'html_code': html_code,



	}

	return render(request,template, context)

# def navbar(request):
# 	print myUser
# 	template = 'navbar.html'
# 	myUser = request.user
# 	# if request.user.is_authenticated():
# 	# 	myUser = request.user
# 	# else:
# 	# 	myUser = ''

# 	context = {'myUser': request.user}
	
# 	return render(request, template, context)