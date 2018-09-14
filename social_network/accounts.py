class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name.lstrip('first_name=')
        self.last_name = last_name.lstrip('last_name=')
        self.email = email.lstrip('email=')
        self.posts = []
        self.following = []

    # Maintain list of user's posts and associate the post with the user
    def add_post(self, post):
        self.posts.append(post)
        post.set_user(self)

    # Maintain list of other users being followed
    def follow(self, other):
        self.following.append(other)

    def get_timeline(self):
        # Get (unordered) list of posts from all followed users
        following_posts = [post for user in self.following for post in user.posts]

        # Extension of sorted relies on __lt__ definition in Posts class
        return sorted(following_posts, reverse=True)

