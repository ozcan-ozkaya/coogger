# Generated by Django 2.0 on 2018-07-15 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooggerapp', '0011_auto_20180712_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.CharField(choices=[('science', 'science'), ('tutorial', 'tutorial'), ('idea', 'idea'), ('project', 'project'), ('computer', 'computer'), ('language', 'language'), ('art', 'art'), ('technology', 'technology'), ('biography', 'biography'), ('books', 'books'), ('business', 'business'), ('media', 'media'), ('travel', 'travel'), ('health', 'health'), ('music', 'music'), ('food', 'food'), ('history', 'history'), ('finance', 'finance'), ('exchange', 'exchange'), ('design-graphic', 'design graphic'), ('development', 'development'), ('question-answer', 'question answer'), ('translation', 'translation'), ('discussion', 'discussion'), ('recipe', 'recipe'), ('food-blog', 'food blog'), ('contest-entry', 'contest entry'), ('steemit-iron-chef', 'steemit iron chef'), ('cook-with-us', 'cook with us'), ('food-photography', 'food photography')], help_text='select content category', max_length=30),
        ),
        migrations.AlterField(
            model_name='content',
            name='language',
            field=models.CharField(choices=[('turkish', 'turkish'), ('english', 'english'), ('korean', 'korean'), ('spanish', 'spanish'), ('arabic', 'arabic'), ('french', 'french'), ('portuguese', 'portuguese'), ('german', 'german'), ('italian', 'italian'), ('japanese', 'japanese'), ('romanian', 'romanian'), ('russian', 'russian'), ('vietnamese', 'vietnamese '), ('arabic', 'arabic'), ('azerbaijani', 'azerbaijani')], help_text=' The language of your content', max_length=30),
        ),
    ]