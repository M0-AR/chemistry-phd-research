Output docs/demo.gif
Require ffmpeg
Hide
Type "docker compose up -d --build research" Enter Sleep 1s
Type "docker compose exec -T research python -m pytest tests/ -q" Enter Sleep 2s
Type "docker compose exec -T research make benchmark-all" Enter Sleep 2s
Show
Loop 0
