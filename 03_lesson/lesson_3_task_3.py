from address import Address
from mailing import Mailing

otpr = Mailing(
    Address(141200, "Moscow", "Krasnaya Plozchad", 12, 456),
    Address(123415, "Magadan", "Severnaya", 2, 91),
    319.12,
    100467319
    )

print(f"Отправление {otpr.track} из {otpr.from_address.zipcode}, \
{otpr.from_address.city}, {otpr.from_address.street}, \
{otpr.from_address.building}-{otpr.from_address.apartment} \
в {otpr.to_address.zipcode}, {otpr.to_address.city}, \
{otpr.to_address.street}, {otpr.to_address.building}\
-{otpr.to_address.apartment}. Стоимость {otpr.cost} \
рублей.")
