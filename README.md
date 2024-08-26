# django_template

## installation

```bash
$ poetry install
$ python ./manage.py runserver
```

```bash
# Secret Manager 에 등록한 정보 확인 및 로컬에 .env 만들기
$ aws secretsmanager get-secret-value --region ap-northeast-2 --secret-id XXXXXXXXX --query SecretString --output text | jq -r '.dev | to_entries | .[] | "\(.key)=\(.value)"' > .env

# .env 파일 확인
$ cat .env
```

## test

```bash
python manage.py test      
```

## contributing

```bash
$ pre-commit install  # required!
$ pre-commit run --all-files  # required!
$ git commit
```
