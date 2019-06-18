# SecHack365_0603
## 環境
- python 3.7.3
- django 2.2.1  
## 環境構築&実行方法
以下はあくまで参考程度に．  
`python manage.py runserver`を実行した後に*The install worked successfully! Congratulations!* と出れば（たぶん）ここは無視してokです．
1. https://www.anaconda.com/distribution/ からPython3.7をダウンロード
1. `python -V`で*Python 3.7.3*と出ればok
1. `conda install django` でDjangoをインストール
1. `python manage.py runserver`を実行後にURLにアクセス
    - *The install worked successfully! Congratulations!* と出れば成功
    - *ModuleNotFoundError: No module named 'XXXXX'* と出るときは，`conda install XXXXX`
## 北海道回までにすること
終わったものは横線で消します．
1. ~~Djangoの環境構築（本田）~~
1. 画面の作成（平川）
    - 登録されてないUSBが接続された時のアラート
    - USB登録画面
1. USBの検知（房安）
1. DBまわり（髙石）
    - 設定
    - DBに保存
    - DBから取得
1. ポスター（全員？）
    - ざっと概要作成（髙石）
