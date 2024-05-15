class DbRouter(object):
    """
    複数のDBをルーティングさせるためのクラス
    ・read/write
    アプリごとに1つのDBを使用を想定
    →「アプリ名=その中のDB」とする
    ただし、app内にないアプリケーション(admin等)はmainのアプリケーションのDBへと行くようにする

    リレーション：あり
    マイグレーション
    対応するアプリ内DBに対して実行させるようにする
    ただしadmin等はmain内DB
    """

    app = {"main", "note", "macro"}


def db_for_read(self, model, **hints):
    if model._meta.app_label in self.app:
        return model._meta.app.label
    return "main"


def db_for_write(self, model, **hints):
    if model._meta.app_label in self.app:
        return model._meta.app_label


def allow_relation(self, obj1, obj2, **hints):
    return True


def allow_migration(self, db, app_label, model_name=None, **hints):
    if app_label in self.app:
        return db == app_label
    return db == "main"
