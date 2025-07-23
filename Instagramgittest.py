
import os
from instagrapi import Client
import logging
# This script uses the instagrapi library to upload a media to Instagram.
#variables for username, password, path to photo, and caption are taken as input from the user.



cl = Client()
# Login to Instagram using the provided username and password
def login_info():
    
       
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
            
            
        

    


   
    login_info = cl.login(username, password)
    return login_info


# Create a class to handle media uploads
class Media_upload:
    def __init__(self, path_for_media, caption_for_the_media):
        # Upload the media to Instagram with the provided path and caption
        self.path_for_media = path_for_media
       


        self.caption_for_the_media = caption_for_the_media


    def __getattribute__(self):
        self.path_for_media = input("path_for_the_media")
        while True: 
            self.path_for_media = input("Enter the path to the media file: ") 
            if os.path.exists(self.path_for_media):
                break
            else:
                print("Invalid path. Please enter a valid path to the media file.")
        self.caption_for_the_media = input("caption_for_the_media")


    
    def photo_upload(self):
        
        return cl.photo_upload(
            self.path_for_media,
            self.caption_for_the_media
        )
    def video_upload(self):
        
        return cl.video_upload(
            self.path_for_media,
            self.caption_for_the_media
        )
    def album_upload(self):
        
        return cl.album_upload(
            self.path_for_media,
            self.caption_for_the_media
        )
    def clip_upload(self):
        
        return cl.clip_upload(
            self.path_for_media,
            self.caption_for_the_media
        )   


def action_selection():
  while True:
          action = input("Enter the action you want to perform (photo upload/video upload/album upload/clip upload): ")
          action = action.strip().lower()

          if action in ["photoupload", "videoupload", "albumupload", "clipupload"]:
                media = Media_upload("","")
                media.__getattribute__()
                # Perform the selected action based on user input
                if action == "photoupload":
                    return media.photo_upload()
                elif action == "videoupload":
                    return media.video_upload()
                elif action == "albumupload":
                    return media.album_upload()
                elif action == "clipupload":
                    return media.clip_upload()
            
         
           
          else:     
              print("Invalid action selected. Please try again.")


# Call the action_selection function to perform the desired media upload


# Print the media dictionary to see the details of the uploaded photo




if __name__ == "__main__":

    while True:
        try:
            login_info()            
            break
        except Exception as e:
            print(f"Login failed: {e}. Please try again.")
            continue
    try:
       while True:
         action_selection()
         print(f"Media  uploaded successfully!")



    except Exception as e:
        print(f"An error occurred during media upload: {e}. Please try again.")

   

