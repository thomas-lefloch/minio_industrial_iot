# Contexte
Projet réalisé dans un but d'apprentissage

## Objectif 
Faciliter le développement d'un outil de maintenance prédictive.  
Aujourd'hui, les données sont stockés en vrac, sans structure ni gouvernance.
Il faut la structurer.

## Dataset source
Dataset utilisé: https://zenodo.org/records/15277168

| Fichier | # Lignes | Entête csv | 
|:--------|:--------:|:-----------|
| LineA_Stable_10K.csv|10000|timestamp,Temperature,pressure,elapsed_time,label |
| LineB_Flux.csv|5000|timestamp,temperature,pressure,Elapsed_time,label |
| LineC_Turbulent.csv|5000|timestamp,Temperature,pressure,label |
| LineD_SpikeControl.csv|5000|timestamp,temperature,Pressure,label |
| LineE_SmoothRun.csv|5000|timestamp,Temperature,pressure,label |

# Etape 1: harmoniser et s'assurer de la qualité de la donnée

## Stockage de la donnée
### Buckets Minio
4 buckets, 1 par étape de la pipeline :
- raw
- staging
- curated
- archived

### Partionnement
Chaque bucket est partitioné par ligne de production (production_line), puis par année (year) et par mois (month).

## Création d'une pipeline d'ingestion de donnée
### Source -> Raw
On stocke et partitionne les fichiers tel quel, dans le bucket `raw` brief 

### Raw -> Staging
On harmonise et explicite les noms des champs
On ignore les colonnes `Elapsed_time` qui ne nous est pas utile dans ce contexte.
//TODO tableau correpondance des champs

| production_line | mesured_at | temperature_in_celcius | pressure_in_bar | is_anomaly |
|:--|:-------|:-------|:-------|:-------|:-------|

### Staging -> Curated
On supprime les anomalies (`is_anomaly` = 1). La colonne `is_anomaly` disparaît elle aussi

### Curated -> Archived
Données des 180 derniers jours archivés. 

