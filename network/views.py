from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from .models import User, profile, post


def index(request):
    objects = post.objects.all().order_by("-date_posted")
    if (len(objects) <= 10):
        page_obj = objects
    else:
        posts = Paginator(objects, 10)

        page_number = request.GET.get("page")
        page_obj = posts.get_page(page_number)
    return render(request, "network/index.html", {
        "page_obj": page_obj
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        Profile = profile()
        Profile.user = user
        Profile.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def new_post(request):
    if (request.method == "POST"):
        # creates new post for user #
        Post = post()
        Post.body = request.POST.get("text")
        Post.user = request.user
        Post.save()

        return HttpResponseRedirect(reverse("index"))

def user_profile(request, id):
    profile_user = User.objects.get(id = id)
    Profile = profile.objects.get(user = profile_user)
    objects = post.objects.filter(user = profile_user).order_by("-date_posted")
    if (len(objects) <= 10):
        page_obj = objects
    else:
        posts = Paginator(objects, 10)

        page_number = request.GET.get("page")
        page_obj = posts.get_page(page_number)
    
    return render(request, "network/profile.html", {
        "profile": Profile,
        "page_obj": page_obj
    })
    

def follow(request):
    if (request.method == "POST"):
        profile_user = User.objects.get(username = request.POST.get("profile-user"))
        Profile = profile.objects.get(user = profile_user)
        users_profile = profile.objects.get(user = request.user)
        
        if not (request.user in Profile.followers.all()):
            Profile.followers.add(request.user)
            users_profile.following.add(Profile.user)
        else:
            Profile.followers.remove(request.user)
            users_profile.following.remove(Profile.user)

        return HttpResponseRedirect(reverse("user_profile", args = (profile_user.id,)))


def following(request):
    # gets all of the post for the users that the current user follows #
    Profile = profile.objects.get(user = request.user)
    objects = post.objects.all().order_by("-date_posted")
    if (len(objects) <= 10):
        page_obj = objects
    else:
        posts = Paginator(objects, 10)

        page_number = request.GET.get("page")
        page_obj = posts.get_page(page_number)

    return render(request, "network/following.html", {
        "page_obj": page_obj,
        "profile": Profile
    })


def like_post(request, post_id):
    # Saves the like for the post that user clicked on #
    Post = post.objects.get(id = post_id)

    if not (request.user in Post.likes.all()):
        Post.likes.add(request.user)
        action = 1
    else:
        Post.likes.remove(request.user)
        action = 2

    return JsonResponse({"action": action, "like_count": Post.likes.count()}, status = 201)

@csrf_exempt
def edit_post(request, post_id):
    # allows the user to edit their post and save it #
    if (request.method == "POST"):
        data = json.loads(request.body)
        body = data.get("body", "")

        Post = post.objects.get(id = post_id)
        Post.body = body
        Post.save()

    return JsonResponse({"status": 201}, status = 201)