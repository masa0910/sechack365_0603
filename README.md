# SecHack365_0603

## 環境
- python 3.7.3
- django 2.2.1  

## 環境構築&実行方法
以下はあくまで参考程度に．  
`python manage.py runserver`を実行した後に*The install worked successfully! Congratulations!* と出れば（たぶん）ここは無視してokです．
#### Pythonのダウンロードからブラウザで確認するまで
1. https://www.anaconda.com/distribution/ からPython3.7をダウンロード
1. `python -V`で*Python 3.7.3*と出ればok
1. `conda install django` でDjangoをインストール
1. `python manage.py runserver`を実行後にURLにアクセス
    - *The install worked successfully! Congratulations!* と出れば成功
    - *ModuleNotFoundError: No module named 'XXXXX'* と出るときは，`conda install XXXXX`

### DBまわり
#### migrateの実行
1. `./SecHack365_0603`に移動
1. `python manage.py migrate`を実行
#### admin関連
1. `python manage.py createsuperuser`を実行して管理者情報の登録
1. `http://localhost:8000/admin/`でログイン

## 参考文献
- Djangoドキュメント ( https://docs.djangoproject.com/ja/2.2/ )
- Python3.7 + DjangoでHello Worldを作ってみた。 ( https://www.indetail.co.jp/blog/190208/ )

## 北海道回までにすること
終わったものは横線で消します．
1. ~~Djangoの環境構築（本田）~~
1. 画面の作成（平川）
    - 登録されてないUSBが接続された時のアラート
    - USB登録画面
1. USBの検知（房安）
1. DBまわり（髙石，本田）
    - 設定
    - DBに保存
    - DBから取得
1. ポスター（全員？）
    - ざっと概要作成（髙石）