## Djamg-Twitter-Clone

### ==Description==</h3>
This is a social media site that functions similarly to twitter where you can share short statements and view a feed where can view other user's post and like it as well. You can follow and unfollow people and also view your profile to see how many followers you have. All of your post appear on your profile where you can edit or delete them. You can view a demo to the site at the bottom of this page, enjoy!

### ==Files and directories==
- `network` - Main application directory.
  - `static/network` - Contains all static files.
    - `static.js` - Contains all of the Javascript for the app.
    - `styles.css` - Contains all the css for the app.
  - `template/network` - Contains all html files for the app.
    - `layout.html` - The base template that all other templates extend.
    - `index.html` - Main template or "homepage".
    - `following.html` - A page where you can see a feed of post of all the people you follow.
    - `login.html` - The login page to sign into your account.
    - `profile.html` - The profile page for whichever user's profile you visit.
    - `register.html` - The page where you sign up to make an account.
  - `admin.py` - File registering your models for the admin page.
  - `models.py` - File containing all of the models for the database.
  - `urls.py` - Contains all the urls for the app.
  - `views.py` - Contains all the views for the app.
- `scraper` - Project directory.

Demo link https://movie-ratings-scraper.herokuapp.com/