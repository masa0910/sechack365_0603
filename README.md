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
