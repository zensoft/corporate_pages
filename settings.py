DATABASE = "bonprix_platform_pl_2"
USER = "bonprix_platform_user"
PASS = "B@nprix11Pl@tform"
HOST = "localhost"
PORT = "5002"

COUNTRIES = ("hu","pl","ro","sk","ua")

OUT_SQL_PATH = "out_sql/"
SQL_SUFFIX = ".sql"

CRITICAL_CSS_PATH = "/home/tomek/rwd_views/bpx-rwd-templ/branches/16.45/corpo-pages/src/temp/criticalCss/"
CSS_SUFFIX = ".css"
FRONT_VIEWS_PATH = "/home/tomek/rwd_views/bpx-rwd-templ/branches/16.45/corpo-pages/public/"
HTML_SUFFIX = ".html"

VIEWS = {
    "our": {
        "name": "Nasza odpowiedzialność",
        "id": 1,
        "parent_id": 0,
        "friendly_url" : "nasza-odpowiedzialnosc",
        "page_path_ids" : "1"
    },
    "environment": {
        "name": "Środowisko",
        "id": 2,
        "parent_id": 1,
        "friendly_url" : "srodowisko",
        "page_path_ids" : "1,2"
    },
    "resources": {
        "name": "Przyrodnicze zasoby",
        "id": 3,
        "parent_id": 2,
        "friendly_url" : "przyrodnicze-zasoby",
        "page_path_ids" : "1,2,3"
    },
    "transport": {
        "name": "Transport",
        "id": 4,
        "parent_id": 2,
        "friendly_url" : "transport",
        "page_path_ids" : "1,2,4"
    },
    "climate": {
        "name": "Klimat",
        "id": 5,
        "parent_id": 2,
        "friendly_url" : "klimat",
        "page_path_ids" : "1,2,5"
    },
    "working_conditions" : {
        "name": "Warunki pracy",
        "id": 6,
        "parent_id": 1,
        "friendly_url" : "warunki-pracy",
        "page_path_ids" : "1,6"
    },
    "supply": {
        "name": "Łańcuch dostawczy",
        "id": 7,
        "parent_id": 6,
        "friendly_url" : "lancuch-dostawczy",
        "page_path_ids" : "1,6,7"
    },
    "codex": {
        "name": "Kodeks postępowania",
        "id": 8,
        "parent_id": 6,
        "friendly_url" : "kodeks-postepowania",
        "page_path_ids" : "1,6,8"
    },
    "assortment": {
        "name": "Asortyment",
        "id": 9,
        "parent_id": 1,
        "friendly_url" : "asortyment",
        "page_path_ids" : "1,9"
    },
    "products": {
        "name": "Zrównoważone produkty",
        "id": 10,
        "parent_id": 9,
        "friendly_url" : "zrownowazone-produkty",
        "page_path_ids" : "1,9,10"
    },
    "quality": {
        "name": "Jakość produktów",
        "id": 11,
        "parent_id": 9,
        "friendly_url" : "jakosc-produktow",
        "page_path_ids" : "1,9,11"
    },
    "engagement": {
        "name": "Zaangażowanie",
        "id": 12,
        "parent_id": 1,
        "friendly_url" : "zaangazowanie",
        "page_path_ids" : "1,12"
    }
}