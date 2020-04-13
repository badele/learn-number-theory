from manimlib.imports import *
import numpy as np

import json
import numbers
import sys


def is_prime(n):
    if n < 2:
        return False
    for k in range(2, int(np.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


def get_divisors(n):
    assert(n >= 0)

    if n == 0:
        return []

    if n == 1:
        return [1]

    divisors = [1]
    for k in range(2, n):
        if n % k == 0:
            divisors.append(k)

    divisors.append(n)
    return divisors


class SearchPrimes(Scene):
    CONFIG = {
        "maxn": 40,
    }

    def construct(self):
        self.title()
        self.a_prime()
        self.search_by_divisors()

    def title(self):
        titre = TextMobject("Les nombres premiers")
        partie = TextMobject("Partie 1")
        partie.next_to(titre, DOWN)

        chapitre = TextMobject("Trouver les nombres premiers")

        # Affiche le titre
        self.play(Write(titre), Write(partie))
        self.wait(1)

        # Anime le sous titre
        self.play(
            FadeOut(partie),
            ReplacementTransform(titre, chapitre))
        self.play(
            ApplyMethod(chapitre.shift, 3 * UP),
        )

        # Souligne le titre
        underline = Line().match_width(chapitre)
        underline.next_to(chapitre, DOWN)
        self.play(
            GrowFromCenter(underline)
        )
        self.wait(1)

    def a_prime(self):

        title = TextMobject("Un nombre", "est dit premier,", "si il admet seulement", "deux diviseurs\\\\",
                            "C'est \\`a dire", "un et lui m\\^eme\\\\"
                            )

        # Colorize le titre
        title.set_width(FRAME_WIDTH - 1)
        title.get_part_by_tex("est dit premier").set_color(TEAL)
        title.get_part_by_tex("deux diviseurs").set_color(TEAL)
        title.get_part_by_tex("un et lui m\\^eme").set_color(TEAL)
        title.set_stroke(BLACK, 5, background=True)

        # Fondu block à block
        for word in title:
            self.play(
                FadeIn(
                    word, run_time=0.05 * len(word),
                    lag_ratio=0.4,
                )
            )
        self.wait()

        # Efface l'intro
        self.play(FadeOut(title))

    def search_by_divisors(self):

        # Configure la grille des nombres
        number_grid = VGroup(*[
            VGroup(*[
                Integer(n) for n in range(10 * k + 1, 10 * k + 11)
            ]).arrange(DOWN)
            for k in range(0, int(self.maxn / 10))
        ]).arrange(RIGHT, buff=1)

        numbers = VGroup(*it.chain(*number_grid))
        numbers.set_height(5)
        numbers.move_to(4 * LEFT)
        numbers.to_edge(DOWN)

        # Prepare le titre
        divisons = TextMobject(
            "Nous allons chercher", "les diviseurs\\\\", "pour chaque nombre",
            alignment=""
        )
        divisons.scale(0.8)
        divisons.next_to(ORIGIN, RIGHT)

        divisor = divisons.get_part_by_tex("diviseurs")
        divisor.set_color(TEAL)

        # Affiche les nombres
        self.play(
            ShowIncreasingSubsets(numbers, run_time=3),
            FadeInFrom(divisons, LEFT)
        )

        # Initiale le texte du compteur
        search_for = TextMobject(
            "Nous allons chercher", "les diviseurs\\\\", "pour le nombre", "1",
            alignment=""
        )
        search_for.scale(0.8)
        search_for.next_to(ORIGIN, RIGHT)

        search_for.get_part_by_tex("diviseurs").set_color(TEAL)
        search_for.get_part_by_tex("1").set_color(YELLOW)

        self.play(
            ReplacementTransform(divisons[2], search_for[2:4]),
        )
        self.remove(*search_for)

        # Recherche des nombres premiers
        run_time = 0.4
        number_noprimes = []
        prime_rects = []
        for n in range(1, numbers[-1].get_value() + 1):
            if n > 7:
                run_time = 0.2

            self.remove(search_for)
            number = str(n)
            search_for = TextMobject(
                "Nous allons chercher", "les diviseurs\\\\", "pour le nombre", number,
                alignment=""
            )
            search_for.scale(0.8)
            search_for.next_to(ORIGIN, RIGHT)

            search_for.get_part_by_tex("diviseurs").set_color(TEAL)
            search_for.get_part_by_tex(number).set_color(YELLOW)

            divisors = get_divisors(n)
            tdivisors = TextMobject(str(divisors))
            tdivisors.next_to(search_for, DOWN)

            if len(divisors) == 2:
                isprime = TextMobject("est premier", color=GREEN)
            else:
                isprime = TextMobject("non premier", color=RED)
                number_noprimes.append(n)

            isprime.next_to(tdivisors, DOWN)

            selected_rect = SurroundingRectangle(numbers[n - 1], color=GRAY)
            self.add(search_for)

            # Affiche le rectangle en cours de recherche
            self.play(
                ShowCreation(selected_rect),
                Write(tdivisors),
                Write(isprime),
                run_time=run_time
            )

            # Entoure en vert le nombre premier trouvé
            if len(divisors) == 2:
                rect = SurroundingRectangle(numbers[n - 1], color=GREEN)
                prime_rects.append(rect)
                self.play(
                    ShowCreation(rect),
                    run_time=run_time
                )

            self.wait(0.3)
            self.remove(tdivisors, isprime, selected_rect)

        # Grise tous les nombres qui ne sont pas premier
        # Laisse apparaitre les nombres premiers
        noprimes_vg_rect = VGroup(
            *[SurroundingRectangle(numbers[np - 1], color=GRAY) for np in number_noprimes]
        )

        primes_vg_rect = VGroup(*prime_rects)

        primes_result = TextMobject(
            "Liste des nombres premiers", "apr\\`es recherche\\\\", "par diviseurs",
            alignment=""
        )
        primes_result.scale(0.8)
        primes_result.next_to(ORIGIN, RIGHT)

        primes_result.get_part_by_tex("par diviseurs").set_color(TEAL)

        self.play(LaggedStartMap(ShowCreation, noprimes_vg_rect, run_time=1))
        self.play(
            LaggedStart(*[
                ApplyMethod(numbers[np - 1].set_opacity, 0.2)
                for np in number_noprimes
            ]),
            LaggedStartMap(FadeOut, noprimes_vg_rect),
            FadeOut(divisons),
            FadeOut(search_for, tdivisors),
            FadeIn(primes_result),
            LaggedStartMap(FadeOut, primes_vg_rect),
            run_time=1
        )
        self.wait(5)
