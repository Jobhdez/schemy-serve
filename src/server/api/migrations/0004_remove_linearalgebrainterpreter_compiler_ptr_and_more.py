# Generated by Django 5.0.3 on 2024-03-11 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_user_lalg_compile_exps_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linearalgebrainterpreter',
            name='compiler_ptr',
        ),
        migrations.DeleteModel(
            name='LinearAlgebraCompiler',
        ),
        migrations.DeleteModel(
            name='LinearAlgebraInterpreter',
        ),
    ]
