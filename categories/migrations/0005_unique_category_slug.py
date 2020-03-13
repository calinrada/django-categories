# Generated by Django 2.0.9 on 2018-10-05 13:59

from django.db import migrations, models


def make_slugs_unique(apps, schema_editor):
    Category = apps.get_model('categories', 'Category')
    duplicates = Category.tree.values('slug').annotate(slug_count=models.Count('slug')).filter(slug_count__gt=1)
    for duplicate in duplicates:
        slug = duplicate['slug']
        categories = Category.tree.filter(slug=slug)
        count = categories.count()
        i = 0
        for category in categories.all():
            if i != 0:
                category.slug = "%s_%s" % (slug, str(i).zfill(len(str(count))))
                category.save()
            i += 1


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20200517_1832'),
    ]

    operations = [
        migrations.RunPython(make_slugs_unique, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug'),
        ),
    ]
