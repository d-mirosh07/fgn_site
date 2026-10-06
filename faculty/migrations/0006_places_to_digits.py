from django.db import migrations


def places_to_digits(apps, schema_editor):
    ExchangeProgram = apps.get_model("faculty", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        digits = ""
        for char in program.places:
            if char.isdigit():
                digits = digits + char
        program.places = digits
        program.save()


class Migration(migrations.Migration):

    dependencies = [
        ("faculty", "0005_split_university"),
    ]

    # Відкат не відновлює текст: "2 місця", "до 4", "1 місце" стали просто "2", "4", "1",
    # і з числа вже не можна дізнатися, які слова там були. Саме тому ому reverse_code = noop.
    operations = [
        migrations.RunPython(places_to_digits, reverse_code=migrations.RunPython.noop),
    ]