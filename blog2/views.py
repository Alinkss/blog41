from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Tag, Comments, SubscribeNewsletter, Profile, Adress, PostImage
from .forms import PostForm, CommentsForm, SubscribeForm, RegisterForm, UserRegister, UserUpdateForm, ProfileUpdate, AdressFormSet, AvatarForm, AdressForm, PostImageForm, ImageFormSet
from django.db.models import Q
from django.utils.timezone import now
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth import logout, login
from django.contrib.auth.models import User

def get_categories():
    all = Category.objects.all()
    count = all.count()
    half = count // 2
    first_half = all[:half]
    second_half = all[half:]
    
    return {'cats': first_half, 'cats2': second_half}

def tags():
    all_tags = Tag.objects.all()
    
    return {'tags': all_tags}

def main(request):
    posts = Post.objects.all().order_by("-published_date")
    # posts = Post.objects.filter(content__contains = "nature")
    
    context = {'posts': posts}
    context.update(get_categories())
    context.update(tags())
    return render(request, 'blog2/index.html', context)

# def main(request):
#     number = 400
#     title = "Blog"
#     context = {"title": title, "products":["products1", "products2", "product3"]}
#     return render(request, "blog2/index.html", context)

def category(request, c=None):
    cObj = get_object_or_404(Category, name=c)
    posts = Post.objects.filter(category=cObj).order_by("-published_date")
    context = {'posts': posts}
    context.update(get_categories())
    return render(request, 'blog2/index.html', context)

def post(request, id=None):
    post = get_object_or_404(Post, pk=id)
    context = {'post': post}
    context.update(get_categories())
    return render(request, 'blog2/post.html', context)

def contacts(request):
    context = {}
    context.update(get_categories())
    return render(request, 'blog2/contacts.html', context)

def about_us(request):
    context = {}
    context.update(get_categories())
    return render(request, 'blog2/about us.html', context)


def search(request):
    query = request.GET.get('query', '')
    
    posts = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))
    context = {'posts': posts}
    context.update(get_categories())
    return render(request, 'blog2/index.html', context)

@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        image_form = ImageFormSet(request.POST, request.FILES, queryset=PostImage.objects.none())
        if form.is_valid() and image_form.is_valid():
            post = form.save(commit=False)
            post.published_date = now()
            post.user = request.user
            post.save()
            
            for form in image_form.cleaned_data:
                if form:
                    image = form['image']
                    PostImage.objects.create(post=post, image=image)
                
            return main(request)
    form = PostForm()
    image_form = ImageFormSet(queryset=PostImage.objects.none())

    
    context = {
        'form': form,
        'image_form': image_form
               }
    context.update(get_categories())
    return render(request, 'blog2/create.html', context)

def comment_and_post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comments.objects.filter(post= post).order_by("-published_date") 

    if request.method == 'POST':
        print("Received POST request with data:", request.POST)
        comments_form = CommentsForm(request.POST)
        if comments_form.is_valid():
            print("Form is valid")
            comment = comments_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.published_date = now()
            comment.save()
            print("Comment saved:", comment)
            return redirect('comments', post_id=post.id)
        else:
            print("Form is not valid:", comments_form.errors)
            
    comments_form = CommentsForm()
    print('Comments', comments)
    print(f'post id: {post_id}')
    # comments = post.comments.all()
    context = {
        'post': post,
        'comments': comments,
        'comments_form': comments_form,
    }
    return render(request, 'blog2/post.html', context)

def newsletter(request):
    if request.method == 'POST':
        sub_form = SubscribeForm(request.POST)
        if sub_form.is_valid():
            sub_form.save()
            return redirect('newsletter')
        print(sub_form.errors)
    else:
        sub_form = SubscribeForm()
        
    context = {'sub_form': sub_form}
        
    return render(request, 'blog2/succes.html', context)
        
class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('main')
    
@login_required
def profile(request, user_id):
    user = User.objects.get(id = user_id)
    profile = get_object_or_404(Profile, user = user)
    
    posts = Post.objects.filter(user = user)
    comments = Comments.objects.filter(user = user)
    adresses = Adress.objects.filter(profile = profile)
    post_number = Post.objects.filter(user=user).count()
    comments_number = Comments.objects.filter(user = user).count()
    days_since_registration = (timezone.now() - user.date_joined).days
    
    profile = get_object_or_404(Profile, user=user)
    avatar = profile.avatar.url
    context = {
               'user': user,
               'posts': posts,
               'comments': comments,
               'adresses': adresses,
               'post_number': post_number,
               'comments_number': comments_number,
               'days_since_register': days_since_registration,
               'avatar': avatar
               }
    
    context.update(get_categories())
    return render(request, 'blog2/profile.html', context)

def registration(request):
    if request.method == 'POST':
        user_form = UserRegister(request.POST)
        register_form = RegisterForm(request.POST, request.FILES)
        adress_form = AdressForm(request.POST)

        if user_form.is_valid() and register_form.is_valid() and adress_form.is_valid():
            user = user_form.save()
            register = register_form.save(commit=False)
            register.user = user
            register.register_date = timezone.now()
            register.save()
            
            adress = adress_form.save(commit=False)
            adress.profile = register
            adress.save()
            
            login(request, user)
            return redirect('profile', user_id=user.id)
        else:
            print(user_form.errors)
            print(register_form.errors)
            print(adress_form.errors)
            print(request.FILES)

    
    user_form = UserRegister()
    register_form = RegisterForm()
    adress_form = AdressForm()

    
    context = {
        'user_form': user_form,
        'register_form': register_form,
        'adress_form': adress_form,
    }
    
    return render(request, 'blog2/registration.html', context)

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_update = UserUpdateForm(request.POST, instance = request.user)
        profile_update = ProfileUpdate(request.POST, request.FILES, instance = request.user.profile)
        adress_form_set = AdressFormSet(request.POST, instance= request.user.profile)
        avatar_form = AvatarForm(request.POST, request.FILES, instance = request.user.profile)
        if user_update.is_valid() and profile_update.is_valid() and adress_form_set.is_valid() and avatar_form.is_valid():
            user_update.save()
            profile_update.save()
            adress_form_set.save()
            avatar_form.save()
            redirect('profile', user_id=request.user.pk)
        else:
            print(f"form is not valid: {avatar_form.errors}")
    else:
        user_update = UserUpdateForm(instance=request.user)
        profile_update = ProfileUpdate(instance=request.user.profile)
        adress_form_set = AdressFormSet(instance=request.user.profile)
        avatar_form = AvatarForm(instance=request.user.profile)
        if not adress_form_set:
            adress_form_set = AdressFormSet(queryset=Adress.objects.none(), instance=request.user.profile)
        
    context = {
        'user_update': user_update,
        'profile_update': profile_update,
        'adress_form_set': adress_form_set,
        'avatar_form': avatar_form,
    }
    
    return render(request, 'blog2/update_profile.html', context)
    


