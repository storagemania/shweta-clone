#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = '👸🏻 Owner'
    ST_BN1_URL = 'https://t.me/Shizuka_Official'
    ST_BN2_NAME = '😘 Use Me'
    ST_BN2_URL = 'https://t.me/+u7q5EbVumvo2ZDFl'
    ST_MSG = '''<i>This bot can leech all your direct links|files|torrents to Telegram.</i>
<b>Type {help_command} to get a list of available commands</b>'''
    ST_BOTPM = '''<i>🕵Now, This bot will send all your files and links here. Start Using ...</i>'''
    ST_UNAUTH = '''<i>⚠️ You Are not authorized user!</i>'''
    OWN_TOKEN_GENERATE = '''<b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i>'''
    USED_TOKEN = '''<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>'''
    LOGGED_PASSWORD = '''<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>'''
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = '''<b><u>Generated Temporary Login Token!</u></b>
<b>Temp Token:</b> <code>{token}</code>
<b>Validity:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅️ Activated ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>Already Bot Login In!</b>'
    INVALID_PASS = '<b>Invalid Password!</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>Bot Permanent Login Successfully!</b>'
    LOGIN_USED = '<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Log Display'
    WEB_PASTE_BT = '📨 Web Paste (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = '✍🏻 Basic'
    USER_BT = '👤 Users'
    MICS_BT = '💫 Mics'
    O_S_BT = '🛡️ Owner & Sudos'
    CLOSE_BT = '🚫 Close 🚫'
    HELP_HEADER = "㊂ <b><i>Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor detalis.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''┎ <b><i>🤖 BOT STATISTICS :</i></b>
┖ <b>⏰ Bot Uptime :</b> {bot_uptime}

┎ <b><i>💽 RAM ( MEMORY ) :</i></b>
┃ {ram_bar} {ram}%
┠ <b>☞ Used :</b> {ram_u} 
┠ <b>☞ Free :</b> {ram_f} 
┖ <b>☞ Total :</b> {ram_t}

┎ <b><i>👒 SWAP MEMORY :</i></b>
┃ {swap_bar} {swap}%
┠ <b>☞ Used :</b> {swap_u} 
┠ <b>☞ Free :</b> {swap_f} 
┖ <b>☞ Total :</b> {swap_t}

┎ <b><i>📦 DISK :</i></b>
┃ {disk_bar} {disk}%
┠ <b>☞ Total Disk Read :</b> {disk_read}
┠ <b>☞ Total Disk Write :</b> {disk_write}
┠ <b>☞ Used :</b> {disk_u} 
┠ <b>☞ Free :</b> {disk_f} 
┖ <b>☞ Total :</b> {disk_t}
    
<a href="https://t.me/Shizuka_Official"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 @Shizuka_Official</b></a>
    '''
    SYS_STATS = '''┎ <b><i>🛠 OS SYSTEM :</i></b>
┠ <b>⏰ OS Uptime :</b> {os_uptime}
┠ <b>☢️ OS Version :</b> {os_version}
┖ <b>🔧 OS Arch :</b> {os_arch}

┎ <b><i>📶 NETWORK STATS :</i></b>
┠ <b>🔺 Upload Data:</b> {up_data}
┠ <b>🔻 Download Data:</b> {dl_data}
┠ <b>🔼 Pkts Sent:</b> {pkt_sent}k
┠ <b>🔽 Pkts Received:</b> {pkt_recv}k
┖ <b>📊 Total I/O Data:</b> {tl_data}

┎ <b>🖥️ CPU :</b>
┃ {cpu_bar} {cpu}%
┠ <b>☞ CPU Frequency :</b> {cpu_freq}
┠ <b>☞ System Avg Load :</b> {sys_load}
┠ <b>☞ P-Core(s) :</b> {p_core} 
┠ <b>☞ V-Core(s) :</b> {v_core}
┠ <b>☞ Total Core(s) :</b> {total_core}
┖ <b>☞ Usabl e CPU(s) :</b> {cpu_use}

<a href="https://t.me/Shizuka_Official"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 @Shizuka_Official</b></a>
    '''
    REPO_STATS = '''┎ <b><i>🧑‍💻 REPO STATISTICS :</i></b>
┠ <b>🤖 Bot Updated :</b> {last_commit}
┠ <b>🆔 Current Version :</b> {bot_version}
┠ <b>🎈 Latest Version :</b> {lat_version}
┠ <b>📝 Last ChangeLog :</b> {commit_details}
┖ <b>💥 REMARKS :</b> <code>{remarks}</code>
 
<a href="https://t.me/Shizuka_Official"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 @Shizuka_Official</b></a>
    '''
    BOT_LIMITS = '''┎ <b><i>❗ BOT LIMITATIONS :</i></b>
┠ <b>🎯 Direct Limit :</b> {DL} GB
┠ <b>🧲 Torrent Limit :</b> {TL} GB
┠ <b>☁️ GDrive Limit :</b> {GL} GB
┠ <b>📺 YT-DLP Limit :</b> {YL} GB
┠ <b>🎥 Playlist Limit :</b> {PL}
┠ <b>Ⓜ️ Mega Limit :</b> {ML} GB
┠ <b>🎗️ Clone Limit :</b> {CL} GB
┖ <b>📂 Leech Limit :</b> {LL} GB

┎ <b>🔑 Token Validity :</b> {TV}
┠ <b>🐢 User Time Limit :</b> {UTI} / task
┠ <b>👤 User Parallel Tasks :</b> {UT}
┖ <b>🤖 Bot Parallel Tasks :</b> {BT}

<a href="https://t.me/Shizuka_Official"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 @Shizuka_Official</b></a>
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>🔄 Restarting...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''┎ <b><i>♻️ Restarted Successfully! 🎉</i></b>
┠ <b>📅 Date:</b> {date}
┠ <b>⌚ Time:</b> {time}
┠ <b>🌐 TimeZone:</b> {timz}
┖ <b>🆔 Version:</b> {version}

<a href="https://t.me/Shizuka_Official"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 @Shizuka_Official</b></a>'''
    RESTARTED = '''<b><i>🤖 Bot Restarted! 🎉</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>🙄 Starting Ping..</i>'
    PING_VALUE = '<b>🏓 Ping</b> <code>{value} ms..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """┎ <b><i>🚧 Task Started</i></b>
┠ <b>💠 Mode:</b> {Mode}
┖ <b>👤 By:</b> {Tag}\n\n"""
    LINKS_SOURCE = """┏ <b>💡 Source:</b>
┖ <b>⏰ Added On:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "🏁 <b><u>Task Started :</u></b>\n┃\n┖ <b>🔗 Link:</b> <a href='{msg_link}'>Click Here</a>"
    L_LOG_START =           "🏁 <b><u>Leech Started :</u></b>\n┃\n┠ <b>👤 User :</b> {mention} ( #ID{uid} )\n┖ <b>💡 Source :</b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '┏<b>🏷️ Name:</b> <code>{Name}</code>\n'
    SIZE =                  '┠ <b>💾 Size: </b>{Size}\n'
    ELAPSE =                '┠ <b>⌛ Elapsed: </b>{Time}\n'
    MODE =                  '┠ <b>💠 Mode: </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '┠ <b>📂 Total Files: </b>{Files}\n'
    L_CORRUPTED_FILES =     '┠ <b>💀 Corrupted Files: </b>{Corrupt}\n'
    L_CC =                  '┖ <b>👤 By: </b>{Tag}\n\n'
    PM_BOT_MSG =            'ℹ️ <b><i>File(s) have been Sent above</i></b>'
    L_BOT_MSG =             'ℹ️ <b><i>File(s) have been Sent to Bot PM (Private)</i></b>'
    L_LL_MSG =              'ℹ️ <b><i>File(s) have been Sent. Access via Links...</i></b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '┠ <b>📜 Type: </b>{Mimetype}\n'
    M_SUBFOLD =             '┠ <b>🗂️ SubFolders: </b>{Folder}\n'
    TOTAL_FILES =           '┠ <b>📂 Files: </b>{Files}\n'
    RCPATH =                '┠ <b>🚩 Path: </b><code>{RCpath}</code>\n'
    M_CC =                  '┖ <b>👤 By: </b>{Tag}\n\n'
    M_BOT_MSG =             '🏁 <b><i>Link(s) have been Sent to Bot PM (Private)</i></b>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cloud Link'
    SAVE_MSG =        '📨 Save Message'
    RCLONE_LINK =     '♻️ RClone Link'
    DDL_LINK =        '📎 {Serv} Link'
    SOURCE_URL =      '🔐 Source Link'
    INDEX_LINK_F =    '🗂 Index Link'
    INDEX_LINK_D =    '⚡ Index Link'
    VIEW_LINK =       '🌐 View Link'
    CHECK_PM =        '📥 View in Bot PM'
    CHECK_LL =        '🖇 View in Links Log'
    MEDIAINFO_LINK =  '📃 MediaInfo'
    SCREENSHOTS =     '🖼 ScreenShots'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '┏ <b>🏷️ Name:</b> <code>{Name}</code>'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n┃ {Bar}'
    PROCESSED =         '\n┠ <b>🔄 Processed:</b> {Processed}'
    STATUS =            '\n┠ <b>✨ Status:</b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' | <b>ETA:</b> {Eta}'
    SPEED =             '\n┠ <b>📶 Speed:</b> {Speed}'
    ELAPSED =                                     ' | <b>Elapsed:</b> {Elapsed}'
    ENGINE =            '\n┠ <b>⚙️ Engine:</b> {Engine}'
    STA_MODE =          '\n┠ <b>💠 Mode:</b> {Mode}'
    SEEDERS =           '\n┠ <b>🌱 Seeders:</b> {Seeders} | '
    LEECHERS =                                           '<b>🪢 Leechers:</b> {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n┠ <b>💾 Size: </b>{Size}'
    SEED_SPEED =     '\n┠ <b>🚀 Speed: </b> {Speed} | '
    UPLOADED =                                     '<b>Uploaded: </b> {Upload}'
    RATIO =          '\n┠ <b>🌀 Ratio: </b> {Ratio} | '
    TIME =                                         '<b>Time: </b> {Time}'
    SEED_ENGINE =    '\n┠ <b>⚙️ Engine:</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n┠ <b>💾 Size: </b>{Size}'
    NON_ENGINE =     '\n┠ <b>⚙️ Engine:</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n┠ <b>👤 User:</b> <code>{User}</code>'
    ID =                '\n┠ <b>🆔 ID:</b> <code>{Id}</code>'
    BTSEL =          '\n┠ <b>✂️ Select:</b> {Btsel}'
    CANCEL =         '\n┖ <b>🚫 Stop:</b> {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '┏ <b><i>🤖 Bot Stats</i></b>\n'
    TASKS =  '┠ <b>🚧 Tasks:</b> {Tasks}\n'
    BOT_TASKS = '┠ <b>🚧 Tasks:</b> {Tasks}/{Ttask} | <b>👷 AVL:</b> {Free}\n'
    Cpu = '┠ <b>🖥️ CPU:</b> {cpu}% | '
    FREE =                      '<b>📭 Free:</b> {free} [{free_p}%]'
    Ram = '\n┠ <b>💿 RAM:</b> {ram}% | '
    uptime =                     '<b>⏰ UPTIME:</b> {uptime}'
    DL = '\n┖ <b>📥 DL:</b> {DL}/s | '
    UL =                        '<b>📤 UL:</b> {UL}/s'

    ###--------BUTTONS-------
    PREVIOUS = '⏪'
    REFRESH = '📑 Page: {Page}'
    NEXT = '⏭️'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = '<b>🏷️ Name:</b> <code>{content}</code>\n<b>⚠️ This File/Folder is already available in Drive!</b>\n\n<b>📑 List Results:</b>'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>🎲 Counting:</b> <code>{LINK}</code>\n\n<b>⏳ Please Wait...</b>'
    COUNT_NAME = '┏ <b>🏷️ Name:</b> <code>{COUNT_NAME}</code>\n'
    COUNT_SIZE = '┠ <b>💾 Size: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '┠ <b>📜 Type: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '┠ <b>🗂️ SubFolders: </b>{COUNT_SUB}\n'
    COUNT_FILE = '┠ <b>📂 Files: </b>{COUNT_FILE}\n'
    COUNT_CC =   '┖ <b>👤 By: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>🔍 Searching for <i>{NAME}</i></b>'
    LIST_FOUND = '<b>ℹ️ Found {NO} result for <i>{NAME}</i></b>'
    LIST_NOT_FOUND = '☹️ No result found for <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<i>No Active Downloads!</i>
    
┏ <b><i>🤖 Bot Stats</i></b>
┠ <b>🖥️ CPU:</b> {cpu}% | <b>📭 Free:</b> {free} [{free_p}%]
┖ <b>💿 RAM:</b> {ram}% | <b>⏰ Uptime:</b> {uptime}
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''㊂ <b><u>User Settings :</u></b>
        
┎<b>👤 Name :</b> {NAME} ( <code>{ID}</code> )
┠<b>🔖 Username :</b> {USERNAME}
┠<b>🆔 Telegram DC :</b> {DC}
┖<b>🗣️ Language :</b> {LANG}

➲ <u><b>Available Args:</b></u>
• <b>-s</b> or <b>-set</b>: Set Directly via Arg

<a href="https://t.me/Shizuka_Official"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 @Shizuka_Official</b></a>'''

    UNIVERSAL = '''㊂ <b><u>Universal Settings : {NAME}</u></b>

┎<b>📺 YT-DLP Options :</b> <b><code>{YT}</code></b>
┠<b>🚧 Daily Tasks :</b> <code>{DT}</code> per day
┠<b>🟢 Last Bot Used :</b> <code>{LAST_USED}</code>
┠<b>📜 User Session :</b> <code>{USESS}</code>
┠<b>📄 MediaInfo Mode :</b> <code>{MEDIAINFO}</code>
┠<b>📩 Save Mode :</b> <code>{SAVE_MODE}</code>
┖<b>🕵️ User Bot PM :</b> <code>{BOT_PM}</code>

<a href="https://t.me/Shizuka_Official"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 @Shizuka_Official</b></a>'''

    MIRROR = '''㊂ <b><u>Mirror/Clone Settings : {NAME}</u></b>

┎<b>🎀 RClone Config :</b> <i>{RCLONE}</i>
┠<b>Ⓟ Mirror Prefix :</b> <code>{MPREFIX}</code>
┠<b>Ⓢ Mirror Suffix :</b> <code>{MSUFFIX}</code>
┠<b>🌈 Mirror Remname :</b> <code>{MREMNAME}</code>
┠<b>🧿 DDL Server(s) :</b> <i>{DDL_SERVER}</i>
┠<b>📮 User TD Mode :</b> <i>{TMODE}</i>
┠<b>📝 Total User TD(s) :</b> <i>{USERTD}</i>
┖<b>☁️ Daily Mirror :</b> <code>{DM}</code> per day

<a href="https://t.me/Shizuka_Official"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 @Shizuka_Official</b></a>'''

    LEECH = '''㊂ <b><u>Leech Settings for {NAME}</u></b>

┎<b>📂 Daily Leech : </b><code>{DL}</code> per day
┠<b>⚙️ Leech Type :</b> <i>{LTYPE}</i>
┠<b>🖼️ Custom Thumbnail :</b> <i>{THUMB}</i>
┠<b>♈ Leech Split Size :</b> <code>{SPLIT_SIZE}</code>
┠<b>♐ Equal Splits :</b> <i>{EQUAL_SPLIT}</i>
┠<b>♒ Media Group :</b> <i>{MEDIA_GROUP}</i>
┠<b>📄 Leech Caption :</b> <code>{LCAPTION}</code>
┠<b>Ⓟ Leech Prefix :</b> <code>{LPREFIX}</code>
┠<b>Ⓢ Leech Suffix :</b> <code>{LSUFFIX}</code>
┠<b>📦 Leech Dumps :</b> <code>{LDUMP}</code>
┖<b>🌈 Leech Remname :</b> <code>{LREMNAME}</code>

<a href="https://t.me/Shizuka_Official"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 @Shizuka_Official</b></a>'''
