# Generated by Django 4.0.5 on 2022-06-06 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_remove_comment_article_remove_comment_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='articles.post'),
            preserve_default=False,
        ),
    ]
