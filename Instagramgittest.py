

from instagrapi import Client
# This script uses the instagrapi library to upload a media to Instagram.
#variables for username, password, path to photo, and caption are taken as input from the user.



cl = Client()
# Login to Instagram using the provided username and password
def login_info():

    username = input("your_username ")
    password = input("your_password " )
    login_info = cl.login(username, password)
    return login_info


login_info()
# Create a class to handle media uploads
class Media_upload:
    def __init__(self, path_for_media, caption_for_the_media):
        # Upload the media to Instagram with the provided path and caption
        self.path_for_media = path_for_media
        self.caption_for_the_media = caption_for_the_media
    
    def photo_upload(self):
        self.caption_for_the_media= input("caption_for_the_media")
        self.path_for_media = input("path_for_the_media")
        return cl.photo_upload(
            self.path_for_media,
            self.caption_for_the_media
        )
    def video_upload(self):
        self.caption_for_the_media= input("caption_for_the_media")
        self.path_for_media = input("path_for_the_media")
        return cl.video_upload(
            self.path_for_media,
            self.caption_for_the_media
        )
    def album_upload(self):
        self.caption_for_the_media= input("caption_for_the_media")
        self.path_for_media = input("path_for_the_media")
        return cl.album_upload(
            self.path_for_media,
            self.caption_for_the_media
        )
    def clip_upload(self):
        self.caption_for_the_media= input("caption_for_the_media")
        self.path_for_media = input("path_for_the_media")
        return cl.clip_upload(
            self.path_fr_media,
            self.caption_for_the_media
        )   


def action_selection():
    action = input("Enter the action you want to perform (photo_upload/video_upload/album_upload/clip_upload): ")
    media = Media_upload("", "")
    if action == "photo_upload":
        return media.photo_upload()
    elif action == "video_upload":
        return media.video_upload()
    elif action == "album_upload":
        return media.album_upload()
    elif action == "clip_upload":
        return media.clip_upload()
    else:
        print("Invalid action selected.")
        return None


# Call the action_selection function to perform the desired media upload
action_selection()

# Print the media dictionary to see the details of the uploaded photo
print("Photo uploaded successfully!")

