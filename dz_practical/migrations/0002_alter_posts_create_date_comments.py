from django.db import migrations, models
import django.db.models.deletion
import django_lifecycle.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('dz_practical', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='create_date',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('text', models.TextField()),
                ('published_date', models.DateTimeField()),
                ('is_publish', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dz_practical.posts')),
            ],
            options={
                'abstract': False,
            },
            bases=(django_lifecycle.mixins.LifecycleModelMixin, models.Model),
        ),
    ]
