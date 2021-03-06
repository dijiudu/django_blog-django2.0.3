# Generated by Django 2.0.3 on 2018-04-02 15:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('blog', '0027_auto_20180401_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('success', 'success'), ('info', 'info'), ('warning', 'warning'), ('error', 'error')], default='info', max_length=20)),
                ('unread', models.BooleanField(default=True)),
                ('actor_object_id', models.CharField(max_length=255)),
                ('verb', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('target_object_id', models.CharField(blank=True, max_length=255, null=True)),
                ('action_object_object_id', models.CharField(blank=True, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('public', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('emailed', models.BooleanField(default=False)),
                ('data', jsonfield.fields.JSONField(blank=True, null=True)),
                ('action_object_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_action_object', to='contenttypes.ContentType')),
                ('actor_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notify_actor', to='contenttypes.ContentType')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='blog.User')),
                ('target_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_target', to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
    ]
