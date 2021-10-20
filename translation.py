class Translation(object):
    START_TEXT = """
<b>Hello {}!!!

I'am a url to telegram file or media uploader bot with permanent thumbnail support.</b>

<i>For More Details check Help 📜</i>
"""
    HELP_TEXT = """
<b>Link to Media or File</b>
- Send a link for upload to telegram file or media.

<b>Set Thumbnail</b>
- Send a photo to make it as permanent thumbnail.

<b>Deleting Thumbnail</b>
- Send /delthumb to deleting thumbnail.

<b>Show Thumbnail</b>
- Send /showthumb to view custom thumbnail.
"""
    ABOUT_TEXT = """
**Bot :** `URL Uploader`
**Creator :** [Vivek](https://telegram.me/vivektvp)
**Channel :** [Vk Projects](https://telegram.me/VKPROJECTS)
**Credits :** `Everyone in this journey`
**Language :** [Python3](https://python.org)
**Library :** [Pyrogram v1.2.0](https://pyrogram.org)
**Server :** [Heroku](https://heroku.com)
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤔 Help', callback_data='help'),
        InlineKeyboardButton('🤖 About', callback_data='about'),
        ],[
        InlineKeyboardButton('Close🔐', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 About', callback_data='about'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠 Home', callback_data='home'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
        ]]
    )
    RENAME_403_ERR = "<b>Sorry. You Are Not Permitted To Rename This File.</b>"
    ABS_TEXT = " <b>Please Don't Be Selfish.</b>"
    UPGRADE_TEXT = "<b>This Bot Is Free To Use If U R My  Friend.</b>"
    FORMAT_SELECTION = "<b>Select The Desired Format:</b> "
    SET_CUSTOM_USERNAME_PASSWORD = """<b>If You Want To Download Premium Videos, Provide In The Following Format:
URL | filename | username | password</b>"""
    NOYES_URL = "<b>This Is Dam Slow Link Bro! I Wont Waste My Time On This. Get Me A Fast Link</b>"
    DOWNLOAD_START = "<b>Downloading Ur Files 🔻</b>"
    UPLOAD_START = "<b>Uploading Ur Files 🔺</b>"
    RCHD_BOT_API_LIMIT ="<b>Size Greater Than Maximum Allowed Size. Neverthless, Trying To Upload.</b>"
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\n<b>Sorry. But, I Cannot Upload Files Greater Than 2GB Due To Telegram API Limitations.</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>File Uploaded Successfully</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "U R Not Authorise To Do This. This Is Only <b>Admin</b> Command"
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription."
    SAVED_CUSTOM_THUMB_NAIL = "<b>Custom video / file thumbnail saved. This image will be used in the video / file.</b>"
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ <b>Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media Cleared Succesfully.</b>"
    SAVED_RECVD_DOC_FILE = "<b>Document Downloaded Successfully.</b>"
    CUSTOM_CAPTION_UL_FILE = " <b>Bot Created By \n   👉 @HxBots</b>"
    NO_CUSTOM_THUMB_NAIL_FOUND = "<b>No Custom ThumbNail Found.</b>"
    NO_VOID_FORMAT_FOUND = "Can You Check The Url? <b>I Am Unable To Detect Video Format From UrL.</b> If You Think This Could Be A Bug Please Report On https://t.me/HxSupport"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """Current plan details
--------
Telegram ID: <code>{}</code>
Plan name: 75GB Per Month
Expires on: 10/12/2021
--------"""
............................
