import requests
import re
import json
from user_agent import *
import uuid
import random
import string
import time
import uuid
import random
import base64
import os






user_agent_generate = str(generate_user_agent())
session = requests.Session()





###############################################################33
def generate_random_user_agent():
    devices = [
        ("Samsung", "SM-A515F", "qcom"),
        ("Xiaomi", "Redmi 8A", "olivelite"),
        ("Huawei", "P30 Lite", "kirin"),
        ("OnePlus", "ONEPLUS A6010", "sdm845"),
        ("Google", "Pixel 3a", "bonito"),
    ]
    android_versions = [
        (30, "11"),
        (29, "10"),
        (28, "9"),
    ]
    dpi = random.choice(["320", "480", "640"])
    resolution = random.choice(["720x1360", "1080x1920", "1080x2340"])

    device_brand, model, chip = random.choice(devices)
    sdk, android_version = random.choice(android_versions)
    lang = random.choice(["en_US", "fr_FR", "es_ES"])

    user_agent = (
        f"Instagram 275.0.0.27.98 Android ({sdk}/{android_version}; {dpi}dpi; {resolution}; "
        f"{device_brand}; {model}; {chip}; {chip}; {lang}; {random.randint(100000000, 999999999)})"
    )
    return user_agent

def generate_mid():
    random_bytes = os.urandom(9)  # 9 bytes = ~12 chars base64
    b64_mid = base64.urlsafe_b64encode(random_bytes).decode().rstrip("=")
    prefix = random.choice(['a', 'b', 'c', 'd'])
    return f"{prefix.upper()}{b64_mid}"

def generate_pigeon_session_id():
    unique_id = str(uuid.uuid4())
    return f"UFS-{unique_id}-0"


def generate_instagram_headers():
    timestamp = str(time.time())
    device_id = str(uuid.uuid4())
    android_id = f"android-{uuid.uuid4().hex[:16]}"
    family_device_id = str(uuid.uuid4())
    bandwidth_speed = str(random.randint(1000, 4000)) + ".000"
    nav_chain = (
        f"MainFeedFragment:feed_timeline:2:main_home:{timestamp}::,"
        f"DirectInboxFragment:direct_inbox:3:on_launch_direct_inbox:{timestamp}::,"
        f"DirectThreadFragment:direct_thread:5:button:{timestamp}::"
    )
    connection_type = random.choice(["WIFI", "MOBILE(LTE)", "CELL"])
    lang = random.choice(["en_US", "fr_FR", "es_ES"])
    headers = {
        'User-Agent': generate_random_user_agent(), #'Instagram 275.0.0.27.98 Android (29/10; 320dpi; 720x1369; Xiaomi; Redmi 8A; olivelite; qcom; en_US; 458229237)',
        # 'Accept-Encoding': 'zstd, gzip, deflate',
        'x-ig-app-locale': 'en_US',
        'x-ig-device-locale': 'en_US',
        'x-ig-mapped-locale': 'en_US',
        'x-pigeon-session-id': generate_pigeon_session_id(),
        'x-pigeon-rawclienttime': timestamp,
        'x-ig-bandwidth-speed-kbps': bandwidth_speed,
        'x-ig-bandwidth-totalbytes-b': '56818',
        'x-ig-bandwidth-totaltime-ms': '61',
        'x-bloks-version-id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb',
        'x-ig-www-claim': '0',
        'x-bloks-is-layout-rtl': 'false',
        'x-ig-device-id': device_id,
        'x-ig-family-device-id': family_device_id,
        'x-ig-android-id': android_id,
        'x-ig-timezone-offset': '3600',
        'x-fb-connection-type': connection_type,
        'x-ig-connection-type': connection_type,
        'x-ig-capabilities': '3brTv10=',
        'x-ig-app-id': '567067343352427',
        'priority': 'u=3',
        'accept-language': 'en-US',
        'x-mid': generate_mid(),
        'ig-intended-user-id': '0',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-fb-http-engine': 'Liger',
        'x-fb-client-ip': 'True',
        'x-fb-server-cluster': 'True',
    }
    return headers




sessionAPP = requests.Session()
headersAPP = generate_instagram_headers()



#--------------------Login---------------#

login = input(" [/] Entre username : ")
passwd = input(" [/] Entre password : ")



