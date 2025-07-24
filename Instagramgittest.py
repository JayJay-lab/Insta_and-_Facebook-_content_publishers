

from instagrapi import Client

# This script uses the instagrapi library to upload a media to Instagram.
#variables for username, password, path to photo, and caption are taken as input from the user.



cl = Client()
# Login to Instagram using the provided username and password
def collect_login_info():
    
       
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
            
    return cl.login(username, password)


# Create a class to handle media uploads
class MediaUpload:
    def __init__(self, path_for_images, caption_for_the_images):
        # Upload the media to Instagram with the provided path and caption
       self.path_for_images = path_for_images
       self.caption_for_the_images = caption_for_the_images


    


    
    def photo_upload(self):
        
        return cl.photo_upload(
            self.path_for_images,
            self.caption_for_the_images
        )
       


def post_to_instagram(path_for_images, caption_for_the_images):
  while True:
          

          try:
                media = MediaUpload(path_for_images, caption_for_the_images)
                media.photo_upload()
                break
          except Exception as e:
                print(f"An error occurred during image upload: {e}. Please try again.")
                   
                
                
         
           
         







   

