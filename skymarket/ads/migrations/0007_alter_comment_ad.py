# Generated by Django 4.1.1 on 2022-09-29 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0006_alter_comment_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="ad",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ads.ad"
            ),
        ),
    ]