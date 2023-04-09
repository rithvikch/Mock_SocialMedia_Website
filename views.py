from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from decimal import Decimal
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login
import datetime
from django.core.mail import EmailMessage
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.db.models import Avg
from django.db.models import IntegerField
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import base64
from django.core.files.base import ContentFile
from django.core.mail import send_mail
import requests
from django.shortcuts import render,get_object_or_404
import random
from django.db.models import F

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

from connectify.models import Post, UserProfile, Blog, Comment, LikePost

cloudinary.config( 
  cloud_name = "hfg9s7ggn", 
  api_key = "736455778975819", 
  api_secret = "drP6LmjwrJv0WTO4TJU9TQULX18" 
)



# def generalpurpose(request):
#     return HttpResponseRedirect(request.name)


def index(request):

    return render(request,'index.html')





def blog_detailed(request):


    item_id = request.GET.get('id')
    
    blog = Blog.objects.all().get(id=item_id)


    context = {"e":blog}

    return render(request,'blog_detailed.html', context)





def post_detailed(request):

    item_id = request.GET.get('id')
    social = Post.objects.all().get(id=item_id)




    comments = Comment.objects.filter(post=social).order_by('-created_at')




    comments_count = len(comments)



    if comments_count == 0:

        print("There are no comments for this yet")

        no_comments = True

    else:

        no_comments = False





    context = {"e":social, "comments":comments, "no_comments" : no_comments}



    if request.method == 'POST':
        print(" Saving a new comment  Saving a new comment  Saving a new comment  Saving a new comment  Saving a new comment ")

        comment_text = request.POST.get("comment")

        user = request.user



        comment = Comment(user=user, post = social, comment_text=comment_text)

        comment.save()


        return HttpResponseRedirect(f"post_detailed.html?id={item_id}")




    return render(request,'post_detailed.html', context)







