
import facebook

# Replace with your access token and page ID
access_token = "EAAb4AhdJkqwBPG5rIbcqXyVY9qZAv3w5t8Fkf0kCRZBN3B5kccBwvwgsUdjZBxcUSZCWYcJ5BZCWAFHnZB5KEDVVUcOE5Udsnm2HnTgWFAS5n367m3QCP6vJnvnePbJGh1YGEbHoURqQqhvpYZCtZBpZBcfuplcVSTRLxQZCY9FHhQIeP54VWZAx3DdWBC5SW4VoyRlrnSzXcF8tMSN0oP7Jyq5WHySFW8wVN7bmrnHCg6I0QZDZD"


page_id = "109560885411387"

try:
    graph = facebook.GraphAPI(access_token=access_token)
   
    def post_to_facebook():
        Type_of_post = input("Enter the type of post you want to make (text/image): ")
        if Type_of_post == "text":
            message = input("Enter your message: ")
            graph.put_object(parent_object=page_id, connection_name='feed', message=message)
            print("Text post successful!")
        elif Type_of_post == "image":
            image_path = input("Enter the path to your image: ")
            caption = input("Enter a caption for the image: ")
            graph.put_photo(image=open(image_path, 'rb'), message=caption)
            print("Image post successful!")
        else:
            print("Invalid post type. Please enter 'text' or 'image'.")
        
        
        
    post_to_facebook()
   
    

except facebook.GraphAPIError as e:
    print(f"Error: {e}")



