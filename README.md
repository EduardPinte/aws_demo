\# Demonstrație AWS S3 cu MiniStack



Proiect educațional care demonstrează utilizarea unui serviciu S3

emulat local prin MiniStack, folosind Python și biblioteca Boto3.



\## Arhitectură



Program Python → MiniStack → S3 emulat



Programul creează un bucket, încarcă un fișier, listează obiectele,

descarcă fișierul și compară conținutul descărcat cu originalul.



\## Cerințe



\- Docker Desktop pornit

\- Python 3

\- Acces la internet pentru descărcarea imaginii și bibliotecilor



Nu este necesar un cont AWS. Programul folosește credențiale fictive

și trimite cererile către http://localhost:4566.



\## Pornirea MiniStack



```bat

docker run --detach --name ministack-demo -p 127.0.0.1:4566:4566 ministackorg/ministack

```



Dacă acest container a fost deja creat, pornește-l cu:



```bat

docker start ministack-demo

```



Verifică pornirea:



```bat

docker ps

docker logs ministack-demo

```



\## Instalare pe Windows



Deschide terminalul în folderul proiectului:



```bat

py -m venv .venv

.venv\\Scripts\\python.exe -m pip install -r requirements.txt

```



\## Rulare



```bat

.venv\\Scripts\\python.exe demo.py

```



Programul generează automat fișierul document.txt și descarcă

obiectul sub numele document-descarcat.txt.



\## Validare



Demonstrația a fost rulată cu succes. A fost creat bucket-ul

documente-demo, iar fișierul a fost încărcat, listat și descărcat.



Programul compară fișierele octet cu octet. Rezultatul obținut:



```text

VERIFICARE REUȘITĂ: fișierele sunt identice.

```



La rulările următoare, programul reutilizează bucket-ul existent.



\## Oprire



```bat

docker stop ministack-demo

```



\## Limite



Exemplul verifică operații de bază într-un mediu emulat local.

Nu măsoară performanța, disponibilitatea sau securitatea AWS real.

Datele din emulator nu trebuie considerate persistente după

eliminarea containerului, deoarece proiectul nu configurează

stocare persistentă.



\## Surse



\- MiniStack: https://ministack.org/

\- Documentație MiniStack: https://ministack.org/docs/

\- Amazon S3: https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html

\- Boto3 S3: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html

