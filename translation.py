class Translation(object):
    START_TEXT = """Hi {},\n
I am Extreme Uploader Bot\n
You can upload HTTP/HTTPS direct link, Using this bot!\n
Use help Command for more details!"""
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    DOWNLOAD_START = "Downloading Content to My Server"
    UPLOAD_START = "Now Uploading.."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Thanks for using @ExtremeUploaderBot"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds.\n\n@xurluploaderbot"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    HELP_USER = """How to Use Me? Follow These steps!
    
1. Send url (example.domain/File.mp4 | New Filename.mp4).
2. Send Image As Custom Thumbnail (Optional).
3. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File (video) as file with Screenshots
   Video  - Give File as video without Screenshots
   File   - Give File without Screenshots

If bot didn't respond, contact @Tellybots_support"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /genthumbnail to a media album, to generate custom thumbnail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    REPLY_TO_DOC_GET_LINK = "<b>Reply to a Telegram media to get High Speed Direct Download Link.</b>"
    REPLY_TO_DOC_FOR_C2V = "<b>Reply to a Telegram Media To Convert.</b>"
    REPLY_TO_DOC_FOR_SCSS = "<b>Reply to a Telegram Media To Get Screenshots.</b>"

    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """Current plan details
--------
Telegram ID: <code>{}</code>
Plan name: 75GB Per Month
Expires on: 10/12/2021
--------"""
    REPLY_TO_DOC_GET_LINK = "<b>Reply to a Telegram media to get High Speed Direct Download Link.</b>"
    REPLY_TO_DOC_FOR_C2V = "<b>Reply to a Telegram Media To Convert.</b>"
    REPLY_TO_DOC_FOR_SCSS = "<b>Reply to a Telegram Media To Get Screenshots.</b>"
    SOURCE = """<b>Hi!,</b>

<b>○ My Name : <i>Hx AnyDLBot</i></b>
<b>○ Creator : <a href='https://telegram.dog/Kirodewal'>This Person</a></b>
<b>○ Credits : Everyone In This Journey</b>
<b>○ Language : Python 3.9</b>
<b>○ Library : Pyrogram Asyncio</b>
<b>○ Cloned From : AnyDLBot [Spechide]</b>
<b>○ Source Code :  <a href='https://t.me/HxSourceCode/2'>👉 Click Here</a></b>
<b>○ Server : <a href='aws.amazon.com'>AWS Amazon</a></b>
<b>○ Build Status : Beta v1</b>"""
    REPLY_TO_DOC_FOR_RENAME_FILE = "<b>Reply to a Telegram Media To /rename With Custom Thumbnail Support.</b>"
    AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days."
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "<b>First send /downloadmedia To Any Media So That It Can Be Downloaded To My Local. \nSend /Storageinfo To Know The Media, That Is Currently Downloaded.</b>"
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia To Delete This Media, From My Storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t A Small Photo / Video, From The Above Media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "<b>A Saved Media Already Exists. Please Send /Storageinfo To Know The Current Media Details.</b>"
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "<b>Reply to a Telegram media (MKV), to extract embedded streams.</b>"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "<b>Reply /generatecustomthumbnail to a media album, to generate custom thumbail</b>"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "<b>Media Album Should Contain Only Two Photos. Please Re-send The Media Album, And Then Try Again, Or Send Only Two Photos In An Album.</b>"
    INVALID_UPLOAD_BOT_URL_FORMAT = "<b>URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension</b>"
    ABUSIVE_USERS = "<b>You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction.</b>"
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "Holy Shit!!"
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice."
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
 users only 1 request per 5 minutes.
/upgrade or Try 300 seconds later."""
    SLOW_URL_DECED = "Gosh That Seems To Be A Very Slow URL. Since You Were Screwing My Home, I Am In No Mood To Download This File. Meanwhile, Why Don't You Get Me A Fast URL So That I can Upload To Telegram, Without Me Slowing Down For Other Users."
    IFLONG_FILE_NAME = """File Name limit allowed by Telegram is {alimit} characters.
The given file name has {num} characters.

<b>Essays Not allowed in Telegram file name!</b>
Please short your file name and try again!"""
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media Cleared Succesfully.</b>"
    SAVED_RECVD_DOC_FILE = "<b>Document Downloaded Successfully.</b>"
    NO_CUSTOM_THUMB_NAIL_FOUND = "<b>No Custom ThumbNail Found.</b>"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """Current plan details
--------
Telegram ID: <code>{}</code>
Plan name: 75GB Per Month
Expires on: 10/12/2021
--------"""
