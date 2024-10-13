# Generated by Django 5.1.2 on 2024-10-13 15:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament_name', models.CharField(max_length=100)),
                ('match_date', models.DateField()),
                ('match_type', models.CharField(choices=[('Singles', 'Singles'), ('Doubles', 'Doubles')], max_length=10)),
                ('result', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='MatchPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=20)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.player')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=50)),
                ('event_time', models.DateTimeField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.match')),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='matches.player')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='videos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.match')),
            ],
        ),
        migrations.CreateModel(
            name='VideoSegment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.PositiveIntegerField()),
                ('end_time', models.PositiveIntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.event')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.video')),
            ],
        ),
    ]