# tweet_to_discord
特定の１つのTwitterアカウントのTweetを取得し、Webhookを通じてDiscordに投稿する簡易スクリプト。

## 設定方法

* target_name

    target_nameにTweetを取得したいTwitterアカウントのスクリーンネームを記述

* reply_flag

    Discordに投稿する際に他のアカウントへのreplyを除きたい場合は値を0に、他のアカウントへのreplyを含めたい場合は値を1に設定

* retweet_flag

    Discordに投稿する際にretweetを除きたい場合は値を0に、replyを含めたい場合は値を1に設定

* favorite_count_threshold

    ここで設定した数以上にlikeがついたときのみDiscordに投稿

* retweet_count_threshold

    ここで設定した数以上にretweetされたときのみDiscordに投稿

* query

    取得したTweetのうち、ここに指定した文字列を含むものだけをDiscordに投稿
    （デフォルトのように何も指定しなければではすべてのTweetをDiscordに投稿）

* collect_interval
    
    最後にDiscordに投稿してから次のTweetを取得するまでに停止する時間（単位は秒）

* stop_tweet

    ここに記載した文字列をtargetのTwitterアカウントが投稿すると、このスクリプトが停止

## 動かし方
Pythonのプログラムを走らせることのできるディレクトリで実行。

スクリプトの作成時のPythonのバージョンは3.6.5。

モジュールとして[discord_hook.py](https://github.com/4rqm/dhooks)をお借りしており、このファイルも同じディレクトリに配置。


## Dependency
以下の２つのモジュールが必要。
* tweepy (スクリプトの作成時はversion 3.5.0を使用)
* [discord_hook.py](https://github.com/4rqm/dhooks)

事前にTwitter APIのキーの取得が必要。

事前にDiscordでWebhookを作成し、URLを取得しておくことが必要。