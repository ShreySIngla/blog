from django.views import generic
from django.shortcuts import render, redirect
from .models import Subscription
from .models import Post
from django.http import HttpResponse
from django.contrib import messages
from django.db import IntegrityError
from django.contrib import messages

from django.contrib import messages

from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

from django.template.loader import render_to_string
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from dotenv import load_dotenv
load_dotenv()
from django.shortcuts import redirect
from django.contrib import messages

from django.shortcuts import redirect
from django.contrib import messages

from django.contrib import messages

def homepage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            messages.error(request, 'Email cannot be blank.')
        else:
            existing_subscription = Subscription.objects.filter(email=email).exists()
            if Subscription.objects.filter(email=email).exists():
                messages.warning(request, 'Email is already registered.')
            else:
                subscription = Subscription(email=email)
                subscription.save()
                messages.success(request, 'Email saved successfully.')

    srs = Subscription.objects.all()
    post_list = Post.objects.all()
    return render(request, 'index1.html', {'post_list': post_list, 'messages': messages.get_messages(request)})




# def homepage(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         print(email)

#         subscription = Subscription(email=email)
#         subscription.save()
#         return redirect('home')
#     srs=Subscription.objects.all()
#     print(srs)
#     post_list = Post.objects.all()
#     return render(request, 'index1.html', {'post_list': post_list})



class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'index1.html'
    

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post.html'

class AboutUsView(generic.TemplateView):
    template_name = 'about.html'

class contactUsView(generic.TemplateView):
    template_name = 'contact.html'


# def homepage(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         print(email)

#         subscription = Subscription(email=email)
#         subscription.save()
#         return redirect('home')
#     srs=Subscription.objects.all()
#     print(srs)
#     post_list = Post.objects.all()
#     return render(request, 'index1.html', {'post_list': post_list})



def search_view(request):
    keywords = request.GET.get('keywords', '')
    
    posts = Post.objects.filter(title__icontains=keywords)  # Adjust this query based on your model and search criteria
    
    jobs_per_page = 5
    paginator = Paginator(posts, jobs_per_page)
    page_number = request.GET.get('page')
    searched_jobs = paginator.get_page(page_number)

    context = {
        'keywords': keywords,
        'posts': searched_jobs,
    }

    return render(request, 'search_results.html',{'searched_jobs': searched_jobs,'keywords': keywords,})

    
from django.core.paginator import Paginator

def latest_jobs(request):
    # Retrieve all jobs from the database
    all_jobs = Post.objects.all()

    # Set the number of jobs to display per page
    jobs_per_page = 5

    # Create a paginator object
    paginator = Paginator(all_jobs, jobs_per_page)

    # Get the requested page number
    page_number = request.GET.get('page')

    # Get the jobs for the requested page
    latest_jobs = paginator.get_page(page_number)
    
    
    # Pass the latest jobs to the template for rendering
    return render(request, 'latest_jobs.html', {'latest_jobs': latest_jobs})

# def latest_jobs(request):
#     # Retrieve the latest jobs from the database
#     latest_jobs = Post.objects.all() # Get the latest 3 jobs

#     # Pass the latest jobs to the template for rendering
#     return render(request, 'latest_jobs.html', {'latest_jobs': latest_jobs})

def demo_templates(request):
    return render(request, 'demo_templates.html')

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


class contactUsView(generic.TemplateView):
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the data or perform other necessary actions
        print(name,email,subject,message)
        # Send an email
        # send_mail(
        #     subject,
        #     message,
        #     email,
        #     ['your-email@example.com'],  # Replace with your email address
        #     fail_silently=False,
        # )           
        recipients = ['shreylearning@gmail.com']
        context ={
                'name':name,
                'subject': subject,
                 
                'message': message,
                'sender': email,
                'recipients': recipients
            }
            
        email_html = render_to_string('email_template.html', context)
        send_mail(subject, message, email, recipients, html_message=email_html, fail_silently=False)
        # send_mail(
        #             subject,
        #             message,
        #             email,
        #             ['shreylearning@gmail.com'],
        #             fail_silently=False,
        #         )     
        # send_mail(
        #             "thanks",
        #             "thanks for contacting us ",
        #             email,
        #             [email],
        #             fail_silently=False,
        #         ) 

        # Add a success message
        messages.success(request, 'Your message has been sent successfully!')

        # Render a success message or redirect to a success page
        return render(request, 'contact.html')