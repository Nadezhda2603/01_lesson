from smartphone import Smartphone
catalog = [Smartphone("Nokia", "250", "+79992221133"),
           Smartphone("Samsung", "S25", "+79995551122"),
           Smartphone("Ericsson", "J3", "+79993330033"),
           Smartphone("Samsung", "C25", "+79990122233"),
           Smartphone("Sony", "1999", "+79999323241")
           ]
for i in catalog:
    print(f"{i.bernd} - {i.model}. {i.number}")
