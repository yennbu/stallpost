# Automatiserade mailutskick för stallet

Python-skript som automatiserar månatliga mailutskick via Gmail för att påminna om att till exempel boka tid för hovslagare. Projektet körs serverlöst i molnet med hjälp av GitHub Actions.

## Funktioner
* **Automatiserad drift:** Schemalagd att köras automatiskt en gång i månaden via GitHub Actions (Cron-jobb).
* **Säker hantering av data:** Inga lösenord eller mailadresser är hårdkodade. All känslig data hanteras säkert via miljövariabler (`.env` lokalt och *GitHub Secrets* i produktion).
* **Robust integration:** Använder standardiserad SMTP-koppling mot Gmails servrar med applösenord.

## Tekniker
* **Python 3**
* **GitHub Actions** (CI/CD / Automatisering)
* **python-dotenv** (För lokal konfiguration)

## Produktionssättning (GitHub Actions)
För att köra skriptet i molnet är samma variabler uppsatta under **Settings -> Secrets and variables -> Actions** i detta repository. Filen `.github/workflows/run_script.yml` styr schemaläggningen.