def browse(request):

    # e = Post()


    txtSearch = request.GET.get('TxtSearch')

    # print("text search drrrrrrrrrrrrrrrrrrr" + txtSearch)


    if (txtSearch is not None):
        print("They searched somethingggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
        social = Post.objects.filter(privacy=False).filter(Q(username__contains = txtSearch))
        # print("'''fefhfffffffffffffffffuei" + social.length())
        searched = True
    
    else:

        social = Post.objects.all().filter(privacy=False).order_by('-created_at')
        txtSearch = ""
        searched = False




    api_url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=e90f2009534649728c3bffc7721b41be" 

    response = requests.get(api_url).json()

    articles = []

    if response['status'] == "ok":

        randoms = random.sample(response['articles'], 5)

        for article in randoms:

            article['title'] = ' - '.join(article['title'].split(' - ')[:-1])


            articles.append({'title': article['title'], 'name': article['source']['name'], 'author': article['author'], 'url': article['url']})


    # blogs context

    blogs = Blog.objects.all().order_by('-created_at')


    # suggested friends context

    # friends = Users

            

    length = social.count()
    




    friends = UserProfile.objects.all().order_by('?')[:4]


    comments_count = []
    for post in social:
        post_comments = Comment.objects.filter(post=post).count()
        comments_count.append(post_comments)

    print(comments_count)


    liked = LikePost.objects.all().filter(user= request.user)
    liked_id = []
    for thing in liked:
        liked_id.append(str(thing.post_id))
    print(liked_id)
    context = {"social_info": social, "length" : length, 'articles': articles, 'blogs':blogs, 'friends': friends, 'comments_count' : comments_count, 'liked':liked_id}













    return render(request,'browse.html', context)



     # e = Post()

     # social = Post.objects.all().filter(privacy=False).order_by('-created_at')

     # print(social.count())

     # length = social.count()

     # context = {"social_info":social, "length" : length}

     # return render(request,'browse.html', context)






    # return render(request,'browse.html', context)


@login_required(login_url = "login.html")
def my_profile(request):

    current_user = request.user.get_username()


    social = Post.objects.all().filter(user=request.user).order_by('-created_at')

    length = social.count()

    if length == 0:

        no_posts = True

    else:
        no_posts = False


    



    context = {"social_info": social, "no_posts" : no_posts}

    



    if request.method == 'POST':
        print(" DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELTING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETITING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETING  DELETIETING  DELETING  DELETING  DELETING  DELETING ")
        delete_id = request.POST.get("delete_post")


        item = get_object_or_404(Post, id=delete_id)

        item.delete()

        



    return render(request,'my_profile.html', context)





def view_profile(request):

    txtSearch = request.GET.get('TxtSearch')

    # print("text search drrrrrrrrrrrrrrrrrrr" + txtSearch)


  





    # blogs context



    # suggested friends context

    # friends = Users

            

    






    comments_count = []
   

    print(comments_count)
    item_id = request.GET.get('id')
    e = UserProfile.objects.all().get(id=item_id)
    posts = Post.objects.all().filter(user = e.user)
    print(posts.count())
    for post in posts:
        post_comments = Comment.objects.filter(post=post).count()
        comments_count.append(post_comments)

    return render(request,'view_profile.html', {'profile':e, 'social_info': posts, 'count': str(posts.count()), 'comments_count' : comments_count})







@login_required(login_url = 'login.html')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('id')
    post = Post.objects.all().get(id=post_id)

    like_filter = LikePost.objects.filter(post_id = post_id, user = request.user).first()

    if (like_filter) == None:
        post.likes += 1
        post.save()
        new_like = LikePost.objects.create(post_id = post_id, user = request.user)
        new_like.save()
        return HttpResponseRedirect('browse.html')
    else:
        like_filter.delete()
        post.likes -= 1
        post.save()
        return HttpResponseRedirect('browse.html')


@login_required(login_url = "login.html")
def edit_post(request):

    item_id = request.GET.get('id')
    e = Post.objects.all().get(id=item_id)


    context = {"e":e}


    if request.method == 'POST':
        print(" EDITING  EDITING  EDITING  EDITING  EDITING  EDITING  EDITING  EDITING  EDITING  EDITING  EDITING  EDITING  EDITING  EDITING ")



        if e.post_type == "text":


            content = request.POST['text_content']


            e.text_content = content




        elif e.post_type == "pictures":



            # Saving all the files into the post image fields

            filelist = request.FILES.getlist('post_images')
            for i in range(len(filelist)):

                filename = filelist[i]

                cover_image_result = cloudinary.uploader.upload(filename, resource_type = "auto")

                if hasattr(e, 'image' + str(i + 1)):

                    # Set the value of the field
                    setattr(e, 'image' + str(i + 1), cover_image_result["url"])




            # Saving the caption

            caption = request.POST['caption']

            e.caption = caption



        #Hide likes settings

        hide_likes = request.POST.get("hide_likes")

        if hide_likes == "checkbox":
            e.hide_likes = True
        else:
            e.hide_likes = False


        #Privacy Settings

        privacy = request.POST.get("privacy")

        if privacy == "checkbox":
            e.privacy = True
        else:
            e.privacy = False

        e.user = request.user



        e.save()

        return HttpResponseRedirect("my_profile.html")




    
 







    return render(request,'edit_post.html', context)







@login_required(login_url = "login.html")
def create(request):
    e = Post()

    x = Blog()


    if request.method == 'POST':
        print(" SAVING  SAVING  SAVING  SAVING  SAVING  SAVING  SAVING  SAVING  SAVING  SAVING  SAVING  SAVING  SAVING  SAVING  SAVING  SAVING  SAVING ")



        post_type = request.POST.get("post_type")
        print("The post type is " + post_type)


        if post_type == "text":


            content = request.POST['text_content']


            e.text_content = content



            #Hide likes settings

            hide_likes = request.POST.get("hide_likes")
            if hide_likes == "checkbox":
                e.hide_likes = True
            else:
                e.hide_likes = False


            #Privacy Settings

            privacy = request.POST.get("privacy")

            if privacy == "checkbox":
                e.privacy = True
            else:
                e.privacy = False

            e.user=request.user

            e.post_type = post_type


            e.save()






        elif post_type == "pictures":



            # Saving all the files into the post image fields

            filelist = request.FILES.getlist('post_images')
            for i in range(len(filelist)):

                filename = filelist[i]

                cover_image_result = cloudinary.uploader.upload(filename, resource_type = "auto")

                if hasattr(e, 'image' + str(i + 1)):

                    # Set the value of the field
                    setattr(e, 'image' + str(i + 1), cover_image_result["url"])




            # Saving the caption

            caption = request.POST['caption']

            e.caption = caption




            #Hide likes settings

            hide_likes = request.POST.get("hide_likes")
            if hide_likes == "checkbox":
                e.hide_likes = True
            else:
                e.hide_likes = False


            #Privacy Settings

            privacy = request.POST.get("privacy")

            if privacy == "checkbox":
                e.privacy = True
            else:
                e.privacy = False

            e.user=request.user

            e.post_type = post_type


            e.save()






        elif post_type == "blog":


            x.title = request.POST['title']

            x.body = request.POST['body']

            x.username = request.user.get_username()




            # Saving all the files into the post image fields

            filelist = request.FILES.getlist('article_image')
            for i in range(len(filelist)):

                filename = filelist[i]

                cover_image_result = cloudinary.uploader.upload(filename, resource_type = "auto")

                if hasattr(x, 'image' + str(i + 1)):

                    # Set the value of the field
                    setattr(x, 'image' + str(i + 1), cover_image_result["url"])



            #Hide likes settings

            hide_likes = request.POST.get("hide_likes")
            if hide_likes == "checkbox":
                x.hide_likes = True
            else:
                x.hide_likes = False


            #Privacy Settings

            privacy = request.POST.get("privacy")

            if privacy == "checkbox":
                x.privacy = True
            else:
                x.privacy = False

            x.user=request.user

            x.post_type = post_type


            x.save()

            return HttpResponseRedirect("blogs.html")




        return HttpResponseRedirect("browse.html")



    return render(request,'create.html')











def blogs(request):

    blogs = Blog.objects.all().order_by('-created_at')

    context = {"blogs": blogs}
 
    return render(request,'blogs.html', context)










# @login_required(login_url = "login.html")
# def edit_profile(request):

#     context = {
#         'username': request.user.username,
#         'email': request.user.email,
#         'fname': request.user.first_name,
#         'lname': request.user.last_name,
#     }

#     if request.method == "POST":
#             print(" WORKING WORKING WORKING WORKING WORKING WORKING WORKING WORKING WORKING")

    
 
#     return render(request,'edit_profile.html', context)







@login_required(login_url = "login.html")
def edit_profile(request):

    profile = UserProfile.objects.all().filter(user=request.user)
    for thing in profile:
        profile = thing
    context = {
        'username': request.user.username,
        'email': request.user.email,
        'fname': request.user.first_name,
        'lname': request.user.last_name,
        'profile':profile
    }

    if request.method == "POST":

        print(" EDITING  EDITING  EDITING  EDITING  EDITING  EDITING  EDITING  EDITING ")


        profile = UserProfile.objects.all().filter(user=request.user)
        for x in profile:
            profile = x
            # print()

        newfname = request.POST['fname']
        newlname = request.POST['lname']
        newusername = request.POST['username']
        bio  = request.POST['bio']


        pfp = request.FILES.get('profile_pic', None)


        # Changing their name

        request.user.first_name = newfname

        request.user.last_name = newlname

# Changing username 

        if (newusername):

            user = request.user

            user.username = newusername





# Saving bio

        profile.bio = bio


# Saving pfp

        if pfp is not None:

            pfp_url = cloudinary.uploader.upload(pfp)

            print(pfp_url["url"])

            profile.profile_pic = pfp_url["url"]




        profile.save()

        request.user.save()

        return HttpResponseRedirect("my_profile.html")



        
        
    return render(request,'edit_profile.html', context)






def new_login(request):
     return render(request,'new_login.html')







def sign_in(request):
    if request.method == "POST":
            print(" WORKING WORKING WORKING WORKING WORKING WORKING WORKING WORKING WORKING")
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username = username, password = password)

            if user is not None:
                fname = user.first_name
                login(request, user)


                next_url = request.GET.get('next')
                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    return render(request, "index.html",{'fname' : fname})
                # return render(request, "index.html",{'fname' : fname})

            else:

                messages.error(request, "Incorrect Username or Password")
                return HttpResponseRedirect("login.html")

    print("*******************************NOT WORKING ****************")
    return render(request,'login.html', {})








