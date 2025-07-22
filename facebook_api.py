
import facebook

# Replace with your access token and page ID




    

try:
        

        def post_to_facebook():
            access_token = input("Enter your Facebook access token: ")
            page_id = input("Enter your Facebook page ID: ")
            graph = facebook.GraphAPI(access_token=access_token)
            post_type = input("Enter the type of post you want to make (text/image): ")
            if post_type == "text":
                message = input("Enter your message: ")
                graph.put_object(parent_object=page_id, connection_name='feed', message=message)
                print("Text post successful!")
            elif post_type == "image":
                image_path = input("Enter the path to your image: ")
                caption = input("Enter a caption for the image: ")
                graph.put_photo(image=open(image_path, 'rb'), message=caption)
                print("Image post successful!")
                
            else:
                print("Invalid post type. Please enter 'text' or 'image'.")
        
        try:
           post_to_facebook()

        except FileNotFoundError as e:
            print(f"Error: {e}. Please check the image path.")



except facebook.GraphAPIError as e:
        print(f"Error: {e}")

