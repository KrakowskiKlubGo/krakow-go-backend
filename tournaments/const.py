from django.db import models


PLAYER_ON_REGISTER_LIST_RESPONSE_MESSAGE = {
    "pl": "Zostałeś zapisany na turniej. Do zobaczenia!",
    "en": "You have been registered for the tournament. See you there!",
}

PLAYER_ON_WAITING_LIST_RESPONSE_MESSAGE = {
    "pl": "Zostałeś dodany do listy oczekujących.",
    "en": "You have been added to the waiting list.",
}


class RuleSystem(models.TextChoices):
    MAC_MAHON = "mac_mahon", "MacMahon"
    SWISS = "swiss", "Swiss"
    ROUND_ROBIN = "round_robin", "Round Robin"
    SWISS_ROUND_ROBIN = "swiss_round_robin", "Swiss Round Robin"


class TournamentClass(models.TextChoices):
    A = "A", "A"
    B = "B", "B"
    C = "C", "C"
    D = "D", "D"


class TournamentResultType(models.TextChoices):
    GAMES_LIST = "games_list", "Games list"
    PLAYERS_LIST = "players_list", "Players list"
    STANDINGS = "standings", "Standings"


class PlayerRank(models.TextChoices):
    EGF_5_PRO = "5p", "5 pro"
    EGF_4_PRO = "4p", "4 pro"
    EGF_3_PRO = "3p", "3 pro"
    EGF_2_PRO = "2p", "2 pro"
    EGF_1_PRO = "1p", "1 pro"
    EGF_9_DAN = "9d", "9 dan"
    EGF_8_DAN = "8d", "8 dan"
    EGF_7_DAN = "7d", "7 dan"
    EGF_6_DAN = "6d", "6 dan"
    EGF_5_DAN = "5d", "5 dan"
    EGF_4_DAN = "4d", "4 dan"
    EGF_3_DAN = "3d", "3 dan"
    EGF_2_DAN = "2d", "2 dan"
    EGF_1_DAN = "1d", "1 dan"
    EGF_1_KYU = "1k", "1 kyu"
    EGF_2_KYU = "2k", "2 kyu"
    EGF_3_KYU = "3k", "3 kyu"
    EGF_4_KYU = "4k", "4 kyu"
    EGF_5_KYU = "5k", "5 kyu"
    EGF_6_KYU = "6k", "6 kyu"
    EGF_7_KYU = "7k", "7 kyu"
    EGF_8_KYU = "8k", "8 kyu"
    EGF_9_KYU = "9k", "9 kyu"
    EGF_10_KYU = "10k", "10 kyu"
    EGF_11_KYU = "11k", "11 kyu"
    EGF_12_KYU = "12k", "12 kyu"
    EGF_13_KYU = "13k", "13 kyu"
    EGF_14_KYU = "14k", "14 kyu"
    EGF_15_KYU = "15k", "15 kyu"
    EGF_16_KYU = "16k", "16 kyu"
    EGF_17_KYU = "17k", "17 kyu"
    EGF_18_KYU = "18k", "18 kyu"
    EGF_19_KYU = "19k", "19 kyu"
    EGF_20_KYU = "20k", "20 kyu"
    EGF_21_KYU = "21k", "21 kyu"
    EGF_22_KYU = "22k", "22 kyu"
    EGF_23_KYU = "23k", "23 kyu"
    EGF_24_KYU = "24k", "24 kyu"
    EGF_25_KYU = "25k", "25 kyu"
    EGF_26_KYU = "26k", "26 kyu"
    EGF_27_KYU = "27k", "27 kyu"
    EGF_28_KYU = "28k", "28 kyu"
    EGF_29_KYU = "29k", "29 kyu"
    EGF_30_KYU = "30k", "30 kyu"
