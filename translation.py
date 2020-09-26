class Translation(object):
    START_TEXT = """Hello {}, I am Smart Rename Bot! Developed by @Grainhanks
<b>Please send me any Telegram file and reply to that file to /rename New Name.mkv</b>

/help for more details.."""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "<b>Don't worry! We update this bot regularly to make it much better.. </b>\n/help for Details"
    DOWNLOAD_START = "Trying to download.."
    UPLOAD_START = "Trying to upload.."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.5GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "**Thank you for Using me.**"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://t,me/grainhanks'>Owner</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom File thumbnail saved. This image will be used in the File."
    DEL_ETED_CUSTOM_THUMB_NAIL = "Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    HELP_USER = """
	Steps to use :-    
	Step 1. Upload or forward any video or file.
	Step 2. Upload thumbnail image.
	Step 3. Reply to that video "/rename" New name.extension.

Use /deletethumbnail to clear your custom thumbnail.
"""
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to `/rename New Name.extension` with custom thumbnail support.."
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    IFLONG_FILE_NAME = """File Name limit allowed by Telegram is {alimit} characters.
The given file name has {num} characters.

<b>Essays Not allowed in Telegram file name!</b><code>@SmartRenameBot</code>
Please short your file name and try again!"""
