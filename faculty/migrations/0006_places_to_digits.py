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
    # Відкат не відновлює формат: "KU Leuven (Бельгія)" і "University of Tartu - Естонія" стануть
    # "KU Leuven, Бельгія" і "University of Tartu, Естонія",
    # бо вже не можна дізнатися, де були дужки чи тире.
    operations = [
        migrations.RunPython(places_to_digits, reverse_code=migrations.RunPython.noop),
    ]