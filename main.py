from dotenv import load_dotenv
from utils.ghost import create_post
from utils.agno import generate_blog_post

load_dotenv()

title = ""
markdown = generate_blog_post(title)
create_post(title, ["tag1", "tag2"], ["ghostemail@example.com"], markdown)
