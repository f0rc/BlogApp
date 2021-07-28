# Allow anyone to view any public posts.
allow(_actor, "view", post: social::Post) if
    post.access_level = social::Post.ACCESS_PUBLIC;

# Allow a user to view their private posts.
allow(actor: social::User, "view", post: social::Post) if
    post.access_level = social::Post.ACCESS_PRIVATE and
    post.author = actor;

# Moderators can view any Post.
#allow(user: social::User, "view", _: social::Post) if
#    user.is_moderator;

# Moderators can perform moderation on any Post.
#allow(user: social::User, "moderate", _: social::Post) if
    #user.is_moderator;

# Allow anyone to view any public posts.
#allow(_actor, "view", post: social::Post) if
    # NEW - Public posts must be approved by moderators.
    #post.approved and
    #post.access_level = social::Post.ACCESS_PUBLIC;

# Allow a user to view their private posts.
#allow(actor: social::User, "view", post: social::Post) if
    #post.access_level = social::Post.ACCESS_PRIVATE and
    #post.created_by = actor;