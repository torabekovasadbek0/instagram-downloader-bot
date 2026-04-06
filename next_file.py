# next_file.py
# Instagram videolarini yuklash funksiyalari

import instaloader

# Instaloader obyektini yaratish
L = instaloader.Instaloader()

def download_instagram_video(url: str, save_path: str = "./") -> str:
    """
    Instagram post videoni yuklaydi.
    url: Instagram post linki
    save_path: video saqlanadigan papka
    return: video fayl nomi yoki xato xabar
    """
    try:
        # Post qisqacha kodini olish
        shortcode = url.split("/")[-2]
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        
        # Videoni yuklash
        L.download_post(post, target=save_path)
        return f"Video muvaffaqiyatli yuklandi: {save_path}{post.shortcode}"
    except Exception as e:
        return f"Xato: {e}"