def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("index.html")


def register(request):



    if request.method == "POST":

        print("************creating a new user *******************************")
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']


        if User.objects.filter(username=username).exists():

            error = True
            print("omg  OMG MMOOOOOOOOOOOOOMFRIF ERHFERIUF    HFUERIFUHERI")

            context = {'error': error}

            return render(request, "register.html", context)


        else: 


            




            email = request.POST['email']
            password1 = request.POST['password']
            password2 = request.POST['conf_password']

            # if User.objects.filter(username = username).first():
            #     print("USERNAME TAKEN ***********************")
            #     messages.error(request, "This username is already taken")
            if  password1 != password2:
                print("PASSWORDS DONT MATCHHHHHHHHHHHHHHH")
                messages.error(request, "The passwrds do not match!")

            else: 
                
                my_user = User.objects.create_user(username, email, password1)
                my_user.first_name = fname
                my_user.last_name = lname

                my_user.save()

                messages.success(request, "Your account has been successfully created.")


                user = authenticate(username = username, password = password1)


                user_profile = UserProfile(user=user, bio="No bio yet.")

                user_profile.save()





                
                if user is not None:
                    fname = user.first_name
                    login(request, user)
                next_url = request.GET.get('next')

                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    return render(request, "index.html",{'fname' : fname})





    print("************NOT creating a new user *******************************")

    return render(request,'register.html')



def about_us(request):
    return render(request, 'about_us.html')




