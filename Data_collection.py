import praw
import pandas as pd
import time

# Reddit API Credentials
reddit = praw.Reddit(
    client_id="Place your client ID",
    client_secret="Palce your client secret",
    user_agent="Your Useragent name",
    username="Your Username",
    password="Password of your reddit id"
)

# Multi-domain subreddit list
subreddits = [
    "Cybersecurity", "QuantumComputing", "Space", "Engineering",
    "stocks", "CryptoCurrency", "wallstreetbets", "economy", "investing", "business",  # Finance
    "PersonalFinance", "RealEstate", "SideHustle", "Ecommerce",
    "Productivity", "Minimalism", "Stoicism", "Fitness", "Cooking",
    "Photography", "DIY", "Writing", "Travel"
]

# Store collected data
posts = []

# Loop through each subreddit and collect posts
for sub in subreddits:
    subreddit = reddit.subreddit(sub)
    print(f"Collecting posts from r/{sub}...")

    try:
        for post in subreddit.hot(limit=100000):  # Get top 200 posts per subreddit
            posts.append([
                sub,  # Subreddit name
                post.title, 
                post.selftext, 
                post.score, 
                post.num_comments, 
                post.created_utc, 
                post.url
            ])
        time.sleep(2)  # Prevent hitting API rate limits
    except Exception as e:
        print(f"Error collecting from r/{sub}: {e}")

# Convert list to DataFrame
df = pd.DataFrame(posts, columns=["Subreddit", "Title", "Text", "Score", "Comments", "Time", "URL"])

# Save to CSV
df.to_csv("Your Location to save raw reddit dataset", index=False)

print("Data collection complete! Check reddit_large_dataset.csv")
