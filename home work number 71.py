songs = [
    ["Believer", "Imagine Dragons"],
    ["Shape of You", "Ed Sheeran"],
    ["Perfect", "Ed Sheeran"]
]

song_name = input("Enter the song name: ")
singer_name = input("Enter the singer name: ")

found = False

for song in songs:
    if song[0] == song_name and song[1] == singer_name:
        print(song)
        found = True

if not found:
    print("The song was not found.")
