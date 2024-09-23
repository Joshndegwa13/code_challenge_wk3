from models import Band, Venue, Concert
import db_setup

def main():
    db_setup.setup_database()  

    
    band1 = Band("Hart the Band", "Nairobi")
    band1.save()

    band2 = Band("Sauti Sol", "Nairobi")
    band2.save()

    venue1 = Venue("Canivore Grounds", "Nairobi")
    venue1.save()

    venue2 = Venue("KICC", "Nairobi")
    venue2.save()

    concert1 = Concert(1, 1, "2024-12-01")
    concert1.save()

    concert2 = Concert(2, 2, "2024-12-15")
    concert2.save()

    
    print(f"Band with most performances: {Band.most_performances()}")
    print(f"Most frequent band at Canivore Grounds: {Venue.most_frequent_band('Canivore Grounds')}")

if __name__ == "__main__":
    main()
