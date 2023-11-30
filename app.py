import os
import requests
from github import Github

# Environment Variables
username = os.getenv('USERNAME')
ignore_list = os.getenv('IGNORE_LIST').split(',')
access_token = os.getenv('GH_ACCESS_TOKEN')
g = Github(access_token)

def get_github_username():
    return input("Enter your GitHub username: ")

def get_followers(username):
    followers = []
    page = 1
    while True:
        url = f'https://api.github.com/users/{username}/followers'
        params = {'per_page': 100, 'page': page}
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            followers_page = response.json()
            if not followers_page:
                break
            followers.extend(followers_page)
            page += 1
        else:
            print(f"Failed to fetch followers. Status code: {response.status_code}")
            break

    print('Your followers is: ', len(followers))
    return [follower['login'] for follower in followers]

def get_following(username):
    following = []
    page = 1
    while True:
        url = f'https://api.github.com/users/{username}/following'
        params = {'per_page': 100, 'page': page}
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            following_page = response.json()
            if not following_page:
                break
            following.extend(following_page)
            page += 1
        else:
            print(f"Failed to fetch following. Status code: {response.status_code}")
            break

    print('Your following is: ', len(following))
    return [follow['login'] for follow in following]

def get_profile_link(username):
    url = f'https://github.com/{username}'
    return url

def find_unfollowed(followers, following, ignore_list):
    followers_set = set(followers)
    following_set = set(following)
    
    unfollowed_users = following_set - followers_set
    unfollowed_users = [user for user in unfollowed_users if user not in ignore_list]
    
    return unfollowed_users

def print_profile_links(unfollowed_users):
    print("Profiles of users you follow but who don't follow you back:")
    for username in unfollowed_users:
        profile_link = get_profile_link(username)
        print(profile_link)

def unfollow_users(users):
    for user in users:
        g.get_user().remove_from_following(g.get_user(user))

def main():
    followers = get_followers(username)
    following = get_following(username)

    if followers and following:
        unfollowed_users = find_unfollowed(followers, following, ignore_list)
        if unfollowed_users:
            print_profile_links(unfollowed_users)
            unfollow_users(unfollowed_users)

if __name__ == "__main__":
    main()
