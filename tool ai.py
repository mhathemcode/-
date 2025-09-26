import lyricsgenius

# ===================== إعداد Genius API =====================
GENIUS_API_KEY = "rRr_6Buopaychnj5yiWEv4VooPLxbW65Jhj_xd1HG7w9de3G4Wi6XJtz8NmOY30m"
genius = lyricsgenius.Genius(GENIUS_API_KEY)
genius.skip_non_songs = True
genius.excluded_terms = ["(Remix)", "(Live)"]

# ===================== البحث عن كلمات الأغاني =====================
def get_lyrics(song_name, artist_name):
    try:
        song = genius.search_song(song_name, artist_name)
        if song:
            return song.lyrics
        else:
            return "❌ لم يتم العثور على كلمات الأغنية."
    except Exception as e:
        return f"❌ حدث خطأ: {e}"

# ===================== واجهة الشات بوت =====================
def main():
    print("🎵 مرحبًا! ادخل اسم الأغنية واسم المغني:")
    song_name = input("اسم الأغنية: ")
    artist_name = input("اسم المغني: ")

    print("\n🔎 جارٍ البحث عن كلمات الأغنية...\n")
    lyrics = get_lyrics(song_name, artist_name)
    print("🎤 كلمات الأغنية:\n")
    print(lyrics)

if __name__ == "__main__":
    main()