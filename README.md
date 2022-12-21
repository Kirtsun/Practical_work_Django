## This is a practical work on django
### This mini app is a blog. You can do the following:
- Register, change your data and password
- Create and edit your posts
- Create comments
- View pages of other users
- View all available posts
- Each time a post and comment is created, the admin will receive a notification by mail (to the console)
- After moderating a comment, the user will receive a notification by mail (to the console),
along with a link to the post

## Quick start
To run locally, you need to install dependencies. 
To quickly populate the base, you can use commands or fixtures.

- To populate the database with random users, use the "create_user <int>" command. Instead of <int> enter the number
of users to make from 1 -500.
- To create a post, use the create_post <int> command, where <int> is the number of posts to be created from 1 -500. 
If there is no user, there will be an error!
- To create a comments, use the create_comment <int> command, where <int> is the number of comment to be created from 1 -500. 
If there is no post, there will be an error!

Or you can use "Fixture"
