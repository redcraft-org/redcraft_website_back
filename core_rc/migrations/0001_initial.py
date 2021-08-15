# Generated by Django 3.1.7 on 2021-08-15 22:08

import core_rc.models.url.UrlToken
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('code', models.CharField(max_length=16, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_uuid', models.CharField(max_length=255)),
                ('provider_processor', models.CharField(choices=[('mc', 'minecraft'), ('ds', 'discord')], default='mc', max_length=2)),
                ('amount', models.IntegerField(help_text='value in cents')),
                ('donation_at', models.DateTimeField(auto_now_add=True)),
                ('refunded_at', models.DateTimeField(auto_now=True)),
                ('donation_id', models.CharField(max_length=256)),
                ('donation_processor', models.CharField(choices=[('pp', 'paypal')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=64)),
                ('meta', models.JSONField(max_length=64)),
                ('file_processor', models.CharField(choices=[('s3', 's3'), ('f', 'folder')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('short_code', models.CharField(choices=[('BG', 'Bulgarian'), ('CS', 'Czech'), ('DA', 'Danish'), ('DE', 'German'), ('EL', 'Greek'), ('EN', 'English'), ('ES', 'Spanish'), ('ET', 'Estonian'), ('FI', 'Finnish'), ('FR', 'French'), ('HU', 'Hungarian'), ('IT', 'Italian'), ('JA', 'Japanese'), ('LT', 'Lithuanian'), ('LV', 'Latvian'), ('NL', 'Dutch'), ('PL', 'Polish'), ('PT', 'Portuguese'), ('RO', 'Romanian'), ('RU', 'Russian'), ('SK', 'Slovak'), ('SL', 'Slovenian'), ('SV', 'Swedish'), ('ZH', 'Chinese')], max_length=5, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=256)),
                ('language', models.CharField(max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UrlToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default=core_rc.models.url.UrlToken.UrlToken.generate_token_default, max_length=32)),
                ('access_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UrlShortener',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=2048)),
                ('shortened', models.CharField(max_length=32)),
                ('url_token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_rc.urltoken')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('article', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core_rc.article')),
                ('img', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core_rc.file')),
            ],
        ),
        migrations.CreateModel(
            name='LocalizedPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=280)),
                ('slug', models.SlugField(blank=True, max_length=42, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_rc.language')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_rc.post')),
            ],
        ),
        migrations.CreateModel(
            name='LocalizedCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localized_category', to='core_rc.category')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_rc.language')),
            ],
        ),
        migrations.CreateModel(
            name='LocalizedArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=42)),
                ('overview', models.CharField(blank=True, max_length=255, null=True)),
                ('text', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=42, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_rc.article')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_rc.language')),
            ],
        ),
        migrations.CreateModel(
            name='InfoProviderPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_provider', models.CharField(choices=[('mc', 'Minecraft'), ('di', 'Discord')], max_length=256)),
                ('uuid_minecraft', models.CharField(max_length=256)),
                ('last_name_provider', models.CharField(max_length=256)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='core_rc.player')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_rc.category'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rank', models.CharField(max_length=32)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name='localizedpost',
            constraint=models.UniqueConstraint(fields=('post', 'language'), name='localized_post_unique'),
        ),
        migrations.AddConstraint(
            model_name='localizedcategory',
            constraint=models.UniqueConstraint(fields=('language', 'category'), name='localized_category_unique'),
        ),
        migrations.AddConstraint(
            model_name='localizedarticle',
            constraint=models.UniqueConstraint(fields=('language', 'article'), name='localized_article_unique'),
        ),
    ]
