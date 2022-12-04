from django.db.models import Model

def query_all_db(model: Model) -> Model:
    return model.objects.all()


def query_one_db(model: Model, *args, **kwargs) -> Model:
    return model.objects.get(*args, **kwargs)


def filter_query_db(model: Model, *args, **kwargs) -> Model:
    return model.objects.filter(*args, **kwargs)
