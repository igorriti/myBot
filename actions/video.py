from random import choice

from pyyoutube import Api



MAX_TOKENS = 1000



def get_random_id(api, playlist_id):
    """Get a random video ID from a YouTube Playlist
    Args:
        api (pyyoutube.api.API):
        playlist_id ([type]): YouTube Playlist ID
    """

    playlist = api.get_playlist_items(playlist_id=playlist_id, count=None)
    video_id_list = [i.snippet.resourceId.videoId for i in playlist.items]

    return choice(video_id_list)

def get_video_info(api, video_id):
    """Get URL, title and description from YouTube video
    Args:
        api (pyyoutube.api.API):
        video_id (str): YouTube video ID
    Returns:
        dict: Dictionary containing video info
    """

    video = api.get_video_by_id(video_id=video_id).to_dict()

    title = video["items"][0]["snippet"]["title"]
    url = f"https://youtu.be/{video_id}"

    return {"url": url, "title": title}


def get_random_video():


    video_id = get_random_id(yt_api, "PL-Ogd76BhmcDxef4liOGXGXLL-4h65bs4")
    info = get_video_info(yt_api, video_id)
    
    return info

