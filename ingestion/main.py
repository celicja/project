from app.csv_loader import load_csv

def main():
    print("Starting ingestion...")
    load_csv()
    print("Ingestion finished")

if __name__ == "__main__":
    main()