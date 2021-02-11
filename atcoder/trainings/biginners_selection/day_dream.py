# NOTE: 困るのは'dreameraser','dreamerase'なので、それぞれ先に消せば良い、反転して愚直に消しても良い
# ref: https://iryond.hatenablog.com/entry/2019/04/13/103733
print("NO" if input().replace("eraser", "").replace(
    "erase", "").replace("dreamer", "").replace("dream", "") else "YES")
