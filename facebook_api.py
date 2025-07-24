import os
import facebook

# Replace with your access token and page ID




    

try:
    def collect_login_info():
        # Collect Facebook login information

        while True: 
          access_token = input("Enter your Facebook access token: ")    
          if  access_token == "":
            raise ValueError("Access token cannot be empty.")   
          else:
            return facebook.GraphAPI(access_token)

          
    graph = collect_login_info() 

    def post_to_facebook(path, caption):     
           
             
            
             
             graph.put_photo(image=open(path, 'rb'), message=caption)
             print("Image post successful!")
                
            
        
    

except facebook.GraphAPIError as e:
        print(f"Error: {e}")

