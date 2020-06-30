import emoji

'''
https://www.unicode.org/emoji/charts/full-emoji-list.html#1f618
function:
    demojize: 将unicode emoji替换为字符串简码用于存储
    emoji_count: 返回字符串中emoji的数量
    emoji_lis: 返回字符串中emoji的位置
    emojize: 将字符串简码替换成unicode emoji
    get_emoji_regexp: 返回编译后的正则表达式，匹配`emoji.UNICODE_EMOJI_ALIAS`

'''

# for k, v in emoji.EMOJI_UNICODE.items():
#     print(v, end=' ')

print(emoji.emojize(':slightly_smiling_face:'))
print(emoji.demojize('🤣'))