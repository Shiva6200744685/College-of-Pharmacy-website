from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import BlogPost
# from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.
def home_view(request):
    return render(request, "index.html", context={})

def about_view(request):
    return render(request, "about.html", context={})

def course_view(request):
    return render(request, "course.html", context={})


class BlogListView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'blog.html' 
    paginate_by = 2  # Adjust number of posts per page

class BlogDetailView(DetailView):
    model = BlogPost

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})

def contact_view(request):
    message = ""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email notification
            # send_mail(subject, message, email, ['your_email@example.com'])
            form.save()

            message = "success"
        else:
            message = "error"
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, "message": message})
