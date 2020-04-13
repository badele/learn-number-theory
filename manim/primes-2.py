from manimlib.imports import *


class SearchPrimes(Scene):
    CONFIG = {
        "maxn": 140,
        "palette": [
            "#D04A03",
            "#A8BD22",
            "#0377A8",
            "#6C088F",
            "#CB9904",
            "#CD200F",
            "#CDD02B",
            "#330188",
            "#013ACF",
            "#0377A8",
            "#CD7D02",
        ],
    }

    def construct(self):
        self.title()
        self.a_prime()
        self.search_by_eratosthene()

    def title(self):
        titre = TextMobject("Les nombres premiers")
        partie = TextMobject("Partie 2")
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

        # Colorize le titre
        title = TextMobject(
            "Trouver des nombres premiers par", "la recherche des diviseurs",
            "n'est pas la m\\'ethode", "la plus rapide",
        )
        title.set_width(FRAME_WIDTH - 1)
        title.get_part_by_tex("la recherche des diviseurs").set_color(TEAL)
        title.get_part_by_tex("la plus rapide").set_color(TEAL)
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

    def search_by_eratosthene(self):

        # Configure la grille des nombres
        number_grid = VGroup(*[
            VGroup(*[
                Integer(n) for n in range(10 * k + 1, 10 * k + 11)
            ]).arrange(DOWN)
            for k in range(0, int(self.maxn / 10))
        ]).arrange(RIGHT, buff=1)

        numbers = VGroup(*it.chain(*number_grid))
        numbers.set_height(3.5)
        # numbers.move_to(CENTER)
        numbers.to_edge(TOP)
        maxnumber = numbers[-1].get_value()

        # Cache le chiffre 1, il n'est pas premier
        numbers[0].set_opacity(0)

        # Prepare le titre
        cherchons = TextMobject(
            "Nous allons chercher", "les nombres premiers\\\\", "via le", "crible d'\\'Eratosth\\`ene",
        )
        cherchons.scale(0.8)
        cherchons.next_to(ORIGIN, 10 * DOWN)

        divisor = cherchons.get_part_by_tex("crible")
        divisor.set_color(TEAL)

        # Affiche les nombres
        self.play(
            ShowIncreasingSubsets(numbers, run_time=2),
        )
        self.play(
            Write(cherchons),
        )

        self.wait(2)

        self.play(
            FadeOut(cherchons),
        )

        # Recherche des nombres premiers
        noprimes = []
        pospal = -1
        all_noprimes_cross_selected = []
        nb_iter = int(maxnumber**0.5)
        for n in range(2, nb_iter + 1):

            # Si ce n'est pas un nombre premier on continue
            if n in noprimes:
                continue

            pospal += 1

            # Configure le text du nombre premier
            cprime = self.palette[pospal]
            tisprime = TextMobject(
                n, "est premier\\\\",
                "Nous supprimons les multiples de", f'{n}\\\\',
                '\\`a partir de', f'${n}^2={int(n)**2}$',
            )

            tisprime.scale(0.8)
            tisprime.next_to(ORIGIN, 10 * DOWN)
            tisprime[0].set_color(cprime)
            tisprime[3].set_color(cprime)
            tisprime[5].set_color(cprime)

            # Rectangle de selection (du nombre premier et du multiple et position du carée(power))
            rprime = SurroundingRectangle(
                numbers[n - 1], color=cprime)
            rmultiple = SurroundingRectangle(
                tisprime[5], color=cprime
            )
            rsquare = SurroundingRectangle(
                numbers[n**2 -
                        1], color=cprime)

            # Affiche le resultat du nombre premier
            self.play(
                ShowCreation(rprime),
                FadeIn(tisprime),
                FadeIn(rmultiple),
            )
            self.wait()

            # Configure les coches des nombres non premier
            noprimes_cross_selected = []
            for sn in range(n**2, maxnumber + 1, n):
                noprimes.append(numbers[sn - 1].get_value())

                noprimes_cross_selected.append(
                    Cross(SurroundingRectangle(
                        numbers[sn - 1])).set_color(cprime)
                )

            # Mémorise toutes les choches (pour pouvoir les éffacer par la suite)
            all_noprimes_cross_selected.extend(noprimes_cross_selected)

            # Deplace les rectangle de selection vers la position du carée(power)
            self.play(
                Transform(rprime, rsquare),
                Transform(rmultiple, rsquare),
            )

            self.play(
                FadeOut(rprime),
                FadeOut(rmultiple),
                FadeOut(rsquare),
            )

            # On coche tous les nombres non premier
            self.play(
                FadeOut(tisprime),

                LaggedStartMap(
                    ShowCreation,
                    noprimes_cross_selected,
                ),
                run_time=2
            )

        # Affiche les informations du résultat final
        nb_primes = maxnumber - len(set(noprimes)) - 1
        tresult = TextMobject(
            "Nous avons trouv\\'e", nb_primes, f"nombres premiers (sur {maxnumber} nombres)\\\\",
            "En", f"{nb_iter} it\\'erations",
        )

        tresult.scale(0.8)
        tresult.next_to(ORIGIN, 10 * DOWN)
        tresult[1].set_color(TEAL)
        tresult[-1].set_color(TEAL)

        all_noprimes_numbers = [
            ApplyMethod(numbers[np - 1].set_opacity, 0.2)
            for np in noprimes
        ]

        self.play(
            Write(tresult),
            LaggedStartMap(FadeOut, all_noprimes_cross_selected),
            LaggedStart(*all_noprimes_numbers),
            run_time=2,
        )
        self.wait(5)