waterfall_id = str(uuid.uuid4())
dataAPP = {
    'params': '{"client_input_params":{"sim_phones":[],"aymh_accounts":[],"secure_family_device_id":"","has_granted_read_contacts_permissions":0,"auth_secure_device_id":"","has_whatsapp_installed":1,"password":"#PWD_INSTAGRAM:0:0:' + str(passwd) + '","sso_token_map_json_string":"{}","block_store_machine_id":"","cloud_trust_token":null,"event_flow":"login_manual","password_contains_non_ascii":"false","client_known_key_hash":"","encrypted_msisdn":"","has_granted_read_phone_permissions":0,"app_manager_id":"","should_show_nested_nta_from_aymh":1,"device_id":"' + str(headersAPP["x-ig-android-id"]) + '","login_attempt_count":1,"machine_id":"' + str(headersAPP["x-mid"]) + '","accounts_list":[],"family_device_id":"' + str(headersAPP["x-ig-family-device-id"]) + '","fb_ig_device_id":[],"device_emails":[],"try_num":1,"lois_settings":{"lois_token":""},"event_step":"home_page","headers_infra_flow_id":"","openid_tokens":{},"contact_point":"' + str(login) + '"},"server_params":{"should_trigger_override_login_2fa_action":0,"is_vanilla_password_page_empty_password":0,"is_from_logged_out":0,"should_trigger_override_login_success_action":0,"login_credential_type":"none","server_login_source":"login","waterfall_id":"' + str(waterfall_id) + '","two_step_login_type":"one_step_login","login_source":"Login","is_platform_login":0,"INTERNAL__latency_qpl_marker_id":36707139,"is_from_aymh":0,"offline_experiment_group":"caa_launch_ig4a_combined_60_percent","is_from_landing_page":0,"password_text_input_id":"exqf6y:68","is_from_empty_password":0,"is_from_msplit_fallback":0,"ar_event_source":"login_home_page","qe_device_id":"' + str(headersAPP["x-ig-device-id"]) + '","username_text_input_id":"exqf6y:67","layered_homepage_experiment_group":null,"device_id":"' + str(headersAPP["x-ig-android-id"]) + '","INTERNAL__latency_qpl_instance_id":9.0318653800205E13,"reg_flow_source":"aymh_multi_profiles_native_integration_point","is_caa_perf_enabled":1,"credential_type":"password","is_from_password_entry_page":0,"caller":"gslr","family_device_id":"' + str(headersAPP["x-ig-family-device-id"]) + '","is_from_assistive_id":0,"access_flow_version":"pre_mt_behavior","is_from_logged_in_switcher":0}}',
    'bk_client_context': '{"bloks_version":"8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb","styles_id":"instagram"}',
    'bloks_versioning_id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb',
}

responseAPP = sessionAPP.post(
    'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',
    headers=headersAPP,
    data=dataAPP,
).text
#print(responseAPP)
if '"login_success' in responseAPP:
    print(" [*] LOGIN SUCCESS")
else:
    print(" [-] LOGIN FAILED")
    exit()


#--------GET DATA----------#
f = str(responseAPP).replace('\\', '')
auth = re.search(r'Bearer\s+(IGT:[\w\-\.=:+]+)', f)
authorization = auth.group(1)


pas = input(" [+] Entre new password : ")



headers = {
    'User-Agent': 'Instagram 275.0.0.27.98 Android (29/10; 320dpi; 720x1369; Xiaomi; Redmi 8A; olivelite; qcom; en_GB; 458229237)',
    # 'Accept-Encoding': 'zstd, gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded; application/x-www-form-urlencoded; charset=UTF-8',
    'x-ig-app-locale': 'en_GB',
    'x-ig-device-locale': 'en_GB',
    'x-ig-mapped-locale': 'en_GB',
    'x-pigeon-session-id': 'UFS-516ac80c-9003-44f0-b89b-c0fcda64d0e7-0',
    'x-pigeon-rawclienttime': '1756123830.519',
    'x-ig-bandwidth-speed-kbps': '950.000',
    'x-ig-bandwidth-totalbytes-b': '0',
    'x-ig-bandwidth-totaltime-ms': '0',
    'x-bloks-version-id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb',
    'x-ig-www-claim': 'hmac.AR3q_SGNWa4jZnBjkGgOiClXZ1jT3HDId-M4rFfWEZcHKZWJ',
    'x-bloks-is-layout-rtl': 'false',
    'x-ig-device-id': '5d03d549-1663-422e-97d7-1387bd404eee',
    'x-ig-family-device-id': 'e6551fa4-a560-43a7-a18e-8c106a320b9e',
    'x-ig-android-id': 'android-f346cbf59363asde',
    'x-ig-timezone-offset': '3600',
    'x-ig-nav-chain': 'SelfFragment:self_profile:2:main_profile:1756123781.853::,ProfileMenuFragment:bottom_sheet_profile:3:button:1756123782.698::,UserOptionsFragment:settings_category_options:4:button:1756123784.851::,SecurityOptionsFragment:security_options:5:button:1756123787.292::,ChangePasswordV2Fragment:change_password:6:button:1756123789.180::',
    'x-fb-connection-type': 'WIFI',
    'x-ig-connection-type': 'WIFI',
    'x-ig-capabilities': '3brTv10=',
    'x-ig-app-id': '567067343352427',
    'priority': 'u=3',
    'accept-language': 'en-GB, en-US',
    'authorization': authorization,
    'x-mid': 'aKuergABAAHUoiCnhz6BG3e3Dhfw',
    'ig-u-ds-user-id': '76494080625',
    'ig-u-rur': 'RVA,76494080625,1787659789:01fe2e896d9bc52f20775d62983a567e718a89e288bc617d2a266eb13b56c321e5753bf7',
    'ig-intended-user-id': '76494080625',
    'x-fb-http-engine': 'Liger',
    'x-fb-client-ip': 'True',
    'x-fb-server-cluster': 'True',
}

data = {
    'signed_body': 'SIGNATURE.{"_uid":"76494080625","_uuid":"5d03d549-1663-422e-97d7-1387bd404eee","enc_old_password":"#PWD_INSTAGRAM:0:1756123830:'+(passwd)+'","enc_new_password1":"#PWD_INSTAGRAM:0:1756123830:'+(pas)+'","enc_new_password2":"#PWD_INSTAGRAM:0:1756123830:'+(pas)+'"}',
}
response = requests.post('https://i.instagram.com/api/v1/accounts/change_password/', headers=headers, data=data)
print(response.text)
