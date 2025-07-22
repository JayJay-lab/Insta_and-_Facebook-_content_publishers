     
# 📱 Social Media Poster

A simple Python script to automatically post images and text to **Instagram** and **Facebook**.

---

## 🚀 Features

- 📸 Post images with captions to Instagram and Facebook.
- 🔐 Simple authentication setup for both platforms.
- 🧰 Clean and easy-to-use codebase for automation or integration into larger projects.

---

## 📆 Prerequisites

### Instagram

- Install the required library:
  ```bash
  pip install InstagramApi


  I used a open source library    https://subzeroid.github.io/instagrapi/.
  ```
- Provide your **Instagram username** and **password** in the script.

> **Note**: Instagram often blocks unofficial APIs, so functionality may break depending on Instagram’s API changes.

### Facebook

- Install the Facebook :
  ```bash
  pip install facebook

  documentation for this library is at  facebook-sdk.readthedocs.io  
  ```
- Create a **Facebook Developer** account: [developers.facebook.com](https://developers.facebook.com)
- Create an app and retrieve:
  - App ID
  - Page ID
  - Page Access Token with `pages_manage_posts` and `pages_read_engagement` permissions.

---

## ⚙️ Configuration

Edit the script to include your credentials:

```python
# Instagram
INSTAGRAM_USERNAME = 'your_username'
INSTAGRAM_PASSWORD = 'your_password'

# Facebook
FACEBOOK_APP_ID = 'your_app_id'
FACEBOOK_PAGE_ID = 'your_page_id'
FACEBOOK_ACCESS_TOKEN = 'your_page_access_token'
```

> Keep these credentials secure. Do **not** hardcode sensitive data in production code.

---

## 🛠️ Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/social-media-poster.git
   cd social-media-poster
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your credentials** inside the script.

4. **Run the script**:

   ```bash
   python post_to_socials.py
   ```

---

## 🤝 Contributing

Contributions are welcome!\
Feel free to fork the repository and submit a pull request.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add awesome feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---



---

## 📬 Contact

Created by **LuckyPhomane56@gmail.com** — feel free to reach out or report issues via GitHub!


