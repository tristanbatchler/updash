from updash.core import get, patch, Response
from enum import StrEnum


class ParentCategory(StrEnum):
    SELF = "parent",
    GOOD_LIFE = "good-life",
    TRANSPORT = "transport"
    PERSONAL = "personal"
    HOME = "home"


class Category(StrEnum):
    SELF = "category"
    LIFE_ADMIN = "life-admin",
    TV_AND_MUSIC = "tv-and-music",
    EVENTS_AND_GIGS = "events-and-gigs",
    INTERNET = "internet",
    GOOD_LIFE = "good-life",
    NEWS_MAGAZINES_AND_BOOKS = "news-magazines-and-books",
    TECHNOLOGY = "technology",
    TAXIS_AND_SHARE_CARS = "taxis-and-share-cars",
    BOOZE = "booze",
    TRANSPORT = "transport",
    TOBACCO_AND_VAPING = "tobacco-and-vaping",
    HAIR_AND_BEAUTY = "hair-and-beauty",
    ADULT = "adult",
    PERSONAL = "personal",
    CAR_REPAYMENTS = "car-repayments",
    PUBS_AND_BARS = "pubs-and-bars",
    GROCERIES = "groceries",
    HEALTH_AND_MEDICAL = "health-and-medical",
    HOME_INSURANCE_AND_RATES = "home-insurance-and-rates",
    HOMEWARE_AND_APPLIANCES = "homeware-and-appliances",
    CLOTHING_AND_ACCESSORIES = "clothing-and-accessories",
    HOME_MAINTENANCE_AND_IMPROVEMENTS = "home-maintenance-and-improvements",
    RESTAURANTS_AND_CAFES = "restaurants-and-cafes",
    TOLL_ROADS = "toll-roads",
    UTILITIES = "utilities",
    HOME = "home",
    FITNESS_AND_WELLBEING = "fitness-and-wellbeing",
    CYCLING = "cycling",
    FAMILY = "family",
    GIFTS_AND_CHARITY = "gifts-and-charity",
    PUBLIC_TRANSPORT = "public-transport",
    GAMES_AND_SOFTWARE = "games-and-software",
    PETS = "pets",
    RENT_AND_MORTGAGE = "rent-and-mortgage",
    HOBBIES = "hobbies",
    FUEL = "fuel",
    CAR_INSURANCE_AND_MAINTENANCE = "car-insurance-and-maintenance",
    MOBILE_PHONE = "mobile-phone",
    EDUCATION_AND_STUDENT_LOANS = "education-and-student-loans",
    PARKING = "parking",
    HOLIDAYS_AND_TRAVEL = "holidays-and-travel",
    TAKEAWAY = "takeaway",
    LOTTERY_AND_GAMBLING = "lottery-and-gambling",
    INVESTMENTS = "investments",


def list_categories(
        parent_category: ParentCategory | None = None,
) -> Response:
    params = {}
    if parent_category:
        params[f"filter[{ParentCategory.SELF}]"] = parent_category
    return get("categories", params)


def get_category(_id: str) -> Response:
    return get(f"categories/{_id}")


def categorize_transaction(transaction_id: str,
                           category: Category) -> Response:
    return patch(f"transactions/{transaction_id}/relationships/category", {
        'data': {
            'type': 'categories',
            'id': category
        }
    })
