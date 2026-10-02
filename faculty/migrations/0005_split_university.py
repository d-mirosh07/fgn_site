from django.db import migrations


def split_university(apps, schema_editor):
    ExchangeProgram = apps.get_model("faculty", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        text = program.university
        if "(" in text:
            name, country = text.split("(")
            country = country.replace(")", "")
        elif " - " in text:
            name, country = text.split(" - ")
        else:
            name, country = text.split(", ")
        program.university = name.strip()
        program.country = country.strip()
        program.save()


def join_university(apps, schema_editor):
    ExchangeProgram = apps.get_model("faculty", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        program.university = program.university + ", " + program.country
        program.save()


class Migration(migrations.Migration):

    dependencies = [
        ("faculty", "0004_exchangeprogram_country"),
    ]
    # Відкат не відновлює текст: "2 місця", "до 4", "1 місце" стали просто "2", "4", "1",
    # і з числа вже не можна дізнатися, які слова там були. Саме тому ому reverse_code = noop.
    operations = [
        migrations.RunPython(split_university, reverse_code=join_university),
    ]
