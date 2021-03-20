class script(object):

    START_TEXT = """<b>Hai ,
    
I'm A simple Zee5 link downloader bot With Permanent Thumbnail Support💯.

Please send me any Zee5 link, I can upload it to telegram as File/Video.

Click <i>/help</i> for more details....

You must subscribe our channel in order to use me😇</b>"""


    HELP_USER = """<b>Hai, Follow these steps..</b>
 
1. Send Custom Thumbnail (It will be saved permenantly!)

2. Send your zee5 url and select desired option.


NOTE: Download may take some time! So please wait for it to complete!


Made With ❤ With @VKPROJECTS"""


    ABOUT_TEXT = """⭕️<b>My Name : Zee5 DL</b>

⭕️<b>Creater :</b> @VkProjects

⭕️<b>Language :</b> <code>Python3</code>

⭕️<b>Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a>"""



    FORMAT_SELECTION = """<b>Choose appropriate option</b> <a href='{}'>⬇️</a>

🎞  - Stream format
📁  - File format

<i>NOTE : Taking high resolutions may result in files above 2GB and hence cannot Upload to TG. So better select a medium resolution.</i> 😇
"""    
    
    UPGRADE_TEXT = "Contact @VkBotssupportBot"
    
    DOWNLOAD_START = "Trying to download to my server. This may take a while 😴"
    
    UPLOAD_START = "Uploading Now ⬆️"
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."

    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "**Thank you for Using Meh!! ❤️ Join @VKPROJECTS**"
    
    SAVED_CUSTOM_THUMB_NAIL = "<b>✅Custom thumbnail Saved.\nThis thumbnail will be Permanent for all future uploads\n\nDo /delthumb to clear your thumbnail!</b>"
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom Thumbnail cleared succesfully."
    
    SHOW_THUMB = "@VKPROJECTS\n\nUse /delthumb to clear this thumbnail."
    
    NO_THUMB = "SED😕 No saved thumbnails Found!!"
    
    CUSTOM_CAPTION_UL_FILE = "<b>{newname}\n\n©️ @VKPROJECTS</b>"
    
    TIMEOUT = "<b><i>Sorry for the delay. It'll help reduce the flood wait</i> 😇\n\nWait for {} sec and try again.</b>"
    
