"""
Function called parse
1. Extract the src attribute from <iframe> tags.
2. Check if it matches one of the YouTube embed formats.
3. Convert it into the https://youtu.be/VIDEO_ID format.
4. Return None if no valid YouTube embed URL exists
"""
import re

def main():
    print(parse(input("HTML: ")))

#def modular function that'll parse the input string and output a shareable link
def parse(s):

    """
    Extract YT embedded URL from HTML iframe and convert it to a shareable short YT URL
    """

    #RegEx to find iframe src containing a YT embed link
        # "src = ...": start looking for the src attribute
        # "https?:// :" makes the s optional
        # (?:www\.)? : makes www. optional but also not captured, so not indexed
        # youtube\.com/embed/: ensures the YT UTL is embedded
        # [a-zA-Z)-9_-]+ : captures video ID and includes _ and -
        # eg:<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    match = re.search(r'<iframe[^>]+src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s)
    # <iframe[^>]+: Match an <iframe tag and then capture everything up until the first > (end of the opening tag).
    # +: one or more of these chars

    #if match is found, return the youtu.be link
    if match:
        video_id = match.group(1) #the only solid(capturing) group ([a-zA-Z0-9_-]+)
        return f"https://youtu.be/{video_id}"

    #If match is truthy → the function returns inside the if block, so it never reaches the return None.
    #If match is falsy → the if block is skipped, and Python continues down to return None.
    return None

if __name__ == "__main__":
    main()
