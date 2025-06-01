from django.db import migrations

def fix_mysql_auth_plugin(apps, schema_editor):
    with schema_editor.connection.cursor() as cursor:
        cursor.execute("""
            ALTER USER 'your_db_user'@'%' IDENTIFIED WITH mysql_native_password BY 'your_db_password';
            FLUSH PRIVILEGES;
        """)

class Migration(migrations.Migration):
    dependencies = [
        ('your_app_name', '0001_initial'),  # update to your last migration
    ]

    operations = [
        migrations.RunPython(fix_mysql_auth_plugin),
    ]
