# Generated by Django 4.2.1 on 2023-05-08 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_stack_organization_alter_cohort_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainee',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='trainee', to='organization.organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='trainers', to='organization.organization'),
            preserve_default=False,
        ),
    ]