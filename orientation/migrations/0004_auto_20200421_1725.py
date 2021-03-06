# Generated by Django 3.0.5 on 2020-04-21 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orientation', '0003_auto_20200421_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmentee',
            name='mentee_name',
        ),
        migrations.RemoveField(
            model_name='projectmentee',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='projectmentor',
            name='mentor_name',
        ),
        migrations.RemoveField(
            model_name='projectmentor',
            name='project_name',
        ),
        migrations.AddField(
            model_name='projectmentee',
            name='mentee_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orientation.User'),
        ),
        migrations.AddField(
            model_name='projectmentee',
            name='project_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orientation.Project'),
        ),
        migrations.AddField(
            model_name='projectmentor',
            name='mentor_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orientation.User'),
        ),
        migrations.AddField(
            model_name='projectmentor',
            name='project_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orientation.Project'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.CreateModel(
            name='MentorMentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentee_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='menteeReverse', to='orientation.User')),
                ('mentor_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mentorReverse', to='orientation.User')),
            ],
        ),
    ]
