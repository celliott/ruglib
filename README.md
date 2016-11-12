# ruglib

Because rugs tie the room together.

### Project setup
- Requires Docker and Docker Compose
- Requires `make` to be installed
- Clone this repo, navigate to it: `cd ruglib`

#### Managing Local Dev with Make and Docker Compose
- `make build_rugs` To Build rugs Container
- `make up_local` To start Local Dev ENV

#### Logger Demo
URI Breakdown `/<topic>/<method>`
- Open in Terminal Window and run `make tail_logger`
- Open Second Terminal Window and run the following commands. View results in First Window.

To Capitalize Text
```sh
curl -X POST -H "Content-Type: application/json" \
	-u admin:zer0 http://localhost/logger/capitalize \
	-d '{"text":"make me capitol"}'
```

To Uppercase Text	
```sh
curl -X POST -H "Content-Type: application/json" \
	-u admin:zer0 http://localhost/logger/upper \
	-d '{"text":"make me louder"}'
```

To Titlecase Text
```sh
curl -X POST -H "Content-Type: application/json" \
	-u admin:zer0 http://localhost/logger/title \
	-d '{"text":"title me"}'
```

To Lowercase Text
```sh
curl -X POST -H "Content-Type: application/json" \
	-u admin:zer0 http://localhost/logger/lower \
	-d '{"text":"MAKE ME QUIETER"}'
```

- `make down` To shutdown your Local Dev ENV
