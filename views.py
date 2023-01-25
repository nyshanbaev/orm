import peewee
from model import Category, Product
def post_category(cat_name):
    try:
        category = Category(name=cat_name)
        category.save()
        print('saved')
    except peewee.IntegrityError:
        print('This category is in the table')

def get_categories():
    categories = Category.select()
    for category in categories:
        print(category.id, category.name, category.created_at)
def delete_category(cat_id):
    try:
        category = Category.get(id=cat_id)
        category.delete_instance()
        print('DELETED')
    except peewee.DoesNotExist:
        print('Not exist')

