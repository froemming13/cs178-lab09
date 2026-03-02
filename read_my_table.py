REGION = "us-east-1"
TABLE_NAME = "Playlist"

def get_table():
    """Return a reference to the DynamoDB Movies table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)

def print_songs(song):
    """Print one song's details in a readable format."""
    title = song.get("Title", "Unknown Title")
    artist = song.get("Artist", "Unknown Artist")
    album = song.get("Album", "No Album")

    print(f"  Title : {title}")
    print(f"  Artist  : {artist}")
    print(f"  Album: {album}")
    print()

def print_all_playlist_songs():
    """Scan the entire Playlist table and print each item."""
    table = get_table()
    
    # scan() retrieves ALL items in the table.
    # For large tables you'd use query() instead — but for our small
    # dataset, scan() is fine.
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No songs found. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} song(s):\n")
    for song in items:
        print_songs(song)

def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_playlist_songs()

if __name__ == "__main__":
    main()