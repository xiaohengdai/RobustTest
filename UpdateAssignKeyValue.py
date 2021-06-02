import json
import os

def check_json_value(dic_json, k, v):
    if isinstance(dic_json, dict):
        for key in dic_json:
            if key == k:
                dic_json[key] = v
            elif isinstance(dic_json[key], dict):
                check_json_value(dic_json[key], k, v)
            elif isinstance(dic_json[key],list):
                for i in range(0,len(dic_json[key])):
                    check_json_value(dic_json[key][i],k,v)


# flow = "{'id': 'af8b7545-f76f-4e4c-be18-d93afdec9f40', 'size': 14453}"
# flow='{"result":1,"hostName":"zt-sc-rs99.idcyz.hb1.kwaidc.com","cache-scope":"nocache","error_msg":null,"sharePanel":{"kpn":"KUAISHOU","subBiz":"PROFILE","shareObjectId":"2305071308","shareResourceType":"","extParams":{"ext":"profile_new online","serverSdkVersion":"1.0","lowLevelPanelConfig":true},"ztShareSDKExtParams":"{\"sharePanelId\":\"117913274073\"}","bundle":[{"area":[{"id":"IM","elementType":"placeholder","camelName":"im","displayName":"私信好友","iconUrl":null,"actionUrl":"kwaishare://shareAny/im","autoAdjustFontSize":false,"autoHidePanelWhenClicked":true}],"title":""},{"area":[{"id":"WECHAT","elementType":"button","camelName":"wechat","displayName":"微信好友","iconUrl":"https://static.yximgs.com/kos/nlav10348/icon/icon_share_panel_wechat_session.webp","actionUrl":"kwaishare://shareAny/wechat","autoAdjustFontSize":false,"autoHidePanelWhenClicked":true},{"id":"WECHAT_MOMENTS","elementType":"button","camelName":"wechatMoments","displayName":"微信朋友圈","iconUrl":"https://static.yximgs.com/kos/nlav10348/icon/icon_share_panel_wechat_timeline.webp","actionUrl":"kwaishare://shareAny/wechatMoments","autoAdjustFontSize":false,"autoHidePanelWhenClicked":true},{"id":"QQ","elementType":"button","camelName":"qq","displayName":"QQ好友","iconUrl":"https://static.yximgs.com/kos/nlav10348/icon/icon_share_panel_qq.webp","actionUrl":"kwaishare://shareAny/qq","autoAdjustFontSize":false,"autoHidePanelWhenClicked":true},{"id":"QZONE","elementType":"button","camelName":"qzone","displayName":"QQ空间","iconUrl":"https://static.yximgs.com/kos/nlav10348/icon/icon_share_panel_qzone.webp","actionUrl":"kwaishare://shareAny/qzone","autoAdjustFontSize":false,"autoHidePanelWhenClicked":true},{"id":"WEIBO","elementType":"button","camelName":"weibo","displayName":"新浪微博","iconUrl":"https://static.yximgs.com/kos/nlav10348/icon/icon_share_panel_weibo.webp","actionUrl":"kwaishare://shareAny/weibo","autoAdjustFontSize":false,"autoHidePanelWhenClicked":true}]},{"area":[{"id":"COPY_LINK","elementType":"button","camelName":"copyLink","displayName":"复制链接","iconUrl":"https://static.yximgs.com/kos/nlav10348/icon/share_panel_icon_copy_link_light.webp","actionUrl":"kwaishare://shareAny/copyLink","autoAdjustFontSize":false,"autoHidePanelWhenClicked":true},{"id":"FACE_TO_FACE_QRCODE","elementType":"button","camelName":"faceToFaceQrcode","displayName":"生成海报","iconUrl":"https://static.yximgs.com/kos/nlav10348/icon/share_panel_icon_scan_code_share_light.webp","actionUrl":"kwaishare://faceToFaceQRCode","autoAdjustFontSize":false,"autoHidePanelWhenClicked":true}]}],"theme":{"area":{"fontSize":15,"fontColor":"#222222"},"element":{"fontSize":11,"fontColor":"#666666","minFontSize":7},"cancelButton":{"fontSize":17,"fontColor":"#222222","backgroundColor":"#FFFFFF","highlightedBackgroundColor":"#F8F8F8","cornerRadius":12},"panel":{"backgroundColor":"#FFFFFF","separatorColor":"#EAEAEA","cornerRadius":12}},"blackList":{"area":[],"title":""},"title":"分享至"},"panelPoster":{},"max-age":0}'
with open(os.path.join(os.getcwd(),"data.json")) as file:
    date_json = json.load(file)
# print("date_json 变更前   :")
# print(date_json)
check_json_value(date_json, 'id', '13333333333')
print("date_json 变更后   :")
print(date_json)
