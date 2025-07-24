import Instagramgittest
import facebook_api
import os







def main():


   


    while True:
       # Login to Facebook and  Instagram
      try:
        facebook_api.graph
        break


      except Exception as e:        
        print(f"Facebook login failed: {e}. Please try again.")



    while True:
        try:
            Instagramgittest.collect_login_info()
            break
        except Exception as e:
            print(f"Instagram login failed: {e}. Please try again.")


    print("Login successful!")

    # Perform actions on Facebook and Instagram
    def collect_image_path():
        # Collect image path from user
      while True:
                image_path = input("Enter the path to your image: ")
                if  os.path.exists(image_path):
                    break
                else:
                    raise FileNotFoundError(f"The image path '{image_path}' does not exist.")
      return image_path
    
    def collect_caption():
        # Collect caption from user
        caption = input("Enter a caption for the image: ")
        if not caption:
            raise ValueError("Caption cannot be empty.")
        return caption
    caption = collect_caption()
    
    image_path = collect_image_path()

    # Post to Facebook & Instagram
    
    facebook_api.post_to_facebook(image_path, caption)
    Instagramgittest.post_to_instagram(image_path, caption)

    if input("Do you want to post another image? (yes/no): ").lower() != 'yes':
             

     print("All posts completed successfully!")




if __name__ == "__main__":
    main()


    
