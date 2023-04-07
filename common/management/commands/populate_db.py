import datetime

from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import now

from meetings.models import Meeting
from tournaments.const import TournamentClass, PlayerRank, RuleSystem
from tournaments.models import Tournament, Registration, RegisteredPlayer


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        szop_3 = Tournament.objects.create(
            name_pl="Turniej w Szopie III",
            name_en="III Tournament in shop",
            image="logo.png",
            start_date=datetime.date(2023, 2, 11),
            end_date=None,
            place="Shop Gracz",
            is_ended=False,
            is_draft=False,
            results="",
            organizer="Adam Białożyt, Maria Kluziak, Jakub Miłkowski",
            referee="Jakub Miłkowski",
            description_pl="Serdecznie zapraszamy na 3 turniej w Szopie",
            description_en="We invite you to the 3rd tournament in the shop",
            additional_info_pl="W razie pytań o nocleg, dojazd na miejsce turnieju, "
            "itp. prosimy o kontakt z organizatorami turnieju.",
            additional_info_en="In case of questions about accommodation, "
            "arrival to the tournament venue, etc. please contact the tournament organizers.",
            address="ul. Bolesława Limanowskiego 16, 30-534 Kraków",
            address_map_link="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d10248.85103357987!2d19.9526665!3d50.0448456!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xbc6417b1f2f072fc!2sShop%20Gracz%20-%20sklep%20z%20grami%20planszowymi%2C%20karcianymi%20i%20bitewnymi!5e0!3m2!1spl!2spl!4v1656874508210!5m2!1spl!2spl",
            prizes_pl="Pieniądze dla zwycięzcy, bony od Szopa gracza",
            prizes_en="Money for the winner, vouchers from the player's shop",
            fee_pl="20 zł dla każdego gracza",
            fee_en="20 zł for every player",
            prepaid_option=False,
            # ruleset
            game_rules_pl="japońskie",
            game_rules_en="japanese",
            komi="6.5",
            rules_system=RuleSystem.MAC_MAHON,
            tournament_class=TournamentClass.C,
            rounds=4,
            handicap_rules_pl="Handicap redukowany o 2, 9 kamieni max",
            handicap_rules_en="Handicap reduced by 2, 9 stones max",
            time_control="25 min + 1 x 15s byo-yomi ",
        )
        Registration.objects.create(
            tournament=szop_3,
            end_date=datetime.date(2023, 2, 10),
            player_limit=22,
            description_en="In case of exceeding the competitor limit, "
            "the participation precedence is given to preregistered players",
            description_pl="W przypadku osiągnięcia limitu uczestników "
            "pierwszeństwo udziału w turnieju przysługuje zarejestrowanym graczom",
        )
        RegisteredPlayer.objects.bulk_create(
            [
                RegisteredPlayer(
                    tournament=szop_3,
                    first_name="Gal",
                    last_name="Anonim",
                    rank=PlayerRank.EGF_1_DAN,
                    city_club="Klub Go",
                    country="PL",
                    email=None,
                    phone=None,
                    is_paid=False,
                    egf_pid=None,
                )
                for _ in range(24)
            ]
        )
        self.stdout.write("Tournaments created.", ending="\n")

        Meeting.objects.create(
            name_pl="Spotkanie klubu w Artefakcie",
            name_en="Club meeting in Artefakt",
            description_pl="Serdecznie zapraszamy",
            description_en="We invite you",
            date=(now() + datetime.timedelta(days=6)).date(),
            start_time=datetime.time(hour=18),
            end_time=None,
            address="Artefact Cafe ul. Dajwór 3",
            address_map_link="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2561.8130792673046!2d19.946771415320175!3d50.05233277942241!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47165b18f5c5bdc1%3A0x4864fed2dc9a1047!2sArtefakt+Cafe!5e0!3m2!1spl!2spl!4v1565187353227!5m2!1spl!2spl",
        )
        Meeting.objects.create(
            name_pl="Spotkanie klubu w Artefakcie",
            name_en="Club meeting in Artefakt",
            description_pl="Serdecznie zapraszamy",
            description_en="We invite you",
            date=(now() + datetime.timedelta(days=15)).date(),
            start_time=datetime.time(hour=18),
            end_time=None,
            address="Artefact Cafe ul. Dajwór 3",
            address_map_link="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2561.8130792673046!2d19.946771415320175!3d50.05233277942241!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47165b18f5c5bdc1%3A0x4864fed2dc9a1047!2sArtefakt+Cafe!5e0!3m2!1spl!2spl!4v1565187353227!5m2!1spl!2spl",
        )

        self.stdout.write("Meetings created.", ending="\n")
