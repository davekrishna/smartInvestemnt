# Generated by Django 2.2.6 on 2020-10-11 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=500)),
                ('thumbnail', models.FileField(null=True, upload_to='BlogPost/')),
                ('Content', models.TextField()),
                ('publishdate', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentByName', models.CharField(max_length=20)),
                ('commentByEmail', models.EmailField(max_length=254)),
                ('comment', models.TextField(max_length=150)),
                ('TimeOfComment', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('ForblogPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogPostModule.blogPosts')),
            ],
        ),
        migrations.CreateModel(
            name='Replys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReplyByName', models.CharField(max_length=20)),
                ('ReplyByEmail', models.EmailField(max_length=254)),
                ('reply', models.TextField(max_length=150)),
                ('TimeOfReply', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('ForComment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogPostModule.Comments')),
                ('ForblogPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogPostModule.blogPosts')),
            ],
        ),
    ]
