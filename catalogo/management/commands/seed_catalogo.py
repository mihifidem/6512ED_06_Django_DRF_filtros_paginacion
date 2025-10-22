from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import datetime, timedelta
from catalogo.models import Book

class Command(BaseCommand):
    help = "Crea datos de ejemplo (Books) para pruebas."

    def add_arguments(self, parser):
        parser.add_argument(
            "--cantidad",
            type=int,
            default=200,
            help="Cantidad de libros a generar (por defecto 200)."
        )

    def handle(self, *args, **options):
        fake = Faker("es_ES")
        cantidad = options["cantidad"]

        generos = ["Fantasía", "Ciencia Ficción", "Romance", "Terror", "No Ficción", "Programación", "Historia", "Misterio"]

        created = 0
        for _ in range(cantidad):
            dias = random.randint(0, 3650)  # últimos ~10 años
            fecha = datetime.today().date() - timedelta(days=dias)

            Book.objects.create(
                titulo = fake.sentence(nb_words=4),
                autor = fake.name(),
                genero = random.choice(generos),
                precio = round(random.uniform(5, 120), 2),
                publicado = fecha,
                stock = random.randint(0, 200),
                rating = round(random.uniform(1, 5), 1),
            )
            created += 1

        self.stdout.write(self.style.SUCCESS(f"Se crearon {created} libros de ejemplo."))
