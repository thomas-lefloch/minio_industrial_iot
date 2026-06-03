set shell := ["powershell.exe", "-NoProfile", "-Command"]

compose_up:
	docker compose up -d

init_minio:
	python minio/setup.py
	python minio/upload_files.py

