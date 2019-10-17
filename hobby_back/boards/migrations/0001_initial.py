# Generated by Django 2.2.6 on 2019-10-15 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardName', models.CharField(max_length=50)),
                ('boardNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectionName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PostHobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('contents', models.TextField()),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('totalMember', models.IntegerField()),
                ('nowMember', models.IntegerField()),
                ('location', models.CharField(max_length=300)),
                ('fee', models.IntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Group')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
        migrations.CreateModel(
            name='PostFree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('contents', models.TextField()),
                ('createDate', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Group')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=20)),
                ('contents', models.TextField()),
                ('createDate', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Post')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Section'),
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=20)),
                ('contents', models.TextField()),
                ('createDate', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Post')),
            ],
        ),
        migrations.CreateModel(
            name='CommentHobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('postHobby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.PostHobby')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
        migrations.CreateModel(
            name='CommentFree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('postFree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.PostFree')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
    ]
